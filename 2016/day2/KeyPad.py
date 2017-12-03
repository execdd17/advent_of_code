from transitions import Machine


class KeyPad(object):
    """
    #########
    # 1 2 3 #
    # 4 5 6 #
    # 7 8 9 #
    #########

    taken from: http://adventofcode.com/2016/day/2
    """

    states = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        states_as_strings = map(lambda x: str(x), KeyPad.states)
        self.machine = Machine(model=self, states=states_as_strings, initial='5')

    def add_all_transitions(self):
        for digit in KeyPad.states:
            self.__add_transition_for_digit__(digit)

    def __add_transition_for_digit__(self, digit):

        # we can't go up any more than we are
        if digit - 3 <= 0:
            self.machine.add_transition(trigger='push_up', source=str(digit), dest=str(digit))
        else:
            self.machine.add_transition(trigger='push_up', source=str(digit), dest=str(digit - 3))

        # we can't go down any more than we are
        if digit + 3 > 9:
            self.machine.add_transition(trigger='push_down', source=str(digit), dest=str(digit))
        else:
            self.machine.add_transition(trigger='push_down', source=str(digit), dest=str(digit + 3))

        # we can't go left any more than we are
        if digit == 1 or digit == 4 or digit == 7:
            self.machine.add_transition(trigger='push_left', source=str(digit), dest=str(digit))
        else:
            self.machine.add_transition(trigger='push_left', source=str(digit), dest=str(digit - 1))

        # we can't go right any more than we are
        if digit == 3 or digit == 6 or digit == 9:
            self.machine.add_transition(trigger='push_right', source=str(digit), dest=str(digit))
        else:
            self.machine.add_transition(trigger='push_right', source=str(digit), dest=str(digit + 1))

