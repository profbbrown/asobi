# Asobi
Pygame is a great package for Python to create games. Asobi is a wrapper for Pygame to give
Python learners access to the game engine by reducing the amount of Python syntax
and concepts needed to build simple games and/or animations.

At its simplest, a programmer needs only a scalar state variable, such as a number,
a function to update the state variable every tick of the clock, and a functon to render
the image. Asobi takes care of running the UI loop, passing events to the programmer,
and offering a simplified API for displaying shapes and images.

# Usage
The user will only need a single import to get started.

    import asobi

Next, set the window dimensions, or use the default of 640x480.

    window_size(640, 480)

Optionally set the clock rate of ticks per second. Default is 20.

    tick_rate(10)

You can start drawing on the surface (window). If running interactively, the
shapes will appear immediately. This helps learners see what effect their
instructions are having on the image.

Preferrably, the user would define a rendering function (by default, `render`)
that draws the image. If not using the default name, set the rendering function.

    set_renderer(my_render)

