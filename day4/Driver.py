import sys

from Room import Room


def usage():
    print "Expected either a '1' or '2' for part one or two, respectively"


def convert_line_to_num_list(input_line):
        sides = input_line.strip().split(" ")
        intermediate_sides = list(filter(lambda x: x != '', sides))
        return list(map(lambda x: int(x), intermediate_sides))


def main():
    if len(sys.argv) != 2:
        usage()

    # the correct answer is 185371 for part one
    # the correct answer is ????? for part two
    # file = open('puzzle_input.txt', 'r')
    file = open('puzzle_input.txt', 'r')
    lines = file.readlines()

    if sys.argv[1] == '1':
        sector_id_sum = 0

        for input_line in lines:
            room = Room.from_line(input_line)
            if room.is_real_room():
                sector_id_sum += room.sector_id
    elif sys.argv[1] == '2':
        for input_line in lines:
            None
    else:
        usage()

    print sector_id_sum


if __name__ == "__main__":
    main()

