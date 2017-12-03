import math
from Direction import Direction

class Actor:
    start_x = 0
    start_y = 0
    curr_x = 0
    curr_y = 0

    def __init__(self, starting_direction):
        self.current_direction = starting_direction

    def move(self, amount, turn_letter):
        prev_direction = self.current_direction
        prev_x = self.curr_x
        prev_y = self.curr_y

        self.current_direction = Direction.get_new_direction(self.current_direction, turn_letter)

        if self.current_direction.index_value == Direction.NORTH:
            self.curr_y += amount
        elif self.current_direction.index_value == Direction.SOUTH:
            self.curr_y -= amount
        elif self.current_direction.index_value == Direction.EAST:
            self.curr_x += amount
        elif self.current_direction.index_value == Direction.WEST:
            self.curr_x -= amount
        else:
            raise "Oh boy..."

        print "[" + str(prev_direction) + "] + [" + str(amount) + str(turn_letter) + "] = " + str(self.current_direction)
        print "(" + str(prev_x) + "," + str(prev_y) + ") -> (" + str(actor.curr_x) + "," + str(actor.curr_y) + ")"
        print

    def get_distance_traveled(self):
        return abs(self.curr_x) + abs(self.curr_y)


if __name__ == '__main__':
    input = "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3"

    # 253 is answer
    chris_input = "L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5"
    input = "R8, R4 , R4, R8"
  #   input = "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5"
  #   input = "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4"
  #   input = "R5, L5, R5, R3"
    actor = Actor(starting_direction=Direction(Direction.NORTH))
    vectors = input.replace(" ", "").split(",")

    for vector in vectors:
        actor.move(amount=int(vector[1]), turn_letter=vector[0])
    print actor.get_distance_traveled()
