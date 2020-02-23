import pygame

class User():
    def __init__(self,ai_object):
        self.screen = ai_object.screen
        self.sc_rect = ai_object.screen.get_rect()

        self.image = pygame.image.load('images/user.bmp')
        self.rect = self.image.get_rect()



        self.rect.midtop = self.sc_rect.midtop

    def bltime(self):
        self.screen.blit(self.image, self.rect)