class KeyboardController(Page):
	'''
	KeyboardController class updates the volume of the linux system hosting the webserver
	'''
	def __init__(self):
		'''
		constructor initializes KeyboardController
		'''
		self.name = "KeyboardController"
		pass
	def action(self, data, response):
		'''
		action method responds to POST call
		Paramaters:
			data (dictionary): Dictonary of json data sent by POST
			response (dictionary): dictionary of response that will be filled with output
		'''
		pass