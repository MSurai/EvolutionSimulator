import sqlite3
import random

def main():
    db_name = 'database.db'

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    commands = read_sql_commands('create_tables.sql')
    for command in commands:
        cur.execute(command)


    # TODO: remove this later
    # generate a few random nodes (testing only)
    nodes = []
    for _ in range(5):
        x_start_pos = random.randint(-5, 5)
        y_start_pos = random.randint(-5, 5)
        friction = random.random()
        nodes.append((x_start_pos, y_start_pos, friction))
    
    command = read_sql_commands('insert_into_nodes.sql')
    cur.executemany(command[0], nodes)
    conn.commit()

    cur.close()
    conn.close()


def read_sql_commands(filename):
    f = open(filename)
    sql_file = f.read()
    f.close()

    sql_commands = [command.strip() for command in sql_file.split(';')]
    # because of ';' at end of file last command is empty string -> remove it
    sql_commands = sql_commands[:-1]

    return sql_commands


if __name__ == "__main__":
    main()
