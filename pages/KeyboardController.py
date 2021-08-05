from Page import *
import subprocess
import time

class KeyboardController(Page):
	'''
	KeyboardController class updates the volume of the linux system hosting the webserver
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
				response["response"] = True
				for letter in data["keySequence"]:
					if letter in "abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
						subprocess.call(["xdotool", "type", letter])
						time.sleep(0.1)
						response["response"] = True
						return
					elif letter == " ":
						print("SPACE SPACE SPACE")
						subprocess.call(["xdotool", "type", "space"])
						time.sleep(0.1)
						response["response"] = True
						return
		response["response"] = False
		return None

page = KeyboardController()