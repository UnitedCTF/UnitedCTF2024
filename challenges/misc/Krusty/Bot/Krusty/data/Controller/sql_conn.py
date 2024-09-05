import os
import sqlite3


class sql_conn:

    def __init__(self, guild_id):
        self.guild_id = guild_id

    def __enter__(self):

        self.conn = sqlite3.connect('./Krusty/data/db/' + str(self.guild_id) + '.db')
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
            raise exc_val
        else:
            self.conn.commit()

        self.cursor.close()
        self.conn.close()
        self.conn = None
        self.cursor = None
