#!/usr/bin/kivy
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
	def build(self):
		return Button(text='Hello world',
			fontsize=150,
			background_color=(0,0,1,1))


if __name__ == '__main__':
	MyApp().run()
