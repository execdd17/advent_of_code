from NoRepeatsPassphraseChecker import NoRepeatsPassphrseChecker
from AnagramPassphraseChecker import AnagramPassphraseChecker


def main():

    # file = open('test_input_2.txt', 'r')
    file = open('puzzle_input.txt', 'r')
    lines = file.readlines()

    # passphrase_checker = NoRepeatsPassphrseChecker
    passphrase_checker = AnagramPassphraseChecker
    total_valid = 0
    
    for line in lines:
        if passphrase_checker.is_valid(line):
            total_valid += 1

    print total_valid


if __name__ == "__main__":
    main()
