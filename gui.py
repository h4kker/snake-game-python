from config import GAME_WIDTH, GAME_HEIGHT, BACKGROUND_COLOR, SPACE_SIZE, SNAKE_COLOR, SPEED
from food import Food
from snake import Snake
from tkinter import Frame, Label, Button, Canvas, ALL


class GameGUI:
    def __init__(self, window):
        self.window = window

        self.main_menu_frame = Frame(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg='gray')
        self.main_menu_frame.pack(fill="both", expand=True)

        title_label = Label(self.main_menu_frame, text="Snake Game", font=('consolas', 50), bg="black", fg="white")
        title_label.pack(pady=50)

        # Используем width и height для кнопок, чтобы они были одного размера
        button_options = {'font': ('consolas', 20),
                          'width': 20,
                          'height': 2}

        start_button = Button(self.main_menu_frame, text="Начать игру",
                              command=self.start_game_button, **button_options)
        start_button.pack(pady=10)

        records_button = Button(self.main_menu_frame, text="Рекорды",
                                command=self.show_records_button, **button_options)
        records_button.pack(pady=10)

        exit_button = Button(self.main_menu_frame, text="Выход",
                             command=self.exit_game_button, **button_options)
        exit_button.pack(pady=10)

        # Создаем фрейм для игры
        self.game_frame = Frame(window, bg="black")

        # Фрейм для счета и кнопки рестарта
        self.score_frame = Frame(self.game_frame)
        self.score_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.label = Label(self.score_frame, text=f'Score: {0}', font=('consolas', 40))
        self.label.grid(row=0, column=1, sticky='w', padx=10)

        # Кнопка рестарт
        restart_button = Button(self.score_frame, text='Restart', font=('consolas', 20), command=self.restart_game)
        restart_button.grid(row=0, column=0, sticky='e', padx=10)

        self.canvas = Canvas(self.game_frame, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Привязываем управление к стрелкам
        window.bind('<Left>', lambda event: self.change_direction('left'))
        window.bind('<Right>', lambda event: self.change_direction('right'))
        window.bind('<Up>', lambda event: self.change_direction('up'))
        window.bind('<Down>', lambda event: self.change_direction('down'))

        # Инициализация переменных
        self.score = 0
        self.direction = 'down'
        self.snake = None
        self.food = None

    def start_game_button(self):
        self.main_menu_frame.pack_forget()  # Скрываем главное меню
        self.game_frame.pack()  # Показываем фрейм игры
        self.restart_game()  # Перезапуск игры
        # Динамическое определение высоты canvas

    def show_records_button(self):
        print("Records soon")

    def exit_game_button(self):
        self.window.destroy()

    def next_turn(self):
        x, y = self.snake.coordinates[0]
        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        self.snake.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        self.snake.squares.insert(0, square)

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.label.config(text=f'Score: {self.score}')
            self.canvas.delete("Food")
            self.food = Food(self.snake.coordinates, self.canvas)
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collisions(self.snake):
            self.game_over()
        else:
            self.window.after(SPEED, self.next_turn)

    def change_direction(self, new_direction):
        if new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

    def check_collisions(self, snake):
        x, y = snake.coordinates[0]
        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True
        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True
        return False

    def game_over(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2, font=('consolas', 70),
                                text="GAME OVER", fill='red', tag="Game over")

    def restart_game(self):
        self.canvas.delete(ALL)
        self.score = 0
        self.direction = 'down'

        # Инициализация объекта Snake и Food
        self.snake = Snake(self.canvas)
        self.food = Food(self.snake.coordinates, self.canvas)
        self.label.config(text=f"Score: {self.score}")

        # Вызов метода next_turn()
        self.next_turn()
