Pixel font implementation for Pyglet
====================================

This is a very simple implementation of pixel fonts for pyglet. The basic idea is
to prepare an image with the font characters and use pyglet's `Sprite` class to
render text using a `Batch` in an efficient way.

First register a font::

    from pixfont import register_font
    register_font("example", "example.png")

Then get a PixFont object:

    from pixfont import get_font
    font = get_font("example")

The PixFont object can be used to render text into a `pyglet.sprite.Sprite` batch::

    import pyglet
    batch = pyglet.graphics.Batch()

    text = font.render(batch, 10, 10, "example text")

This will render the "example text" text at (10, 10) position.

Then the batch can be drawn with the usual `batch.draw`, or using `text.draw` (it
is in fact executing `batch.draw`). If a batch is not provided in the `render` call,
a new batch will be created for just that text.

Optional parameters of `PixFont.render` are:

- `align`: that can be "left" (default), "right" and "center"; describing the text
           alignment based on the text position.
- `group`: the group in which the text will be redered in the batch (None by default).

See `example.py` for a complete example and run `pydoc pixfont` for method's documentation.

Juan J. Martinez <jjm@usebox.net>

