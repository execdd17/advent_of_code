def part1(input_line):
    prev = None
    sum = 0

    for i in input_line:
        if prev is None:
            prev = i
            continue

        if prev == i:
            sum += int(i)
        prev = i

    if input_line[len(input_line) - 1] == input_line[0]:
        sum += int(input_line[0])

    return sum


def part2(input_line):
    sum = 0
    look_ahead_amount = len(input_line) / 2
    current_index = 0

    for i in map(lambda num: int(num), input_line):
        if current_index + look_ahead_amount > len(input_line) - 1:
            target_index = (current_index + look_ahead_amount) % len(input_line)
            if input_line[target_index] == str(i):
                sum += i
        else:
            if str(i) == input_line[current_index + look_ahead_amount]:
                sum += i
        current_index += 1

    return sum


def main(input_line):
    print part1(input_line)
    print part2(input_line)


if __name__ == "__main__":
    file = open('puzzle_input.txt', 'r')  # NOTE: column_length should be set to 8
    lines = file.readlines()

    if len(lines) != 1:
        raise "Not what I expected"

    main(lines[0])
