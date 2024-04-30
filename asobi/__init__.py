import sys
import inspect
import pygame

__all__ = ['fill_screen', 'set_renderer']


def _get_renderer():
    main_module = sys.modules['__main__']
    r = getattr(main_module, 'render', None)
    if callable(r):
        return r
    else:
        return None

def fill_screen(color):
    _screen.fill(color)

def set_renderer(fn):
    global _renderer
    _renderer = fn

pygame.init()
_screen = pygame.display.set_mode((640, 480))
_clock = pygame.time.Clock()
_renderer = _get_renderer()

_running = True

while _running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _running = False

    if callable(_renderer):
        _renderer()
    else:
        print("No render function was found.")
        break

    pygame.display.flip()
    _clock.tick(20)

pygame.quit()