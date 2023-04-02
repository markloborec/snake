import pygame
import time
from src.domain.svet import Svet



class Gui:
    def __init__(self, sirina: int, visina: int):
        self.svet: Svet = Svet()
        self.sirina: int = sirina
        self.visina: int = visina
        pygame.init()
        self.screen = pygame.display.set_mode((sirina, visina))
        self.clock = pygame.time.Clock()
    def narisi(self):
        self.screen.fill("white")
        #pygame.draw.circle(self.screen, "red", (self.sirina/2, self.visina/2), 10)
        hrana = pygame.draw.rect(self.screen,"red", [150,150,10,10])
        kvadrat = pygame.draw.rect(self.screen, "darkgreen", [self.sirina/2, self.visina/2, 10, 10])
        pygame.display.flip()
        self.clock.tick(10)
        #self.sirina += 10

    def premakni(self):
        key_input = pygame.key.get_pressed()
        press3 = 0

        if key_input[pygame.K_UP]:
            press1 = 1
            if press1 == 1:
                self.visina -= 10
                #self.sirina -= 10
        if key_input[pygame.K_DOWN]:
            press2 = 1
            if press2 == 1:
                self.visina += 10
                #self.sirina -= 10
            print("Dol")
        if key_input[pygame.K_LEFT]:
            press3 = 1
            if press3 == 1:
                #self.visina += 10
                self.sirina -= 10
                print(press3)
        if key_input[pygame.K_RIGHT]:
            press4 = 1
            if press4 == 1:
                #self.visina += 10
                self.sirina += 10
                print("Desna")
        if press3 == 0:
            self.sirina += 10
            print(press3)
        press3 = 1
        #BORDERX
        if self.sirina > 805:
            self.sirina = 5
        if self.sirina < -5:
            self.sirina = 805
        #BORDERY
        if self.visina > 805:
            self.visina = 5
        if self.visina < -5:
            self.visina = 805




        #print("Narisi")

    def vnos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #print("Vnos")

    def konec(self)->bool:
        return False
