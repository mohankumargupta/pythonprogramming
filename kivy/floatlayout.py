#!/usr/bin/kivy
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(App):
	def build(self):
		f = FloatLayout()
		s = Scatter()
		l = Label(text='hello')
		t = TextInput(text='hello')
		f.add_widget(s)
		s.add_widget(l)
		s.add_widget(t)
		return f

if __name__ == '__main__':
	MyApp().run()