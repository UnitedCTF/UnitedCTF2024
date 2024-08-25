import sqlite3


class sql_conn():

    def __init__(self, guild_id):
        self.guild_id = guild_id



    def __enter__(self):
        try:
            file = open('./data/db/' + self.guild_id + '.db', 'x')
            file.close()

        except FileExistsError:
            pass
        self.conn = sqlite3.connect('./data/db/' + self.guild_id + '.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, name TEXT, password TEXT)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS balloons (id INTEGER PRIMARY KEY, emoji INTEGER, points INTEGER, possesed_by INTEGER FOREIGN KEY REFERENCES players(id) )')
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        self.cursor.close()
        self.conn = None
        self.cursor = None
