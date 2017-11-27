from RepetitionCodeCorrector import RepetitionCodeCorrector


class ModifiedRepetitionCodeCorrector(RepetitionCodeCorrector):
    def get_corrected_message(self):
        message = ""
        for code_column in self.code_columns:
            message += code_column.get_least_common_letter()

        print message