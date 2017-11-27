class RepetitionCodeColumn(object):
    def __init__(self):
        self.entries = {}

    def add_entry(self, letter):
        if letter in self.entries:
            self.entries[letter] += 1
        else:
            self.entries[letter] = 1

    def get_most_common_letter(self):
        highest_occurrence = self._get_max_num_in_list()
        inverted_dict = self._get_inverted_dictionary()
        return inverted_dict[highest_occurrence]

    def get_least_common_letter(self):
        lowest_occurrence = self._get_min_num_in_list()
        inverted_dict = self._get_inverted_dictionary()
        return inverted_dict[lowest_occurrence]

    def _get_inverted_dictionary(self):
        inverted_dict = {}
        for k, v in self.entries.iteritems():
            inverted_dict[v] = k
        return inverted_dict

    def _get_max_num_in_list(self):
        max = 0

        for number in self.entries.values():
            if number > max:
                max = number

        return max

    def _get_min_num_in_list(self):
        min = 9999999   # some arbitrarily big number

        for number in self.entries.values():
            if number < min:
                min = number

        return min
