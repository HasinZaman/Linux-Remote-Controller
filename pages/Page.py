class Page():
	'''
	Page is an abstract class on the structure of Page python files
	'''
	def __init__(self):
		'''
		Constructor sets class name
		'''
		self.name = "Page"
		pass

	def validActionSource(self, pageName):
		'''
		validActionSource method checks if the source of the POST call is from the correct page

		paramaters:
			pageName (string): name of page name of source of post

		return:
			boolean of if pageName paramater is the same as instance name
		'''
		if self.name == None:
			raise Exception("")
		return pageName == self.name

	def action(self, data, response):
		'''
		action abstract method responds to POST from corresponding page source

		Paramaters:
			data (dictionary): Dictonary of json data sent by POST
			response (dictionary): dictionary of response that will be filled with output
		'''
		raise Exception("Unimplemented method")
