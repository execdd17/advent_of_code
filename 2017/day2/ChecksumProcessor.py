class ChecksumProcessor(object):
    def __init__(self):
        self.sum = 0
        self.initialize_counters()

    def initialize_counters(self):
        self.highest = 0
        self.lowest = 999999999

    def add_row_entry(self, num):
        if num > self.highest:
            self.highest = num

        if num < self.lowest:
            self.lowest = num

    def conclude_row(self):
        self.sum += self.highest - self.lowest
        self.initialize_counters()

    def provide_checksum(self):
        return self.sum
