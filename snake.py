from config import BODY_PARTS, SPACE_SIZE, SNAKE_COLOR


class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = [[i * SPACE_SIZE, 0] for i in range(BODY_PARTS)]
        self.squares = []
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="Snake")
            self.squares.append(square)
