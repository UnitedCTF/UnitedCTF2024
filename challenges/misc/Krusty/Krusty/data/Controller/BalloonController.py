from .sql_conn import sql_conn
from ..Model.Balloon import Balloon


class BalloonController():

    def __init__(self, guild_id):
        self.guild_id = guild_id

    def get_player_balloons(self, player_name):
        with sql_conn(self.guild_id) as cursor:
            data = cursor.execute(
                'SELECT balloons.emoji, balloons.points, balloons.description FROM balloons JOIN players ON balloons.possessed_by = players.id WHERE players.name = ?;', (player_name,))
            balloons_data = data.fetchall()
        balloons_obj = []
        for balloon in balloons_data:
            balloons_obj.append(Balloon(balloon[0], balloon[1], balloon[2]))
        return balloons_obj

    def give_balloon(self, player_id, emoji, points, description):
        with sql_conn(self.guild_id) as cursor:
            cursor.execute(
                'INSERT INTO balloons (emoji, points, possessed_by, description) VALUES (?, ?, ?, ?);', (emoji, points, player_id, description))


