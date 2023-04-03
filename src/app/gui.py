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
        hranax, hranay = self.mapiraj(x=self.svet.hrana.x, y=self.svet.hrana.y)
        hxs,hys = self.mapiraj(x=self.svet.hrana.size,y=self.svet.hrana.size)
        #pygame.draw.circle(self.screen, "red", (self.sirina/2, self.visina/2), 10)
        pygame.draw.rect(self.screen,"red", [hranax,hranay,hxs,hys])
        xG,yG = self.mapiraj(x=self.svet.snake.glava.x, y=self.svet.snake.glava.y)
        sizex, sizey = self.mapiraj(x=self.svet.snake.glava.size,y=self.svet.snake.glava.size)
        pygame.draw.rect(self.screen, "darkgreen", [xG, yG, sizex, sizey])
        pygame.display.flip()
        self.clock.tick(8)
        #self.sirina += 10
    def mapiraj(self,x,y):

        x = x*self.sirina
        y = y*self.visina
        return x,y

    def premakni(self):
        self.svet.snake.premakni()


    def vnos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key_input = pygame.key.get_pressed()

        if key_input[pygame.K_UP]:
            self.svet.snake.smer = "gor"
        if key_input[pygame.K_DOWN]:
            self.svet.snake.smer = "dol"
        if key_input[pygame.K_LEFT]:
            self.svet.snake.smer = "leva"
        if key_input[pygame.K_RIGHT]:
            self.svet.snake.smer = "desna"

    def konec(self)->bool:
        return False
