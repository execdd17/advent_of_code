from Room import Room


def main():

    # the correct answer is 185371 for part one
    # the correct answer is 984 for part two
    # file = open('puzzle_input.txt', 'r')
    file = open('puzzle_input.txt', 'r')
    lines = file.readlines()

    sector_id_sum = 0

    for input_line in lines:
        room = Room.from_line(input_line)
        if room.is_real_room():
            sector_id_sum += room.sector_id
            print room.apply_shift_decipher() + " " + str(room.sector_id)

    print sector_id_sum


if __name__ == "__main__":
    main()

