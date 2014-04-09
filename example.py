#!/usr/bin/env python

import pyglet
from pyglet import gl

from pixfont import *

register_font("example", "example.png", 5, 10)
font = get_font("example")

window = pyglet.window.Window(width=640, height=400)

batch = pyglet.graphics.Batch()
text = font.render(batch, window.width//2, window.height//2, "this is an example", align="center")

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()

