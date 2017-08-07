import math
import random
import sqlite3


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
        # TODO: update generation of random x and y position (?)
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
        self.nodes = []
        self.muscles = []
        self.alive = True

    @classmethod
    def random_init(cls):
        pass

    def insert_into_db(self, db_name):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        insert_creature = """
            INSERT INTO creatures
                (alive)
            VALUES
                (1);
        """

        get_creature_id = """
            SELECT creature_id FROM creatures
            ORDER BY creature_id DESC
            LIMIT 1;
        """

        insert_nodes = """
            INSERT INTO nodes
                (x_position, y_position, friction, creature_id)
            VALUES
                (?, ?, ?, ?);
        """

        insert_muscles = """
            INSERT INTO nodes
                (extended_length, contracted_length, extended_time, contracted_time, strength,
                node_1_id, node_2_id, creature_id)
            VALUES
                (?, ?, ?, ?, ?,
                ?, ?, ?);
        """

        cur.execute(insert_creature)
        creature_id = cur.execute(get_creature_id)
        for node in self.nodes:
            cur.execute(insert_nodes, node.x_pos, node.y_pos, node.friction, creature_id)
        # TODO: find better way?
        for muscle in self.muscles:
            cur.execute(insert_muscles, muscle.extended_length, muscle.contracted_length, \
                muscle.extended_time, muscle.contracted_time, muscle.strength, \
                node_1_id, node_2_id, creature_id)

        cur.close()
        conn.close()


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def main():
    pass


if __name__ == '__main__':
    main()
