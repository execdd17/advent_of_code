import hashlib


class PasswordCracker(object):
    PASSWORD_DELIMITER = "_"

    def __init__(self, door_id):
        self.door_id = door_id
        self.current_index = 0

    def crack_part_1(self):
        matching_md5s = map(lambda x: self._get_next_matching_md5(), [PasswordCracker.PASSWORD_DELIMITER] * 8)
        return map(lambda md5: md5[5], matching_md5s)

    def crack_part_2(self):
        password = [PasswordCracker.PASSWORD_DELIMITER] * 8
        print "Password cracking status is: " + " ".join(password)

        while '_' in "".join(password):
            matching_md5 = self._get_next_matching_md5()
            password_position = matching_md5[5]
            password_value = matching_md5[6]

            if (password_position.isdigit() and 0 <= int(password_position) <= 7 and
                    password[int(password_position)] == PasswordCracker.PASSWORD_DELIMITER):

                password[int(password_position)] = password_value
                print "Password cracking status is: " + " ".join(password)

        return password

    def _get_next_matching_md5(self):
        matching_md5 = None
        not_found = True

        while not_found:
            result = hashlib.md5(
                self.door_id + str(self.current_index)
            ).hexdigest()

            if result.startswith("00000"):
                matching_md5 = result
                not_found = False

            self.current_index += 1

        return matching_md5


if __name__ == '__main__':
    pc = PasswordCracker('ojvtpuvg')
    # print pc.crack_part_1()
    pc.crack_part_2()