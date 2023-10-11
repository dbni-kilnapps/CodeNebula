import curses
from gameplay import SnakeGame
from settings import Direction, WINDOW_WIDTH, WINDOW_HEIGHT

def main(stdscr):
    curses.curs_set(0)
    window = curses.newwin(WINDOW_HEIGHT, WINDOW_WIDTH, 0, 0)
    window.keypad(1)
    window.timeout(100)

    game = SnakeGame()
    game.create_food(window)

    while True:
        window.border(0)
        window.addstr(0, 2 , 'Score : ' + str(game.score) + ' ')
        event = window.getch()

        if event == ord('q'):
            break
        elif event == ord('w'):
            game.direction = Direction.UP
        elif event == ord('s'):
            game.direction = Direction.DOWN
        elif event == ord('a'):
            game.direction = Direction.LEFT
        elif event == ord('d'):
            game.direction = Direction.RIGHT

        if game.play_step(window):
            break

if __name__ == "__main__":
    curses.wrapper(main)
