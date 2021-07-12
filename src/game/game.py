from random import random
#from player import *
from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self) -> None:
        """
        Solo el constructor
        """
        self.__player1 = None
        self.__player2 = None

    def __str__(self) -> str:
        return f"Esto es el objeto Game"

    @abstractmethod
    def start(self) -> bool:
        pass
    
    @abstractmethod
    def end(self) -> bool:
        pass

    @property
    def player1(self):
        return self.__player1

    @player1.setter
    def player1(self, player):
        self.__player1 = player

    @property
    def player2(self):
        return self.__player2

    @player2.setter
    def player2(self, player):
        self.__player2 = player

    @abstractmethod
    def update(self) -> bool:
        self.player2.score = random() * 10
        self.player1.score = random() * 10
        return False
