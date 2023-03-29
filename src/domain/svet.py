from src.domain.hrana import Hrana
from src.domain.snake import Snake
import random

class Svet:
    def __init__(self):
        self.snake = Snake()
        self.hrana = Hrana(size=0.1,x=random.randint(0,10)/10,y=random.randint(0,10)/10)