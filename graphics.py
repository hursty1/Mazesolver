from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
class Line:
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Window:
    def __init__(self, height:int, width:int):
        self.height = height
        self.width = width
        self.__root = Tk()
        self.__root.title = "Maze"
        self.canvas:Canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line:Line, fill_color:str="black"):
        line.draw(self.canvas, fill_color)

        
class Cell:
    def __init__(self, 
                win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win:Window = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_line)
        if self.has_top_wall:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_line)
        if self.has_bottom_wall:
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_line)
        if self.has_right_wall:
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_line)

    def get_center(self) -> Point:
        half = abs(self._x1 - self._x2) // 2
        return Point(self._x1 + half, self._y1 + half)
    
    def draw_move(self, to_cell, undo=False):
        color = 'red'
        if undo:
            color = 'grey'
        line = Line(self.get_center(), to_cell.get_center())
        self._win.draw_line(line,color)
        