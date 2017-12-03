class Direction(object):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    # Adjacency Matrix:
    #
    #       L   R
    # N [   W   E   ]
    # S [   E   W   ]
    # E [   N   S   ]
    # W [   S   N   ]
    MATRIX = [
        [WEST,  EAST],
        [EAST,  WEST],
        [NORTH, SOUTH],
        [SOUTH, NORTH]
    ]

    @staticmethod
    def get_new_direction(starting_direction, turn_letter):
        if turn_letter == 'L':
            return Direction(Direction.MATRIX[starting_direction.index_value][0])
        elif turn_letter == 'R':
            return Direction(Direction.MATRIX[starting_direction.index_value][1])
        else:
            raise "What are you talking about?"

    def __init__(self, index_value):
        self.index_value = index_value

    def __str__(self):
        if self.index_value == 0:
            return "North"
        elif self.index_value == 1:
            return "South"
        elif self.index_value == 2:
            return "East"
        elif self.index_value == 3:
            return "West"
