import sys
import inspect
import pygame

__all__ = ['fill_screen', 'set_renderer', 'window_size', 'tick_rate']
_win_size = (640, 480)
_tick_rate = 20

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

def window_size(width, height):
    global _win_size
    _win_size = (width, height)

def tick_rate(rate):
    global _tick_rate
    _tick_rate = rate


global _screen, _clock, _renderer
pygame.init()
_screen = pygame.display.set_mode(_win_size)
_clock = pygame.time.Clock()
_renderer = _get_renderer()

_running = True

while _running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _running = False

    if callable(_renderer):
        _renderer()

    pygame.display.flip()
    _clock.tick(_tick_rate)

pygame.quit()