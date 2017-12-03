from RepetitionCodeColumn import RepetitionCodeColumn


class RepetitionCodeCorrector(object):
    def __init__(self, lines, column_length):
        self.lines = map(lambda line: line.strip(), lines)
        self.code_columns = [RepetitionCodeColumn() for count in xrange(column_length)]

        for line in self.lines:
            for i in range(len(line)):
                self.code_columns[i].add_entry(line[i])

    def get_corrected_message(self):
        message = ""
        for code_column in self.code_columns:
            message += code_column.get_most_common_letter()

        print message
