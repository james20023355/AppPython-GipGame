"""
This class will operate by having a template which will be called over and over with the ability to update the data within.

initialize variables in class
Main will call printGUI function and pass in all necessary variable that need updating

PrintGui function will need to take in any of the available variables and edit the GUI while keeping all other entries

╭───────────────────────────╮
│         Roll: 3           │
│     current score: 52     │
│ player1           player2 │
│ score: 55        score:32 │
╰───────────────────────────╯


"""


from rich import console
from rich.console import Console
console = Console()

class richGUI():
    def __init__(self, player1="", player2="", score1=0, score2=0, roll=0, tempscore=0):
        self.__player1 = player1
        self.__player2 = player2
        self.__score1 = score1
        self.__score2 = score2
        self.__roll = roll
        self.__tempscore = tempscore


    def printGUI(self):
        """
        This function will be the template for the data that will be called each turn.
        """
        roll = f"Roll: {self.__roll}"
        current = f"Current count: {self.__tempscore}"
        player1 = f"{self.__player1}"
        player2 = f"{self.__player2}"
        score1 = f"Score:{self.__score1}"
        score2 = f"Score:{self.__score2}"        
        message = ""

        console.print(f"╭────────────────────────────╮", style="green")
        console.print(f"[green]│[/]{roll:^28}[green]│[/]")
        console.print(f"[green]│[/]{current:^28}[green]│[/]")
        console.print(f"[green]│[/]{message:^28}[green]│[/]")
        console.print(f"[green]│[/] {player1:<13}{player2:>13} [green]│[/]")
        console.print(f"[green]│[/]  [#de8221 bold]{score1:<12}{score2:>12}[/]  [green]│[/]")
        console.print(f"╰────────────────────────────╯", style="green")

    def printGameOver(self, player):
        """
        Called when a player has won.
        """
        congrats = "Congradulations!"
        playe = f"{player} WINS!"
        goodjob = "Good Work!"
        console.print(f"╭────────────────────────────╮", style='magenta')
        console.print(f"[magenta]│[/]{congrats:^28}[magenta]│[/]")
        console.print(f"[magenta]│[/]{playe:^28}[magenta]│[/]")
        console.print(f"[magenta]│[/]{goodjob:^28}[magenta]│[/]")
        console.print(f"╰────────────────────────────╯", style="magenta")

    def updatePlayer1(self, player):
        self.__player1 = player
    
    def updatePlayer2(self, player):
        self.__player2 = player

    def updateScore1(self, score):
        self.__score1 = score

    def updateScore2(self, score):
        self.__score2 = score

    def updateRoll(self, roll):
        self.__roll = roll

    def updateTemp(self, temp):
        self.__tempscore = temp
