from Page import *
import subprocess
import time

class KeyboardController(Page):
	'''
	KeyboardController class simulates keyboard server side
	'''
	def __init__(self):
		'''
		constructor initializes KeyboardController
		'''
		self.name = "KeyboardController"
		
	def action(self, data, response):
		'''
		action method responds to POST call
		Paramaters:
			data (dictionary): Dictonary of json data sent by POST
			response (dictionary): dictionary of response that will be filled with output
		'''
		if self.validActionSource(data["page"]):
			if data["action"] == "keySequence":
				for letter in data["keySequence"]:
					if letter in "abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
						subprocess.call(["xdotool", "type", letter])
						time.sleep(0.1)
						response["response"] = True
						return
					elif letter == "+":
						subprocess.call(["xdotool", "type", " "])
						time.sleep(0.1)
						response["response"] = True
						return
			elif data["action"] == "buttonPress":
				if data["button"] == "enter":
					subprocess.call(["xdotool", "key", "Return"])
					time.sleep(0.1)
					response["response"] = True
					return
				elif data["button"] == "backspace":
					subprocess.call(["xdotool", "key", "BackSpace"])
					time.sleep(0.1)
					response["response"] = True
					return
		response["response"] = False
		return None

page = KeyboardController()