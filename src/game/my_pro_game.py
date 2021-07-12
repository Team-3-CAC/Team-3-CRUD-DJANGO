from game.game import Game


class MyProGame(Game):
    def end(self) -> bool:
        winner = self.player1
        if self.player2.score > self.player1.score:
            winner = self.player2

        print("And de winner is =====>", winner)
        return super().end()
