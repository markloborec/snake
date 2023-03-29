from src.domain.snakepart import SnakePart
class Snake:
    def __init__(self):
        xpozicija = 0.5
        self.delcki:list[SnakePart] = []
        for i in range(3):
            delcek = SnakePart(size=0.1,x=xpozicija,y=0.5)
            self.delcki.append(delcek)
            xpozicija += 0.1

