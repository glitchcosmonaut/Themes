from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import Button, ToggleButton
from kivy.graphics import Color
from PaintBrush import PaintBrush
from random import random


# Create the App class
class DrawingApp(App):

    def __init__(self):
        super().__init__()
        self.eraserbtn = None
        self.painter = None
        self.background = Color(0, 0, 0)

    def build(self):
        parent = Widget()
        self.painter = PaintBrush()

        # Creates toggle button for eraser
        self.eraserbtn = ToggleButton(text='Eraser')
        self.eraserbtn.bind(on_release=self.erase_toggle)

        # Creates button for canvas clear
        clearbtn = Button(text="Clear", pos=(1500, 0))
        clearbtn.bind(on_release=self.clear_canvas)

        parent.add_widget(self.painter)
        parent.add_widget(self.eraserbtn)
        parent.add_widget(clearbtn)
        return parent

    def erase_toggle(self, obj):
        if self.painter.color == self.background:
            self.painter.color = Color(random(), random(), random())
        else:
            self.painter.color = self.background

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


DrawingApp().run()
