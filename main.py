import pygame
pygame.init()

from Chest import *


# минимальная программа Pygame
class Game:
    def __init__(self, argSize: int, caption: str):
        self.window = pygame.display.set_mode(size=(argSize, argSize))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

    def run(self, FPS: int):

        isGame = True
        while isGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isGame = False

            self.window.fill(pygame.Color('black'))
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game(1000, "Game")
    game.run(60)


# Surface - отрисовка и группировка графических объектов, работа с изображениями и текстом, изменение их
# Rect - размещение, перемещение, столкновения
# Sprite - Surf + Rect
