from Page import *
import subprocess

class MouseController(Page):
	'''
	MouseController class handles mouse inputs from client
	'''
	def __init__(self):
		'''
		constructor initializes MouseController
		'''
		self.name = "MouseController"
		self.mouseDown = [False, False]
		
	def action(self, data, response):
		'''
		action method responds to POST call
		Paramaters:
			data (dictionary): Dictonary of json data sent by POST
			response (dictionary): dictionary of response that will be filled with output
		'''
		if self.validActionSource(data["page"]):
			if data["action"] == "buttonPress":
				if not self.mouseDown[0] and not self.mouseDown[1]:
					if data["button"] == "leftDown":
						subprocess.call(["xdotool", "mousedown", "1"])
						self.mouseDown[0] = True
					elif data["button"] == "rightUp":
						subprocess.call(["xdotool", "mousedown", "3"])
						self.mouseDown[1] = True

				elif self.mouseDown[0] and not self.mouseDown[1]:
					if data["button"] == "leftUp":
						subprocess.call(["xdotool", "mouseup", "1"])
						self.mouseDown[0] = False

				elif not self.mouseDown[1] and self.mouseDown[1]:
					if data["button"] == "rightDown":
						subprocess.call(["xdotool", "mouseup", "3"])
						self.mouseDown[1] = False
				else:
					print("invalid state")
				response["response"] = True
				return
			elif data["action"] == "move":
				delta = [data["deltaX"], data["deltaY"]]


				subprocess.call(["xdotool", "mousemove_relative", "--", delta[0], delta[1]])
				response["response"] = True

page = MouseController()	