from src.domain.jabolko import Jabolko
from src.domain.snake import Snake
import random

class Svet:
    def __init__(self):
        self.snake = Snake()
        self.hrana = Jabolko(size=0.05, x=random.randint(0, 10) / 10, y=random.randint(0, 10) / 10)