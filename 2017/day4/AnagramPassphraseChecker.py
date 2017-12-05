class AnagramPassphraseChecker:

    @staticmethod
    def is_valid(passphrase):
        unique_tokens = []
        tokens = passphrase.split()

        for token in tokens:
            sorted_token = "".join(sorted(token))

            if sorted_token in unique_tokens:
                return False
            else:
                unique_tokens.append(sorted_token)

        return True

