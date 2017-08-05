import math
import random


# CONSTANTS
NODE_POS_OFFSET_AT_CREATION = 10

MIN_NODE_FRICTION = 0
MAX_NODE_FRICTION = 1


class Node:
    def __init__(self, x_pos, y_pos, friction, speed, angle):
        # position in space
        self.x_pos = x_pos
        self.y_pos = y_pos
        # friction with the ground
        self.friction = friction
        # speed vector (better than vX and vY?)
        self.speed = speed
        self.angle = angle

    @classmethod
    def from_random(cls):
        # TODO: update generation of random x and y position
        x_pos = random.randint(-1 * NODE_POS_OFFSET_AT_CREATION, NODE_POS_OFFSET_AT_CREATION)
        y_pos = random.randint(-1 * NODE_POS_OFFSET_AT_CREATION, NODE_POS_OFFSET_AT_CREATION)
        friction = random.uniform(MIN_NODE_FRICTION, MAX_NODE_FRICTION)
        # node doesnt have any speed at creation
        speed = 0
        angle = 0

        return cls(x_pos, y_pos, friction, speed, angle)


class Muscle:
    def __init__(self):
        pass

    @classmethod
    def random_init(cls):
        pass


class Creature:
    def __init__(self):
        pass

    @classmethod
    def random_init(cls):
        pass


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def main():
    pass


if __name__ == '__main__':
    main()
