import curses
from random import randint
from settings import Direction, WINDOW_HEIGHT, WINDOW_WIDTH, SNAKE_LENGTH, TIMEOUT

class SnakeGame:
    def __init__(self):
        self.score = 0
        self.timeout = TIMEOUT
        self.snake = [[int(WINDOW_WIDTH/2), int(WINDOW_HEIGHT/2)]]
        self.direction = Direction.RIGHT
        for i in range(SNAKE_LENGTH - 1):
            self.snake.append([self.snake[i][0] - 1, self.snake[i][1]])
        self.food = None

    def create_food(self, window):
        while self.food is None:
            self.food = [randint(1, WINDOW_WIDTH - 2), randint(1, WINDOW_HEIGHT - 2)]
            if self.food in self.snake:
                self.food = None
        window.addch(self.food[1], self.food[0], chr(9608))

    def play_step(self, window):
        self.snake.insert(0, [self.snake[0][0] + (self.direction == Direction.RIGHT and 1) + (self.direction == Direction.LEFT and -1),
                         self.snake[0][1] + (self.direction == Direction.DOWN and 1) + (self.direction == Direction.UP and -1)])

        window.addch(self.snake[0][1], self.snake[0][0], chr(9608))

        if self.snake[0] == self.food:
            self.create_food(window)
        else:
            window.addch(self.snake[-1][1], self.snake[-1][0], ' ')
            self.snake.pop()

        return self.game_over(window)

    def game_over(self, window):
        if self.snake[0][0] == 0 or self.snake[0][0] == WINDOW_WIDTH - 1:
            return True
        if self.snake[0][1] == 0 or self.snake[0][1] == WINDOW_HEIGHT - 1:
            return True
        if self.snake[0] in self.snake[1:]:
            return True
        return False
