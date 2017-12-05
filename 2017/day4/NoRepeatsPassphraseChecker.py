class NoRepeatsPassphrseChecker:

    @staticmethod
    def is_valid(passphrase):
        unique_tokens = []
        tokens = passphrase.split()

        for token in tokens:
            if token in unique_tokens:
                return False
            else:
                unique_tokens.append(token)

        return True

