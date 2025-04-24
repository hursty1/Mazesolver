import random
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
        seed=None
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
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        self.solve()
        if seed != None:
            random.seed(seed)
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

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True #mark current cell as visited
        running = True
        while running:
            to_visit = []

            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]
            #determine direction
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
                
            #move 
            self._break_walls_r(next_index[0], next_index[1])
    def _solve_r(self, i, j) -> bool:
        "using depth-first algorithm"
        #animate
        self._animate()
        #mark visited
        self._cells[i][j].visited = True

        #if end return true
        if i == self.num_cols - 1 and j == self.num_rows -1:
            return True #exit
        print('solving')
        directions = ['left', 'right', 'top', 'bottom']
        # for direction in directions:
        #     if direction == 'left':
        if i > 0 and not self._cells[i - 1][j].visited and \
        not self._cells[i][j].has_left_wall:
            
            self._cells[i][j].draw_move(self._cells[i-1][j])
            result = self._solve_r(i-1,j)
            if result:
                return result
            else:
                # self._cells[i][j].draw_move(self._cells[i-1][j])
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
            # if direction == 'right':


        if i < self.num_cols - 1 and \
        not self._cells[i + 1][j].visited and \
        not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            result = self._solve_r(i+1,j)
            if result:
                return result
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
            # if direction == 'up':


        if j > 0 and not self._cells[i][j - 1].visited and \
        not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            result = self._solve_r(i,j - 1)
            if result:
                return result
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
            # if direction == 'down':
        if j < self.num_rows - 1 and not self._cells[i][j + 1].visited and \
        not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            result = self._solve_r(i,j+1)
            if result:
                return result
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        #for each direction
            #if cell in that direction and no wall and not visited
            #call solve_r in that direction
            #if true return true
            #else draw undo and try next direction

        #if no direction remain return false
        return False
        
    def solve(self):
        result = self._solve_r(0,0)
        return result