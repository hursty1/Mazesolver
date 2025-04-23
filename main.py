
from graphics import Window, Line, Point, Cell
    
if __name__ == "__main__":
    win = Window(800, 600)
    # win.draw_line(Line(Point(1,1), Point(23,23)),"red")
    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c1 = Cell(win)
    c1.has_top_wall = False
    c1.draw(300, 300, 500, 500)

    c.draw_move(c1)

    c2 = Cell(win)
    c2.draw(200,200,240,240)

    win.wait_for_close()