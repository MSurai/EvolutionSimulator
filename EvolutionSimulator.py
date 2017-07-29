import math
import random


# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SEED = 11

MIN_NODE_COUNT = 3
MAX_NODE_COUNT = 5


class Node:
    """
    **Description:**
        Nodes are part of a creature, in which they are connected by muscles.
        They collide with the floor, but not with other nodes.

    _____

    **Properties:**
        x
            position on x-axis
        y
            position on y-axis
        friction
            determines the friction with the ground
    """
    def __init__(self, x, y, friction):
        self.x = x
        self.y = y
        self.friction = friction

    @classmethod
    def random_init(cls):
        # TODO: actually set random values
        x = None
        y = None
        friction = None

        return cls(x, y, friction)


class Muscle:
    """
    **Description:**
        Muscles are part of a creature, in which they connect nodes.
        If the internal_clock of the creature reaches the contracted_time
        of the muscle, the muscle contracts/pulls to contracted_length.
        If the internal_clock of the creature reaches the extended_time
        of the muscle, the muscle extends/pushes to extended_length.
        The muscle pushes/pulls with his strength.
        They don't collide with anything.

    _____

    **Properties:**
        extended_time
            between 0 and 2*pi (when internal_clock of creature reaches extended_time, muscle extends)
        contracted_time
            between 0 and 2*pi (when internal_clock of creature reaches contracted_time, muscle contracts)
        extended_length
            .
        contracted_length
            .
        strength
            determines how strong (fast?) the two connected nodes are pulled towards each other
    """
    def __init__(self, extended_time, contracted_time, extended_length, contracted_length, strength):
        self.extended_time = extended_time
        self.contracted_time = contracted_time
        self.extended_length = extended_length
        self.contracted_length = contracted_length
        self.strength = strength

    @classmethod
    def random_init(cls):
        # TODO: actually set random values
        extended_time = None
        contracted_time = None
        extended_length = None
        contracted_length = None
        strength = None

        return cls(extended_time, contracted_time, extended_length, contracted_length, strength)


class Creature:
    """
    **Description:**
        A creature ...

    _____

    **Properties:**
        nodes
            see class: :class:`Node`
        muscles
            see class: :class:`Muscle`
        internal clock
            loops from 0 to some 2*pi
    """
    def __init__(self, nodes, muscles):
        self.nodes = nodes
        self.muscles = muscles
        self.internal_clock = 0

    @classmethod
    def random_init(cls):
        """Acts as an overloaded constructor for random initialization of all properties."""
        nodes = []
        muscles = []

        node_count = random.randint(MIN_NODE_COUNT, MAX_NODE_COUNT)
        muscle_count = random.randint(node_count, nCr(node_count, 2))

        for i in range(node_count):
            node = Node.random_init()
            nodes.append(node)

        for i in range(muscle_count):
            muscle = Muscle.random_init()
            muscles.append(muscle)

        return cls(nodes, muscles)


def nCr(n, r):
    """
    Calculate the binomial coefficient (n choose r).
        n! / (r! * (n-r)!)
    """
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def float_range(start=0.0, stop=1.0, step=1.0):
    """
    Implementation of range(start, stop, step) as a generator that accepts floats as parameters.

    **Disclaimer: comes with float rounding errors!**
    """
    i = 0
    current_val = start
    while current_val < stop:
        yield current_val
        i += 1
        current_val = start + i * step


def main():
    random.seed(SEED)

    creature = Creature.random_init()
    print(creature.nodes)
    print(creature.nodes[0].x)


if __name__ == '__main__':
    main()
