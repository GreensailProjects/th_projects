import pygame
class Ship:
    def __init__(self, ai_game):
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.image =pygame.image.load('images/d7ee96a96b8e1b694af3a1f0f6238f43.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.settings = ai_game.settings
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.x > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

