class Cell(object):
    def __init__(self, x, y, key):
        self.x = x
        self.y = y
        self.key = key


class ComplexKeyPad(object):
    """
    #############
    #     1     #
    #   2 3 4   #
    # 5 6 7 8 9 #
    #   A B C   #
    #     D     #
    #############

    taken from: http://adventofcode.com/2016/day/2
    """
    KEYS = [
        [None,  None,   '1',    None,   None],
        [None,  '2',    '3',    '4',    None],
        ['5',   '6',    '7',    '8',    '9'],
        [None,  'A',    'B',    'C',    None],
        [None,  None,   'D',    None,   None]
    ]

    NUM_ROWS = NUM_COLS = 5

    def __init__(self):
        self.matrix = [[Cell(x, y, ComplexKeyPad.KEYS[x][y]) for y in range(ComplexKeyPad.NUM_ROWS)] for x in range(ComplexKeyPad.NUM_COLS)]
        self.current_cell = self.matrix[2][0]

    def push_up(self):
        if (self.current_cell.x - 1) < 0:
            return self.current_cell

        intended_cell = self.matrix[self.current_cell.x - 1][self.current_cell.y]
        return self._set_new_cell_if_valid(intended_cell)

    def push_down(self):
        if (self.current_cell.x + 1) >= ComplexKeyPad.NUM_ROWS:
            return self.current_cell

        intended_cell = self.matrix[self.current_cell.x + 1][self.current_cell.y]
        return self._set_new_cell_if_valid(intended_cell)

    def push_right(self):
        if (self.current_cell.y + 1) >= ComplexKeyPad.NUM_COLS:
            return self.current_cell

        intended_cell = self.matrix[self.current_cell.x][self.current_cell.y + 1]
        return self._set_new_cell_if_valid(intended_cell)

    def push_left(self):
        if (self.current_cell.y - 1) < 0:
            return self.current_cell

        intended_cell = self.matrix[self.current_cell.x][self.current_cell.y - 1]
        return self._set_new_cell_if_valid(intended_cell)

    def _set_new_cell_if_valid(self, intended_cell):
        if intended_cell.key is None:
            return self.current_cell
        else:
            self.current_cell = intended_cell
            return intended_cell
