from Page import *

class page1(Page):
	def __init__(self):
		self.name = "Page1"
	def action(self, data, server):
		if self.validActionSource(data["page"]):
			print("active")
			if data["action"] == "a":
				print("a")
				return [True]
		return [False]

page = page1()