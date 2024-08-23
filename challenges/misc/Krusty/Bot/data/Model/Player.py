from Balloon import Balloon

class Player():

    balloons: list[Balloon]
    score: int


    @property
    def score(self) -> int:
        return sum([ballon.points for ballon in self.balloons])