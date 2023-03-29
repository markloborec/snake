import pygame

from src.domain.svet import Svet



class Gui:
    def __init__(self, sirina: int, visina: int):
        self.svet: Svet = Svet()
        self.sirina: int = sirina
        self.visina: int = visina
        pygame.init()
        self.screen = pygame.display.set_mode((sirina, visina))

    def narisi(self):
        self.screen.fill("purple")
        pygame.display.flip()
        print("Narisi")

    def vnos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        print("Vnos")

    def konec(self)->bool:
        return False
