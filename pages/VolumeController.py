from Page import *
import alsaaudio

class VolumeController(Page):
	'''
	VolumeController class updates the volume of the linux system hosting the webserver
	'''
	def __init__(self):
		'''
		constructor initializes VolumeController
		'''
		self.mixer = alsaaudio.Mixer()
		self.name = "VolumeController"
		self.muted = False
		self.volume = self.mixer.getvolume()

	def action(self, data, response):
		'''
		action method responds to POST call

		Paramaters:
			data (dictionary): Dictonary of json data sent by POST
			response (dictionary): dictionary of response that will be filled with output
		'''
		if self.validActionSource(data["page"]):
			if data["action"] == "getState":
				response["response"] = True
				response["volume"] = int(self.volume)
				response["muted"] = self.muted
				return None;
			elif data["action"] == "buttonPress":
				response["response"] = True
				return None;
		response["response"] = False
		return None;

page = VolumeController()