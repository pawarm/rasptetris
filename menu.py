from tetris import Tetris
import keyboard
import os
import time
import threading
from segment_display import LED_Module
from MAX7219 import MAX7219

from config import text_display

class Menu():
	
	def __init__(self):
		self.game = Tetris()
		self.led_display = LED_Module()
		self.led = MAX7219()
		self.to_show_led = ""
		self.showed_led = ""
		self.to_show_matrix = []
		self.showed_matrix = []
		self.state = ""
		self.change_state("PLAY")
		self.num = 0
	
	def press(self, event):
		if self.state == "PLAY":
			if event.name == 'down':
				self.change_state("QUIT")
			elif event.name == 'space':
				self.change_state("RUN")
				
		elif self.state == "QUIT":
			if event.name == 'up':
				self.change_state("PLAY")
			elif event.name == 'space':
				self.change_state("EXIT")
				
		elif self.state == "LOST":
			if event.name == 'space':
				self.game.quit()
				self.change_state("PLAY")
				
		elif self.state == "RUNNING":	
			if event.name == 'left':
				self.game.move(+1)
			elif event.name == 'right':
				self.game.move(-1)
			elif event.name == 'down':
				self.game.drop()
			elif event.name == 'up':
				self.game.rotate_stone()
			elif event.name == 'p':
				self.game.toggle_pause()
			elif event.name == 'space':
				self.game.start_game()
			elif event.name == 'esc':
				self.game.quit()
				self.change_state("PLAY")
	
	def change_state(self, st):
		self.state = st
		if self.state == "PLAY":
			self.to_show_led = text_display[self.state]
		elif self.state == "LOST":
			self.led_display.set_screen(self.game.message)
			self.showed_led = self.game.message
		elif self.state == "QUIT":
			self.to_show_led = text_display[self.state]
		elif self.state == "EXIT":
			self.to_show_led = text_display[self.state]
			time.sleep(0.5)
			os._exit(0)
	
	def run(self):
		while True:
			if self.state == "RUN":
				self.change_state("RUNNING")
				game_thread = threading.Thread(target=self.game.run)
				game_thread.start()
			if self.state in ["RUNNING", "LOST"]:
				if self.game.gameover:
					self.change_state("LOST")
				if self.game.message != self.showed_led:
					self.led_display.set_screen(self.game.message)
					self.showed_led = self.game.message
			else:
				if self.to_show_led != self.showed_led:
					self.led_display.set_screen(self.to_show_led)
					self.showed_led = self.to_show_led
			if self.game.led_matrix != self.showed_matrix:
				self.led.WriteMap(self.game.led_matrix)
				self.showed_matrix = self.game.led_matrix
				
			time.sleep(0.01)
			
if __name__ == '__main__':
	game = Menu()
	keyboard.on_press(game.press)
	game.run()
