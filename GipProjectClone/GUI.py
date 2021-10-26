"""
GUI.py contains a Text and Window class. The Window class initializes pygame and sets up a GUI window.
Text class allows for text to be easily managed in one call, isntead of setting and rendering each individual text
for display in GUI window.
"""

import sys
import pygame
pygame.init()
"""Initialize pygame and set up GUI window"""
class Text:
    """Create a text object."""
    def __init__(self, text, font, fontsize, fontcolour, pos):
        self.text = text #text to be displayed on screen
        self.pos = pos #position
        self.font = font
        self.fontsize = fontsize
        self.fontcolour = fontcolour
        self.set_font()
        self.render()

    def set_font(self):
        """Set the Font object from name and size."""
        self.font = pygame.font.SysFont(self.font, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolour)
        self.rect = self.img.get_rect()
        self.rect = self.pos #display text rect in pos=(x,y), passed through when function called


    def draw(self):
        """Draw the text image to the screen."""
        Window.screen.blit(self.img, self.pos)

class Window:
    """
    This class defines a Window. Paramaters include: screen width, height, background colour, title, and gameRunning
    """
    def __init__(self, screenwidth, screenheight, bgcolour=(255,255,255), title="GIP GAME", gameRunning = True):
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.bgcolour = bgcolour
        self.title = title
        self.gameRunning = gameRunning
        Window.screen = pygame.display.set_mode((self.screenwidth, self.screenheight))

    def displayWindow(self):
        """
        Initialize pygame window
        If user quits game, window will exit
        """
        pygame.init()
        screen = pygame.display.set_mode((self.screenwidth, self.screenheight))
        pygame.display.set_caption(self.title)
        screen.fill(self.bgcolour)
        img = pygame.image.load('PIGG.png')
        img2 = pygame.image.load('PIGGG.png')
        bg = pygame.image.load('farmland.png')


        Window.screen.blit(bg,[0,0])
        Window.title = Text('Welcome to Gip Game', None, 50, 'black', pos=(220,50))
        Window.title.draw()
        
        Window.screen.blit(pygame.transform.flip(img2, True, False), [0,0])
        #Window.screen.blit(pygame.transform.flip(img, True, False), [self.screenwidth-100,0])
        Window.screen.blit(img2,[575,0])
        """Display window using flip()"""
        pygame.display.flip()  # .flip function displays window


        while self.gameRunning == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__gameRunning = False
                    pygame.quit()
                    sys.exit()


    def quitWindow(self):
        """
        This function can be called from GipGame on a button click to exit window
        :return: quits window
        """
        pygame.quit()
        sys.exit()



window = Window(800, 600)
window.displayWindow()
