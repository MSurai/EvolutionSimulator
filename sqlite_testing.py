import sqlite3


def main():
    db_name = 'database.db'
    sql_commands_file = 'create_tables.sql'

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    commands = read_sql_commands(sql_commands_file)
    for command in commands:
        cur.execute(command)

    cur.close()
    conn.close()


def read_sql_commands(filename):
    f = open(filename)
    sql_file = f.read()
    f.close()

    sql_commands = [command.strip() for command in sql_file.split(';')]

    return sql_commands


if __name__ == "__main__":
    main()
