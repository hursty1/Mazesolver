
from graphics import Window, Line, Point, Cell
from maze import maze
if __name__ == "__main__":
    win = Window(800, 600)
    num_rows = 10
    num_cols = 10
    margin = 50
    screen_x = 600
    screen_y = 400
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    maze = maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()