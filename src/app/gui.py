from src.domain.svet import Svet


class Gui:
    def __init__(self, sirina: int, visina: int):
        self.svet: Svet = Svet()
        self.sirina: int = sirina
        self.visina: int = visina

    def narisi(self):
        print("Narisi")

    def vnos(self):
        print("Vnos")

    def konec(self):
        print("Konec")
