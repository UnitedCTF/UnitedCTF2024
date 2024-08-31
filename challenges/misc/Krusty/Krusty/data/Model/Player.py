from .Balloon import Balloon

class Player():

    balloons: list[Balloon]
    score: int

    def __init__(self, player_id: int, player_name: str, balloons: list[Balloon]):
        self.id = player_id
        self.name = player_name
        self.balloons = balloons

    @property
    def score(self) -> int:
        return sum([ballon.points for ballon in self.balloons])