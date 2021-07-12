from ale.utils import factorial
from ale.utils import division
from game.factorygame import FactoryGame
from game.game import *
from game.tictactoe import *
from game.player import *
from game.my_pro_game import *
from game.factorygame import *
import sys
import json
#from sys import exc_info

def main():
    """
    main() -> None
    """
    x = 12313
    y = 0
    try:
        division(x, y)
    except ZeroDivisionError:
        y =  y + 0.0000001
        division(x, y)
        print("Exception por division por 0")
    except:
        print("Exception", sys.exc_info()[2])
    finally:
        print("lesto")

    print(factorial(3))

    myPlayer1 = Player("Ale", 1)
    myPlayer2 = Player("Lolo", 2)

    print(f"Player1: {myPlayer1} and Player2: {myPlayer2}")
    
    myGame = FactoryGame.createGame("TicTacToeGame") #Factory parametrizada
    
    myGame.player1 = myPlayer1
    myGame.player2 = myPlayer2

    myPlayer1.id = 158

    myGame.start()

    print(Player.score)

    while(myGame.update()):
        print(myGame)

    print(myPlayer1.getNombre())

    print(Player.score)

    myGame.end()
    
    return None




if __name__ == "__main__":
    main()
    
 
    