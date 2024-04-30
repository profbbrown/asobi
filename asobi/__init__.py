import pygame

__all__ = ['fill_screen', 'set_renderer']

pygame.init()
_screen = pygame.display.set_mode((640, 480))
_clock = pygame.time.Clock()
_renderer = None


def fill_screen(color):
    _screen.fill(color)

def set_renderer(fn):
    global _renderer
    _renderer = fn

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    _renderer()
    pygame.display.flip()
    _clock.tick(20)