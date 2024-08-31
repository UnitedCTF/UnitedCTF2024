from .sql_conn import sql_conn
from Krusty.errors import DataModelErrors as dataErrors
from .BalloonController import BalloonController
from ..Model.Player import Player


class PlayerController():

    def __init__(self, guild_id):
        self.guild_id = guild_id
        self.sql_conn = sql_conn(guild_id)

    def get_player(self, player_id, player_name):
        with self.sql_conn as cursor:
            data = cursor.execute('SELECT * FROM players WHERE id = ?;', (player_id,))
            player = data.fetchone()
        if not player:
            raise dataErrors.NotFoundError('Player ' + str(player_id))
        else:
            balloon_controller = BalloonController(self.guild_id)
            balloons = balloon_controller.get_player_balloons(player_name)
            return Player(player[0], player[1], balloons)

    def create_player(self, player_id, player_name):
        with self.sql_conn as cursor:
            data = cursor.execute('SELECT * FROM players WHERE id = ?;', (player_id,))
            player = data.fetchone()
            if player:
                raise dataErrors.AlreadyExistsError('Player ' + str(player_id))
            else:
                cursor.execute('INSERT INTO players (id, name) VALUES (?, ?);', (player_id, player_name))
                return cursor.lastrowid

    def give_balloon(self, player_id, emoji, points, description):
        balloon_controller = BalloonController(self.guild_id)
        balloon_controller.give_balloon(player_id, emoji, points, description)