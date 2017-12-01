"""
Dicing
An example, open source game, using AGK3
Game source by Kyle Cunningham.
AGK3 by Kyle Cunningham, modified from the original AGK by Mason Armstrong.
Accept where otherwise noted, all source code is under GPL, version 3.
See the license file in this repository.
"""

#imports
import pygame
import random
import sys
from AGK.audio import sound
from AGK.mainframe import window, keyboard
from AGK.misc import menu, dialog
from AGK.speech import auto

# The game module
class game(object):
	#variables we need
	computer_score = 0
	player_score = 0
	target_score = 0
	player_round_score = 0
	computer_round_score=0
	turn = 1
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
		m.add_item_tts("Game Credits","credits")
		m.add_item_tts("exit game","exit")
		result = m.run("Select an option from the menu.")
		if result==-1:
			self.ExitGame()
		if result.name=="start":
			self.SelectTargetScore()
		if result.name == "credits":
			self.ShowCredits()
		if result.name=="exit":
			self.ExitGame()

	def ShowCredits(self):
		dialog.dialog("Game credits:", type=2)
		dialog.dialog("Programming by Kyle Cunningham, www.underworldtech.com.", type=2)
		dialog.dialog("Music by Eric Matyas, www.soundimage.org.", type=2)
		dialog.dialog("Sounds from various free sources.", type=2)
		self.main_menu()

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

	def SelectTargetScore(self):
		m = menu.menu(select_sound="sounds/menu_select.ogg", move_sound="sounds/menu_move.ogg")
		m.add_item_tts("Easy (6 rounds)","1")
		m.add_item_tts("medium (9 rounds)","2")
		m.add_item_tts("Difficult (12 rounds)","3")
		res = m.run("Select a difficulty level.")
		if res == -1:
			self.main_menu()
		if res.name=="1":
			self.target_score=6
			self.StartGame()
		if res.name=="2":
			self.target_score=9
			self.StartGame()
		if res.name=="3":
			self.target_score=12
			self.StartGame()

	def StartGame(self):
		dialog.dialog("Welcome. Your target is " + str(self.target_score) + " rounds. Press enter to begin. When in the game, press R to roll the dice when it is your turn. Good luck!", type=2)
		while 1:
			if self.turn == 1:
				self.take_player_turn()

	def RollDice(self):
		self.dice.stop()
		self.dice.play()
		return random.randint(1,6)

	#Lets add some game logic.
	def take_player_turn(self):
		rolls = 0
		temp_score = 0
		auto.speak("Its your turn. Roll three times.")
		key = keyboard.pressed()
		if key == pygame.K_r:
			num = self.RollDice()
			rolls = rolls + 1
			temp_score = temp_score + num
			auto.speak("You got a " + str(num) + ". You have " + str(3 - rolls) + " dice remaining.")
		if key == pygame.K_ESCAPE:
			self.main_menu()

#Set up the game.
game = game(title="Dicing")