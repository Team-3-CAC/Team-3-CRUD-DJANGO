from game.game import Game
from game.tictactoe import TicTacToeGame
from game.my_pro_game import MyProGame
import sys

class FactoryGame:
    
    @staticmethod
    def createGame(gameType) -> Game:
        myGame = None
        try:
            if gameType == "TicTacToeGame":
                myGame = TicTacToeGame()
            elif gameType == "MyProGame":
                myGame = MyProGame()
        except:
            print("no puedo crear la instancia ", sys.exc_info()[1])
        finally:
            print("Construyo algo")


        return myGame