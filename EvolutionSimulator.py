import math
import random


# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MIN_NODE_COUNT = 3
MAX_NODE_COUNT = 5


class Node:
    """
    Nodes are part of a creature, in which they are connected by muscles.
    They collide with the floor, but not with other nodes.

    =================== ===================
    property            description
    =================== ===================
    x                   position on x-axis
    y                   position on y-axis
    friction            determines the friction with the ground
    =================== ===================
    """
    def __init__(self, x, y, friction):
        pass


class Muscle:
    """
    Muscles are part of a creature, in which they connect nodes.
    They don't collide with anything.

    =================== ===================
    property            description
    =================== ===================
    extended_time       between 0 and 2*pi (when internal_clock of creature reaches extended_time, muscle extends)
    contracted_time     between 0 and 2*pi (when internal_clock of creature reaches contracted_time, muscle contracts)
    extended_length
    contracted_length
    strength            determines how strong (fast) the two connected nodes are pulled towards each other
    =================== ===================
    """
    def __init__(self, extended_time, contracted_time, extended_length, contracted_length, strength):
        pass


class Creature:
    """
    A creature consists of:

    - internal clock (loops from 0 to some 2*pi)
    - nodes (see class: :class:`Node`)
    - muscles (see class: :class:`Muscle`)
    """
    def __init__(self):
        """Create all parts (and properties?) of creature."""
        self.nodes = []
        self.muscles = []
        self.internal_clock = 0

    def create_random(self):
        # node_count between min and max
        node_count = random.randint(MIN_NODE_COUNT, MAX_NODE_COUNT)
        # every node must be connected with at least on other node
        muscle_count = random.randint(node_count, nCr(node_count, 2))

        # TODO: actually create random nodes and muscles
        for i in range(node_count):
            node = Node()
            self.nodes.append(node)

        for i in range(muscle_count):
            muscle = Muscle()
            self.muscles.append(muscle)


def nCr(n, r):
    """
    Calculate the binomial coefficient (n choose r).
        n! / (r! * (n-r)!)
    """
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def main():
    pass


if __name__ == '__main__':
    main()
