class TinyLCD(object):
    """
    A simulated LCD screen with a grid of LEDs that can either be on or off.
    The __str__ method implements a nice visual reference
    """
    ACTIVACTED_CHAR = '#'

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[None for j in range(columns)] for i in range(rows)]

    def activate_region(self, width, height):
        """
        Activates a rectangle starting from the the top left (0,0)
        :param width: the number of columns to fill
        :param height: the number of rows to fill
        :return:
        """
        for i in range(height):
            for j in range(width):
                self.matrix[i][j] = TinyLCD.ACTIVACTED_CHAR

    def rotate_column(self, column_index, amount):
        """
        Shifts the specified column down by the specified amount; wrapping when necessary
        :param column_index:
        :param amount:
        :return:
        """
        modified_column = [None for i in range(self.rows)]

        for row_index in range(self.rows):
            if self.matrix[row_index][column_index] == TinyLCD.ACTIVACTED_CHAR:
                if row_index + amount >= self.rows:
                    new_index = (row_index + amount) % self.rows
                else:
                    new_index = row_index + amount
                modified_column[new_index] = TinyLCD.ACTIVACTED_CHAR

        # I'm not writing in place because I'm afraid it will clobber somehow. need to test though
        for row_index in range(self.rows):
            self.matrix[row_index][column_index] = modified_column[row_index]

    def rotate_row(self, row_index, amount):
        """
        Shifts the specified row right by the specified amount; wrapping when necessary
        :param row_index:
        :param amount:
        :return:
        """
        modified_row = [None for i in range(self.columns)]

        for column_index in range(self.columns):
            if self.matrix[row_index][column_index] == TinyLCD.ACTIVACTED_CHAR:
                if column_index + amount >= self.columns:
                    new_index = (column_index + amount) % self.columns
                else:
                    new_index = column_index + amount
                modified_row[new_index] = TinyLCD.ACTIVACTED_CHAR

        self.matrix[row_index] = modified_row

    def get_total_activated(self):
        total = 0

        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] == TinyLCD.ACTIVACTED_CHAR:
                    total += 1

        return total

    def __str__(self):
        pretty_lcd = ""

        for row_index in range(self.rows):
            for column_index in range(self.columns):
                if self.matrix[row_index][column_index] is None:
                    pretty_lcd += "."
                else:
                    pretty_lcd += self.matrix[row_index][column_index]
            pretty_lcd += "\n"

        return pretty_lcd
