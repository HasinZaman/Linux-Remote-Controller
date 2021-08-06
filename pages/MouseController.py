from Page import *

class MouseController(Page):
	'''
	MouseController class updates the volume of the linux system hosting the webserver
	'''
	def __init__(self):
		'''
		constructor initializes MouseController
		'''
		self.name = "MouseController"
		
	def action(self, data, response):
		'''
		action method responds to POST call
		Paramaters:
			data (dictionary): Dictonary of json data sent by POST
			response (dictionary): dictionary of response that will be filled with output
		'''
		if self.validActionSource(data["page"]):
			if data["action"] == "buttonPress":
				print(data["button"])
			elif data["action"] == "move":
				print(data["deltaX"])
				print(data["deltaY"])

page = MouseController()	