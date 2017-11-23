import sys
from Triangle import Triangle


def usage():
    print "Expected either a '1' or '2' for part one or two, respectively"


def convert_line_to_num_list(input_line):
        sides = input_line.strip().split(" ")
        intermediate_sides = list(filter(lambda x: x != '', sides))
        return list(map(lambda x: int(x), intermediate_sides))


def main():
    if len(sys.argv) != 2:
        usage()

    # the correct answer is 862 for part one
    # the correct answer is 1577 for part two
    # file = open('puzzle_input.txt', 'r')
    file = open('puzzle_input.txt', 'r')
    lines = file.readlines()
    total_valid = 0

    if sys.argv[1] == '1':
        for input_line in lines:
            side1, side2, side3 = convert_line_to_num_list(input_line)
            triangle = Triangle(side1, side2, side3)

            if triangle.is_valid():
                total_valid += 1
    elif sys.argv[1] == '2':
        matrix = [[0 for j in range(3)] for i in range(len(lines))]
        line_number_index = 0

        for input_line in lines:
            matrix[line_number_index] = convert_line_to_num_list(input_line)
            line_number_index += 1

        for j in range(3):                      # num columns
            for i in range(0, len(lines), 3):   # num rows; increment by 2
                triangle = Triangle(side1=matrix[i][j], side2=matrix[i+1][j], side3=matrix[i+2][j])

                if triangle.is_valid():
                    total_valid += 1
    else:
        usage()

    print total_valid


if __name__ == "__main__":
    main()

