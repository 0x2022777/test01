import kivy

from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Assalaumagaleikum!!!')


if __name__ == '__main__':
    MyApp().run()

    