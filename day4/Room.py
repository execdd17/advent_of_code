import re


class Room(object):

    @staticmethod
    def from_line(line):
        regexp = r"-\d+"
        match_object = re.search(regexp, line)

        if match_object:
            name = line[:match_object.start()]
            sector_id = line[match_object.start() + 1: match_object.end()]
            checksum = line.strip()[match_object.end() + 1:-1]
            return Room(name=name, sector_id=int(sector_id), checksum=checksum)
        else:
            raise "Unexpected line encountered!"

    @staticmethod
    def _get_counts_dict(dict):
        """
        :param dict: A dictionary containing a letter mapped to how many occurrences in a room name
        :return: A new dictionary containing the number of occurrences of a letter,
        mapped to the matching list of letters with that amount
        """
        new_dict = {}

        for letter, count in dict.iteritems():
            if count in new_dict:
                new_dict[count].append(letter)
            else:
                new_dict[count] = [letter]

        for count, letter in new_dict.iteritems():
            if len(letter) > 0:
                ascii_list = map(lambda l: ord(l), letter)
                sorted_letters = map(lambda number: chr(number), sorted(ascii_list, key=int))
                new_dict[count] = sorted_letters

        return new_dict

    def __init__(self, name, sector_id, checksum):
        self.name = name
        self.sector_id = sector_id
        self.checksum = checksum
        self.letter_counts = {}

    def is_real_room(self):
        """
        A real room's checksum matches the algorithm described in the challenge
        :return: True or False
        """
        return self._calculate_checksum() == self.checksum

    def apply_shift_decipher(self):
        """
        Shifts each alphabetic character by the room's checksum, wrapping when necessary.
        Dashes are replaced with spaces
        :return: The decrypted name
        """
        return self._shift_helper("", self.name)

    def _shift_helper(self, decrypted, encrypted):
        if len(encrypted) == 0:
            return decrypted

        current_letter = encrypted[0]

        if current_letter == "-":
            decrypted += " "
        else:
            offset = self.sector_id % 26                        # 26 letters in the alphabet
            shifted_letter = ord(current_letter) + offset

            if shifted_letter > 122:                            # 122 is 'z'
                decrypted += chr(96 + (shifted_letter - 122))   # 97 is 'a'
            else:
                decrypted += chr(ord(current_letter) + offset)

        return self._shift_helper(decrypted, encrypted[1:])

    def _calculate_checksum(self):

        for letter in self.name.replace("-", ""):
            if letter in self.letter_counts:
                self.letter_counts[letter] += 1
            else:
                self.letter_counts[letter] = 1

        count_to_letter_list = self._get_counts_dict(self.letter_counts)
        checksum = ""
        for count in sorted(count_to_letter_list.keys(), key=int, reverse=True):
            checksum += "".join(count_to_letter_list[count])
        return checksum[:5]
