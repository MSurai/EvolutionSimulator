import math
import random


# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


SEED = 11

GRAVITY = 0.9
AIR_FRICTION = 0.1

MIN_NODE_COUNT = 3
MAX_NODE_COUNT = 5

NODE_RADIUS = 5

MIN_NODE_FRICTION = 0
MAX_NODE_FRICTION = 1

MIN_MUSCLE_LENGTH = 5
MAX_MUSCLE_LENGTH = 10


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
    # TODO: rework values (extended and contracted time could 0 - 360° or 0 - 100%) in docstring and random_init
    """
    **Description:**
        Muscles are part of a creature, in which they connect nodes.
        If the internal_clock of the creature the muscle belongs to
        reaches the contracted_time of the muscle, the muscle
        contracts/pulls to contracted_length. Same goes for
        extended_time and extended_length.
        The muscle pushes/pulls with his strength.
        Muscles don't collide with anything.

    _____

    **Properties:**
        extended_time
            angle between 0 and 2*pi (when internal_clock of creature
            reaches extended_time, muscle extends)
        contracted_time
            angle between 0 and 2*pi (when internal_clock of creature
            reaches contracted_time, muscle contracts)
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
        times = random.sample(range(0, 360), 2)
        times = [math.sin(x) for x in times]
        extended_time, contracted_time = min(times), max(times)

        lengths = random.sample(range(MAX_MUSCLE_LENGTH, MAX_MUSCLE_LENGTH+1), 2)
        contracted_length, extended_length = min(lengths), max(lengths)

        strength = random.random()

        return cls(extended_time, contracted_time, extended_length, contracted_length, strength)


class Creature:
    # TODO: add description
    """
    **Description:**
        A creature ...

    _____

    **Properties:**
        nodes
            see class: :class:`Node`
        muscles
            see class: :class:`Muscle`
        internal_clock
            (angle) loops from 0 to some 2*pi
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


def main():
    random.seed(SEED)

    creature = Creature.random_init()
    print(creature.nodes)
    print(creature.nodes[0].x)


if __name__ == '__main__':
    main()
