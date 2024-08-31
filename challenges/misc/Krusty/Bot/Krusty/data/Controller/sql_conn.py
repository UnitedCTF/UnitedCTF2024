import os
import sqlite3


class sql_conn():

    def __init__(self, guild_id):
        self.guild_id = guild_id
        sqlite3.enable_callback_tracebacks(True)
        try:
            file = open('./Krusty/data/db/' + str(self.guild_id) + '.db', 'x')
            file.close()
            self.conn = sqlite3.connect('./Krusty/data/db/' + str(self.guild_id) + '.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('CREATE TABLE IF NOT EXISTS players ('
                                'id INTEGER PRIMARY KEY, '
                                'name TEXT'
                                ')')
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS balloons ('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'emoji CHAR(1), '
                'points INTEGER, '
                'description TEXT,'
                'possessed_by INTEGER, '
                'FOREIGN KEY (possessed_by) REFERENCES players(id) '
                ')')

            self.cursor.execute(
                "INSERT INTO players (id, name) VALUES (1267654171843231794, 'Krusty')"
            )
            self.cursor.execute(
                "INSERT INTO balloons (emoji, points, possessed_by, description) VALUES ('🚩', 10, 1267654171843231794, ?)",
                (os.getenv("KRUSTYS_BALLOON"),)
            )
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            self.conn = None
            self.cursor = None
        except FileExistsError:
            pass


    def __enter__(self):
        self.conn = sqlite3.connect('./Krusty/data/db/' + str(self.guild_id) + '.db')
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()

        self.cursor.close()
        self.conn.close()
        self.conn = None
        self.cursor = None
