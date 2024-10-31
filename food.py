import random
from config import SPACE_SIZE, FOOD_COLOR, GAME_WIDTH, GAME_HEIGHT


class Food:
    def __init__(self, snake_coordinates, canvas):
        self.coordinates = self.generate_food_coordinates(snake_coordinates)
        x, y = self.coordinates
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="Food")

    def generate_food_coordinates(self, snake_coordinates):
        while True:
            x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, ((GAME_HEIGHT) / SPACE_SIZE) - 1) * SPACE_SIZE
            if (x, y) not in [tuple(coord) for coord in snake_coordinates]:
                return [x, y]
