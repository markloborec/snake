from src.domain.snakepart import SnakePart
class Snake:
    def __init__(self):
        self.glava = SnakePart(size=0.05,x=0.5,y=0.5)
        self.smer:str = "leva"
        x = 0.5
        self.delcki:list[SnakePart] = []
        for i in range(3):
            delcek = SnakePart(size=0.1,x=x,y=0.5)
            self.delcki.append(delcek)
            x += 0.1

    def premakni(self):
        if self.smer == "leva":
            self.glava.x -= 0.01
        elif self.smer == "desna":
            self.glava.x += 0.01
        elif self.smer == "gor":
            self.glava.y -= 0.01
        elif self.smer == "dol":
            self.glava.y += 0.01






