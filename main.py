import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from camera import CameraCv

class Microscope(Screen):

    pass

#-- main widget
class Main(Screen):
    pass

#--scene manager
class ScreenManager(ScreenManager):
    pass

#--load my.kv gui
GUI = Builder.load_file('gui.kv')

#--main app
class MyApp(App):

    def build(self):

        return GUI

if __name__ == "__main__":

    MyApp().run()