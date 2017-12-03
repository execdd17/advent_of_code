class Triangle(object):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Not valid: 624   23  262
    def is_valid(self):
        """
        In a valid triangle, the sum of any two sides must be larger than the remaining side.
        a + b > c; and
        a + c > b; and
        b + c > a;
        :return: True or False
        """
        if self.side1 + self.side2 > self.side3 \
                and self.side1 + self.side3 > self.side2 \
                and self.side2 + self.side3 > self.side1:
            return True

        return False
