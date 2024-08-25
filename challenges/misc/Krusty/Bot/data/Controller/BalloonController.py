from sql_conn import sql_conn
class BalloonController:

    def __init__(self, guild_id):
        self.guild_id = guild_id

    def get_player_balloons(self, player_id, password):
        with sql_conn(self.guild_id) as cursor:
            cursor.execute('SELECT * FROM balloons WHERE player_id=' + str(player_id) +)



