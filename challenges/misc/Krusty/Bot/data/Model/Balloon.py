class Balloon():
    color: str
    emoji_id: int
    points: int
    password: str | None

    def __init__(self, color: str, emoji_id: int, points: int, password: str | None):
        self.color = color
        self.emoji_id = emoji_id
        self.points = points
        self.password = password


