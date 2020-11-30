import random


class Population(object):

    def __init__(self, size):
        self.genes = [0] * size

    class DNA(object):

        def __init__(self):
            self

        def crossover(self, partner):
            mid = random.randrange(0, partner.genes)
