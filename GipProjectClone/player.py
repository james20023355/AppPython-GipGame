"""
Player Class
"""

class Player():
    def __init__(self, name="", score=0):
        self.__name = name
        self.__score = score

    @property
    def score(self):
        return self.score

    def addScore(self, tempScore):
        self.score += tempScore