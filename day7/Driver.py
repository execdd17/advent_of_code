from TinyLCD import TinyLCD


def main():

    # the correct answer is 185371 for part one
    # the correct answer is 984 for part two
    file = open('puzzle_input.txt', 'r')  # NOTE: column_length should be set to 8
    lines = file.readlines()

    # tiny_lcd = TinyLCD(rows=3, columns=7)
    # tiny_lcd.activate_region(width=3, height=2)
    # print(tiny_lcd)
    # tiny_lcd.rotate_column(column_index=1, amount=1)
    # print(tiny_lcd)
    # tiny_lcd.rotate_row(row_index=0, amount=4)
    # print(tiny_lcd)
    # tiny_lcd.rotate_column(column_index=1, amount=1)
    # print(tiny_lcd)

    tiny_lcd = TinyLCD(rows=6, columns=50)

    for line in lines:
        line = line.strip()
        tokens = line.split(" ")

        if tokens[0] == 'rect':
            width, height = tokens[1].split("x")
            tiny_lcd.activate_region(width=int(width), height=int(height))
            print(tiny_lcd)
        elif tokens[0] + " " + tokens[1] == "rotate row":
            row_index = tokens[2].split("=")[1]
            amount = tokens[-1]
            tiny_lcd.rotate_row(row_index=int(row_index), amount=int(amount))
            print(tiny_lcd)
        elif tokens[0] + " " + tokens[1] == "rotate column":
            column_index = tokens[2].split("=")[1]
            amount = tokens[-1]
            tiny_lcd.rotate_row(row_index=int(column_index), amount=int(amount))
            print(tiny_lcd)

    # file = open('puzzle_input.txt', 'r')


if __name__ == "__main__":
    main()
