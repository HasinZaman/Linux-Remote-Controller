from Page import *
import alsaaudio
from xdo import Xdo

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

			if self.muted and self.volume != 0:
				self.mixer.setvolume(0)
			elif int(self.mixer.getvolume()[0]) != self.volume:
				self.mixer.setvolume(self.volume)

			if not self.muted:
				self.volume = int(self.mixer.getvolume()[0])

			if data["action"] == "getState":
				response["response"] = True
				response["volume"] = self.volume
				response["muted"] = self.muted
				return None;
			elif data["action"] == "buttonPress":
				response["response"] = True
				
				if data["button"] == "increaseVolume":
					self.volume += self.volumeStep
				elif data["button"] == "decreaseVolume":
					self.volume -= self.volumeStep
				elif data["button"] == "toggleMute":
					self.muted = not self.muted
				elif data["button"] == "togglePlayPause":
					xdo = Xdo()
					winID = xdo.get_active_window()
					xdo.send_keysequence_window(winID, "XF86AudioPlay")
				elif data["button"] == "skipNext":
					xdo = Xdo()
					winID = xdo.get_active_window()
					xdo.send_keysequence_window(winID, "XF86AudioNext")
				elif data["button"] == "skipPrev":
					xdo = Xdo()
					winID = xdo.get_active_window()
					xdo.send_keysequence_window(winID, "XF86AudioPrev")

				return None;
		response["response"] = False
		return None;

page = VolumeController()