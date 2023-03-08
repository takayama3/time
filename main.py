import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config


px = 45
size = (9, 18)
title = 'kkk'


Config.set('graphics', 'width', str(size[0] * px))
Config.set('graphics', 'height', str(size[1] * px))


class Window(App):

    def build(self):
        self.title = title
        return Builder.load_file('window.kv')


Window().run()
