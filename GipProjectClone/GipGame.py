"""
GIP GAME

Rules:
Players take turns rolling a die.
They can continue to roll and increase their score on their turn as long as they do not roll a 1
if a one is rolled their turn ends and their points accumulated in that turn are lost
the first player to 100 wins

This defines the main, and uses Player and Dice objects to play.
"""

from richGui import richGUI
from player import Player
from dice import Dice
from rich import console
from rich.console import Console

console = Console()


class GipGame():
    def __init__(self):
        self.player1 = Player(name="Player 1")
        self.player2 = Player(name="Player 2")
        self.players = [self.player1, self.player2]
        self.continueGame = 'y'
        self.gui = richGUI("Player 1", "Player 2", self.player1, self.player2, self.player1.getscore(),
                           self.player2.getscore(), 0, 0)
        # self.gui = richGUI(self.player1.getname(), self.player2.getname(), self.player1.getscore(), self.player2.getscore(), 0, 0)

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
        self.gui.updateP1Name(self.player1.getname())
        self.gui.updateP2Name(self.player2.getname())
        console.print(f":pig: {player.getname()}'s turn! :pig:", style="bold blue")
        while rollAgain == "y":
            roll = Dice.roll()
            self.gui.updateRoll(roll)

            if roll == 1:
                # if player rolls a 1, they do not get to go again and temp score = 0
                self.gui.printGUI()
                console.print(f":pig2: {player.getname()}! TURN TERMINATED! :pig2:", style="bold red")
                input()
                rollAgain = "f"  # Changed this variable from "n" to "f" as to not add the score when they lost that round
            else:
                tempscore += roll
                self.gui.updateTemp(tempscore)
                if player.getscore() + tempscore > 100:
                    player.addScore(tempscore)
                    self.gui.updateTemp(player.getscore())
                    return
                else:
                    self.gui.printGUI()
                    rollAgain = input(f"Roll again? Y/N: ").lower()
                    print()

        if rollAgain == "n":
            player.addScore(tempscore)
            if player.getname() == "Player 1":
                self.gui.updateScore1(player.getscore())
            else:
                self.gui.updateScore2(player.getscore())
            print()
            return

    def gameOver(self, player):
        """
        This function takes in winning player and ends the game
        :param player:
        :return: continueGame = no
        """
        self.gui.printGameOver(player.getname())
        self.continueGame = 'n'
        quit()

    def introMessage(self):
        """ This method is in charge of the introduction to the game"""
        from time import sleep

        tutorial = [
            "\n> Each player gets a turn to roll a die, if the player rolls a number between 2 and 6.",
            "> That number is added to the overall score for that turn.",
            "> The player will have the option to keep re-rolling.",
            "> But if they roll a 1, the amount of points built up in that turn is lost.",
            "> And the other player gets a turn",
            "> First Person to 100 wins.",
            "> Good Luck.\n"]

        intro = input("\nWould you like to learn the Rules of Gip Game? [Y/N]: ")

        if intro.upper() == "Y":
            for message in tutorial:
                print(message)
                sleep(5)
        elif intro.upper() == "N":
            pass
        else:
            print("> [ERROR]: Please Enter either 'Y' or 'N'.")
            self.introMessage()

    def startGame(self):
        """
        This function prompts user to start game as well as asking whether to use custom names
        :return: continueGame Y or N
        """
        print("Welcome to Gip Game!\n")
        self.player1.changeName(input("Player 1, enter your name: "))
        self.player2.changeName(input("Player 2, enter your name: "))
        self.introMessage()
        self.continueGame = input(f"Start game? Y/N ").lower()

    def mainloop(self):
        """
        Main loop for game. Whilst gameContinue is still "y"
        each player takes turn to roll dice using playerMove()
        If isWinner == true, game over
        """
        while self.continueGame == 'y':
            for player in self.players:
                self.playerMove(player)
                if player.isWinner() == True:
                    self.gameOver(player)


if __name__ == '__main__':
    gipgame = GipGame()
    gipgame.startGame()
    if gipgame.continueGame == 'y':
        gipgame.mainloop()
