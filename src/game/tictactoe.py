from game.game import Game

class TicTacToeGame(Game):

    def __init__(self) -> None:
        super().__init__()
    

    def start(self) -> bool:
        myVariable = True
        return myVariable and super().start()
    
    def end(self) -> bool:
        return super().end()