import time
from graphics import Cell, Window

class maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win:Window = win
        self._cells=[]
        self._create_cells()
        self._break_entrance_exit()
    def _create_cells(self):
        for col in range(self.num_cols):
            self._cells.append([])
            for row in range(self.num_rows):
                c = Cell(self.win)
                self._cells[col].append(c)
                self._draw_cell(col,row)
    def _draw_cell(self,i,j):
        if self.win is None:
            return
        #cell size * col = top_left postion
        cell:Cell = self._cells[i][j]
        cell.draw(
            self.x1 + i*self.cell_size_x, 
            self.y1 + j*self.cell_size_y, 
            self.x1 + i*self.cell_size_x + self.cell_size_x, 
            self.y1 + j*self.cell_size_y + self.cell_size_y
            )
        self._animate()
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_exit(self):
        self._cells[0][0].has_left_wall = False
        
        self._draw_cell(0,0)

        self._cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)