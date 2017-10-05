#Dicing
#An example, open source game, using AGK3
#imports
import pygame
import sys
from AGK.audio import sound
from AGK.mainframe import window, keyboard
from AGK.misc import menu

# The game module
class game(object):
	#variables we need
	computer_score = 0
	player_score = 0
	target_score = 0
	player_round_score = 0
	computer_round_score=0
	#define some sound objects
	dice = sound.sound()
	dice.load("sounds/dice.ogg")
	lost_round = sound.sound()
	lost_round.load("sounds/lost_round.wav")
	lost_game = sound.sound()
	lost_game.load("sounds/lost_game.wav")
	won_round = sound.sound()
	won_round.load("sounds/won_round.wav")
	won_game = sound.sound()
	won_game.load("sounds/won_game.wav")
	music = sound.sound() # we're not going to load anything here yet
	#define our init function
	def __init__(self, title):
		w = window.window(title)
		w.show()
		self.music.load("sounds/menu_music.mp3")
		self.music.set_volume(0.40)
		self.music.play_looped()
		self.main_menu()

	def main_menu(self):
		m = menu.menu(select_sound="sounds/menu_select.ogg", move_sound="sounds/menu_move.ogg")
		m.add_item_tts("Start game","start")
		m.add_item_tts("exit game","exit")
		result = m.run("Select an option from the menu.")
		if result==-1:
			self.ExitGame()
		if result.name=="start":
			self.StartGame()
		if result.name=="exit":
			self.ExitGame()

	def ExitGame(self):
		m = menu.menu(select_sound="sounds/menu_select.ogg", move_sound="sounds/menu_move.ogg")
		m.add_item_tts("Yes", "y")
		m.add_item_tts("no", "n")
		res = m.run("You are about to exit. Are you sure?")
		if res == -1:
			self.main_menu()
		if res.name == "y":
			sys.exit()
		if res.name == "n":
			self.main_menu()

game = game(title="Dicing")