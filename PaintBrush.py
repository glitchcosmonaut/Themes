from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from random import random


class PaintBrush(Widget):

    def __init__(self):
        super().__init__()
        self.color = Color(random(), random(), random())

    def on_touch_down(self, touch):
        with self.canvas:
            Color(self.color.r, self.color.g, self.color.b)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(50, 50))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=25)

    # On mouse movement how Paint_brush behave
    def on_touch_move(self, touch):
        with self.canvas:
            touch.ud['line'].points += [touch.x, touch.y]