CREATE TABLE IF NOT EXISTS creatures (
    creature_id INTEGER PRIMARY KEY,
    alive INTEGER NOT NULL,
    distance REAL DEFAULT 0 NOT NULL
);

CREATE TABLE IF NOT EXISTS nodes (
    node_id INTEGER PRIMARY KEY,
    x_start_pos INTEGER NOT NULL,
    y_start_pos INTEGER NOT NULL,
    friction REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS muscles (
    muscle_id INTEGER PRIMARY KEY,
    extended_length REAL NOT NULL,
    contracted_length REAL NOT NULL,
    extended_time INTEGER NOT NULL,
    contracted_time INTEGER NOT NULL,
    strength REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS creature_muscle_connections (
    creature_id INTEGER,
    muscle_id INTEGER,

    PRIMARY KEY (creature_id, muscle_id),
    FOREIGN KEY (creature_id) REFERENCES creatures(creature_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (muscle_id) REFERENCES muscles(muscle_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS muscle_node_connections (
    muscle_id INTEGER,
    node_1_id INTEGER,
    node_2_id INTEGER,

    PRIMARY KEY (muscle_id, node_1_id, node_2_id),
    FOREIGN KEY (muscle_id) REFERENCES muscles(muscle_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (node_1_id) REFERENCES nodes(node_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
    FOREIGN KEY (node_2_id) REFERENCES nodes(node_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);