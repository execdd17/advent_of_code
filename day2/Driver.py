from KeyPad import KeyPad
from ComplexKeyPad import ComplexKeyPad
import sys


def usage():
    print "Expected either a '1' or '2' for part one or two, respectively"


def compute_password(keypad, file, get_key):
    password = []

    for input_line in file.readlines():
        for direction in input_line:
            if direction == 'U':
                keypad.push_up()
            elif direction == 'D':
                keypad.push_down()
            elif direction == 'L':
                keypad.push_left()
            elif direction == 'R':
                keypad.push_right()
        password.append(get_key())

    print password


def main():
    if len(sys.argv) != 2:
        usage()

    # the correct answer is 78985 for part one
    # the correct answer is 57DD8 for part two
    file = open('puzzle_input.txt', 'r')

    if sys.argv[1] == '1':
        keypad = KeyPad()
        keypad.add_all_transitions()
        compute_password(keypad, file, lambda: keypad.state)
    elif sys.argv[1] == '2':
        keypad = ComplexKeyPad()
        compute_password(keypad, file, lambda: keypad.current_cell.key)
    else:
        usage()


if __name__ == "__main__":
    main()

