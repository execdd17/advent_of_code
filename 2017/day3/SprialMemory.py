class SpiralMemory(object):
    def __init__(self, total_elements):
        self.total_elements = total_elements
        self._create_board(total_elements)

    def _create_board(self, total_elements):
        starting_board = [[5, 4, 3], [6, 1, 2], [7, 8, 9]]
        augmented_board, center = self._create_board_helper(
            board=starting_board,
            rows=3,
            columns=3,
            max_num=total_elements,
            center=(1, 1)
        )
        self.center = center
        self.board = augmented_board

    def _create_board_helper(self, board, rows, columns, max_num, center):
        current_num = board[rows - 1][columns - 1]

        if current_num >= max_num:
            return board, center
        else:
            new_board = [[None for j in range(rows + 2)] for i in range(columns + 2)]

            # copy original values to new board
            for i in range(rows):
                for j in range(columns):
                    new_board[i+1][j+1] = board[i][j]

            current_num += 1
            new_board[rows][columns + 1] = current_num

            for i in reversed(range(rows)):
                current_num += 1
                new_board[i][columns + 1] = current_num

            for j in reversed(range(columns + 1)):
                current_num += 1
                new_board[0][j] = current_num

            for i in range(rows + 1):
                current_num += 1
                new_board[i + 1][0] = current_num

            for j in range(columns + 1):
                current_num += 1
                new_board[rows + 1][j + 1] = current_num

            new_center = (center[0] + 1, center[1] + 1)
            return self._create_board_helper(new_board, rows + 2, columns + 2, max_num, new_center)

    # TODO: this is a pretty dumb way of handling spaces
    def __str__(self):
        board_representation = ""
        board_representation += "Center is located at: " + str(self.center) + "\n"
        board_representation += "Size is: " + str(len(self.board)) + "x" + str(len(self.board)) + "\n\n"

        for i in range(len(self.board)):
            for j in range((len(self.board))):
                if self.board[i][j] >= 100000:
                    board_representation += str(self.board[i][j]) + " "
                elif self.board[i][j] >= 10000:
                    board_representation += str(self.board[i][j]) + "  "
                elif self.board[i][j] >= 1000:
                    board_representation += str(self.board[i][j]) + "   "
                elif self.board[i][j] >= 100:
                    board_representation += str(self.board[i][j]) + "    "
                elif self.board[i][j] >= 10:
                    board_representation += str(self.board[i][j]) + "     "
                else:
                    board_representation += str(self.board[i][j]) + "      "
            board_representation += "\n"

        return board_representation
