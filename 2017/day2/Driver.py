from ChecksumProcessor import ChecksumProcessor
from ComplexChecksumProcessor import ComplexChecksumProcessor

def main():
    cp = ChecksumProcessor()
    ccp = ComplexChecksumProcessor()

    file = open('puzzle_input.txt', 'r')  # NOTE: column_length should be set to 8
    # file = open('test_input_2.txt', 'r')  # NOTE: column_length should be set to 8
    lines = file.readlines()

    for line in lines:
        nums = map(lambda num: int(num), line.split())
        for num in nums:
            cp.add_row_entry(num)
            ccp.add_row_entry(num)
        cp.conclude_row()
        ccp.conclude_row()

    print cp.provide_checksum()
    print ccp.provide_checksum()


if __name__ == "__main__":
    main()
