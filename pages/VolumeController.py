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
		self.volume = self.mixer.getvolume()[0]
		self.volumeStep = 10

	def action(self, data, response):
		'''
		action method responds to POST call

		Paramaters:
			data (dictionary): Dictonary of json data sent by POST
			response (dictionary): dictionary of response that will be filled with output
		'''
		if self.validActionSource(data["page"]):
			self.mixer = alsaaudio.Mixer()
			self.volume = int(self.mixer.getvolume()[0])

			if data["action"] == "getState":
				response["response"] = True
				response["volume"] = self.volume
				response["muted"] = self.muted
				return None;
			elif data["action"] == "buttonPress":
				response["response"] = True
				
				if data["button"] == "increaseVolume":
					m.setvolume(self.volume + self.volumeStep)
				elif data["button"] == "decreaseVolume":
					m.setvolume(self.volume - self.volumeStep)
				elif data["button"] == "toggleMute":
					self.muted = not self.muted
					if self.muted:
						m.setvolume(0)
					else:
						m.setvolume(self.volume)
				elif data["button"] == "togglePlayPause":
					pass
				elif data["button"] == "skipNext":
					pass
				elif data["button"] == "skipPrev":
					pass
				return None;
		response["response"] = False
		return None;

page = VolumeController()