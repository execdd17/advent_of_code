from TinyLCD import TinyLCD


def main():

    file = open('puzzle_input.txt', 'r')  # NOTE: column_length should be set to 8
    lines = file.readlines()
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
            tiny_lcd.rotate_column(column_index=int(column_index), amount=int(amount))
            print(tiny_lcd)

    print("Total activated is " + str(tiny_lcd.get_total_activated()))


if __name__ == "__main__":
    main()
