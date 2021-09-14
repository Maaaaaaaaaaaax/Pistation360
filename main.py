import pygame
import os
from random import randrange
from time import sleep
from math import sqrt


class Settings:
    width = 1920
    height = 1080
    fps = 60
    title = "PiStation 360"
    file_path = os.path.dirname(os.path.abspath(__file__))
    menu_images_path = os.path.join(file_path, "menu_images")


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.menu_images_path, image)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


class Menu(object):
    def __init__(self):
        ############ Display ############
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(Settings.title)
        Settings.width = self.screen.get_width()
        Settings.height = self.screen.get_height()

        ############# Sound ##############
        # pygame.mixer.music.load('menu_sounds/background.mp3')
        # pygame.mixer.music.play(-1, 0.0)
        # pygame.mixer.music.set_volume(.03)

        # Start des Menüs
        self.screen.fill((100, 100, 100))
        self.bootup = True
        self.timer = 0
        self.start = pygame.image.load(os.path.join(Settings.menu_images_path, "start.png")).convert()
        self.start = pygame.transform.scale(self.start, (Settings.width, Settings.height))
        self.start_alpha = 0
        self.start.set_alpha(self.start_alpha)
        self.reverse = False

        # Spielauswahlmenü
        self.menu = False
        self.all_tiles = pygame.sprite.Group()
        #for x in range(40, 1442, 467):
        #    for y in range(40, 727, 343):
        #        self.tile = Tile("tile.png", x, y)
        #        self.all_tiles.add(self.tile)
        self.tiles = pygame.image.load(os.path.join(Settings.menu_images_path, "tiles.png")).convert()
        self.tiles = pygame.transform.scale(self.tiles, (Settings.width, Settings.height))

        self.clock = pygame.time.Clock()
        self.done = False
        # pygame.mouse.set_visible(False)

    def run(self):
        while not self.done:
            self.clock.tick(Settings.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True

            if self.bootup:
                if self.timer == 60:
                    self.screen.fill((100, 100, 100))
                    if self.start.get_alpha() < 254 and self.reverse == False:
                        self.screen.blit(self.start, (0, 0))
                        self.start_alpha += 2
                        self.start.set_alpha(self.start_alpha)
                    else:
                        self.reverse = True
                    if self.reverse == True and self.start.get_alpha() > 0:
                        self.screen.blit(self.start, (0, 0))
                        self.start_alpha -= 2
                        self.start.set_alpha(self.start_alpha)
                    elif self.reverse:
                        self.bootup = False
                        self.menu = True
                else:
                    self.timer += 1

            if self.menu:
                self.screen.fill((100, 100, 100))
                self.screen.blit(self.tiles, (0, 0))

            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    menu = Menu()
    menu.run()
    pygame.quit()
