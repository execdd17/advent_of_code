from KeyPad import KeyPad

if __name__ == "__main__":
    keypad = KeyPad()
    keypad.add_all_transitions()

    # the correct answer is 78985
    file = open('day2_input.txt', 'r')

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

        print keypad.state