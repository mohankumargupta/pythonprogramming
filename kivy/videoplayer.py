#!/usr/bin/kivy
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import requests

def panRight(instance):
	requests.get('http://192.168.2.118:99/decoder_control.cgi?command=6&onestep=1&user=admin&pwd=')

def panLeft(instance):
	requests.get('http://192.168.2.118:99/decoder_control.cgi?command=4&onestep=1&user=admin&pwd=')

def tiltUp(instance):
	requests.get('http://192.168.2.118:99/decoder_control.cgi?command=0&onestep=1&user=admin&pwd=')

def tiltDown(instance):
	requests.get('http://192.168.2.118:99/decoder_control.cgi?command=2&onestep=1&user=admin&pwd=')

def horpatrolOn(instance):
	requests.get('http://192.168.2.118:99/decoder_control.cgi?command=28&onestep=0&user=admin&pwd=')
	requests.get('http://192.168.2.118:99/decoder_control.cgi?command=28&onestep=0&user=admin&pwd=')

def horpatrolOff(instance):
	requests.get('http://192.168.2.118:99/decoder_control.cgi?command=29&onestep=1&user=admin&pwd=')


class MyApp(App):
	def build(self):
		layout = BoxLayout(orientation='vertical')
		buttonsLayout = BoxLayout()
		secondButtonsLayout = BoxLayout()
		thirdButtonsLayout = BoxLayout()
		#a='C:\\Users\\mohan\\Downloads\\lacuca.mp3'
		#a='C:\\Users\\mohan\\Downloads\\My Blackberry Is Not Working - The Two Ronnies.mp4'
		#a='rtsp://38.96.148.99:1935/live/bb'
		#a='rtsp://93.120.27.78:1935/live/cnn.stream'
		#a='rtsp://93.120.27.78:1935/live/syfy.stream'
		#a='rtsp://93.120.27.78:1935/live/hbousa.stream'
		#a = 'C:\\Users\\mohan\\Downloads\\kivy\\kivy\\examples\\widgets\\softboy.avi'
		#a='http://admin@192.168.2.118:99/videostream.cgi?user=admin&pwd=&resolution=32&rate=0'
		
		#try http streaming from vlc
		a='http://localhost:8082/video'
		
		#open stream in vlc and click Stream instead of play
		#a='rtsp://localhost:8554/test.sdp'

		videoplayer =  VideoPlayer(source=a,state="play",options={'eos':'loop'}, size_hint=(1,2))
		panrightbutton = Button(text="Pan +", size_hint=(0.5,1))
		panrightbutton.bind(on_press=panRight)
		panleftbutton = Button(text="Pan -", size_hint=(0.5,1))
		panleftbutton.bind(on_press=panLeft)
		tiltupbutton = Button(text="Tilt +", size_hint=(0.5,1))
		tiltupbutton.bind(on_press=tiltUp)
		tiltdownbutton = Button(text="Tilt -", size_hint=(0.5,1))
		tiltdownbutton.bind(on_press=tiltDown)		
		buttonsLayout.add_widget(panleftbutton)
		buttonsLayout.add_widget(panrightbutton)
		secondButtonsLayout.add_widget(tiltupbutton)
		secondButtonsLayout.add_widget(tiltdownbutton)
		horpatrolonbutton = Button(text='Hor. Patrol On', size_hint=(0.5,1))
		horpatrolonbutton.bind(on_press=horpatrolOn)
		horpatroloffbutton = Button(text='Hor. Patrol Off', size_hint=(0.5,1))
		horpatroloffbutton.bind(on_press=horpatrolOff)
		thirdButtonsLayout.add_widget(horpatrolonbutton)
		thirdButtonsLayout.add_widget(horpatroloffbutton)		
		layout.add_widget(videoplayer)
		layout.add_widget(buttonsLayout)
		layout.add_widget(secondButtonsLayout)
		layout.add_widget(thirdButtonsLayout)
		return layout


if __name__ == '__main__':
	MyApp().run()

