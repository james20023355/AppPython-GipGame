"""
Gip Game

Pseudo Code:


Player Class
    Data: score

Dice Class
    function: roll

Main Class

"""
"""
Rules:
Players take turns rolling a die.
They can continue to roll and increase their score on their turn as long as they do not roll a 1
if a one is rolled their turn ends and their points acumulated in that turn are lost
the first player to 100 wins
"""

from player import Player
from dice import Dice

class GipGame():
    def __init__(self):
        self.player1 = Player(name="Player 1")
        self.player2 = Player(name="Player 2")
        self.players = [self.player1, self.player2]
        self.tempscore = 0

    #this function will include all the actual meat fo the game
    def mainloop(self):
        while self.player1.score < 100 and self.player2.score < 100:
            for player in self.players:
                # This is where the actual game part will go

                print(f"Its {player.__name}'s turn") #Initial turn
                rollAgain = "y"
                while rollAgain == "y":
                        roll = Dice.roll()
                        print(f"You rolled a {roll}")
                        if roll == 1:
                            print(f"Sorry, thats the end of your turn. total score is {player.score}")
                            break
                        else:
                            self.tempscore += roll
                            rollAgain = input(f"current count is {self.tempscore}. Roll again? y/n")

                if rollAgain == "n":
                    player.__score += self.tempscore                            
                
                
                
                """roll = Dice.roll()
                print(f"Rolled: {roll}")
                if roll == 1:
                    print("Sorry, Thats the end of your turn.")
                else:
                    self.tempscore += roll
                    # Every consecutive turn"""
                    




                #winning conditions
                if self.player1.score >= 100:
                    print(f"{self.player1.name} WINS")
                    break
                elif self.player2.score >= 100:
                    print(f"{self.player2.name} WINS")
                    break        


if __name__ == '__main__':
    gipgame = GipGame()
    gipgame.mainloop()