"""
GIP GAME

Rules:
Players take turns rolling a die.
They can continue to roll and increase their score on their turn as long as they do not roll a 1
if a one is rolled their turn ends and their points accumulated in that turn are lost
the first player to 100 wins

This defines the main, and uses Player and Dice objects to play.
"""
import pygame
from player import Player
from dice import Dice

class GipGame():
    def __init__(self):
        self.player1 = Player(name="Player 1")
        self.player2 = Player(name="Player 2")
        self.players = [self.player1, self.player2]
        self.continueGame = 'y'

    def playerMove(self, player):
        """
        This function takes in current player and allows them to use the Dice roll() function.
        If their roll is 1, their turn ends and they do not get to bank their score
        If roll > 1, roll is added to temp score. Player gets option to roll again, or bank temp score
        :param player: current player
        :return:
        """
        rollAgain = "y"
        tempscore = 0
        roll = Dice.roll()
        print(f"{player.getname()}'s turn!")

        while rollAgain == "y":
            roll = Dice.roll()
            print(f"You rolled a {roll}")
            if roll == 1:
                #if player rolls a 1, they do not get to go again and temp score = 0
                print(f"Sorry, thats the end of your turn.")
                rollAgain = "n"
            else:
                tempscore += roll
                if player.getscore() + tempscore > 100:
                    player.addScore(tempscore)
                    return
                else:
                    rollAgain = input(f"{player.getname()}'s current count: {tempscore} \nRoll again? Y/N \n").lower()

        if rollAgain == "n":
            player.addScore(tempscore)
            return

    def gameOver(self, player):
        """
        This function takes in winning player and ends the game
        :param player:
        :return: continueGame = no
        """
        print(f"GAME OVER! {player.getname()} wins! Thanks for playing!")
        self.continueGame = 'n'
        quit()

    def startGame(self):
        """
        This function prompts user to start game.
        :return: continueGame Y or N
        """
        self.continueGame = input(f"Welcome to Gip! \nStart game? Y/N \n").lower()


    def mainloop(self):
        """
        Main loop for game. Whilst gameContinue is still "y"
        each player takes turn to roll dice using playerMove()
        If isWinner == true, game over
        """
        while self.continueGame == 'y':
            for player in self.players:
                self.playerMove(player)
                print(f"{player.getname()}'s total score is {player.getscore()}.\n")
                if player.isWinner() == True:
                    self.gameOver(player)

if __name__ == '__main__':
    gipgame = GipGame()
    gipgame.startGame()
    if gipgame.continueGame == 'y':
        gipgame.mainloop()

