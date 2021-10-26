"""
This class defines a Player() object.
Player object holds attributes NAME and SCORE

Functions:
getName: returns player name
getScore: returns players score
addScore: add temp score to actual score
isWinner: checks if player score is 100 or above, the winning score
"""

class Player():
    def __init__(self, name="", score=0):
        self.__name = name
        self.__score = score

    def getname(self):
        return self.__name
        
    def getscore(self):
        """
        This function returns player score
        :return: player score
        """
        return self.__score

    def addScore(self, tempscore):
        """
        This function adds temp score to player score
        :param tempScore: input temp score
        :return: adds tempscore to player score
        """
        self.__score = self.__score + tempscore

    def isWinner(self):
        """
        check if winner found, if yes continue game
        :return: True if score > 100, false if score < 100
        """
        if self.getscore() >= 100:
            return True
        else:
            return False



