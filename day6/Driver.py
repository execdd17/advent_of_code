from RepetitionCodeCorrector import RepetitionCodeCorrector
from ModifiedRepetitionCodeCorrector import ModifiedRepetitionCodeCorrector

def main():

    # the correct answer is 185371 for part one
    # the correct answer is 984 for part two
    # file = open('test_input.txt', 'r')    # NOTE: column_length should be set to 6
    file = open('puzzle_input.txt', 'r')    # NOTE: column_length should be set to 8
    lines = file.readlines()

    code_corrector = RepetitionCodeCorrector(lines=lines, column_length=8)
    code_corrector.get_corrected_message()

    code_corrector = ModifiedRepetitionCodeCorrector(lines=lines, column_length=8)
    code_corrector.get_corrected_message()


if __name__ == "__main__":
    main()
