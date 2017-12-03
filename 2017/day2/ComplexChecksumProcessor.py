class ComplexChecksumProcessor(object):
    def __init__(self):
        self.sum = 0
        self.entries = []

    def add_row_entry(self, num):
        self.entries.append(num)

    def conclude_row(self):
        for i in range(len(self.entries)):
            for j in range(len(self.entries)):
                if i != j and self.entries[i] % self.entries[j] == 0:
                    self.sum += self.entries[i] / self.entries[j]
        self.entries = []

    def provide_checksum(self):
        return self.sum
