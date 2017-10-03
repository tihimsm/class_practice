class Prism:
	def _init_(self, width, height, depth):
		self.width = width
		self.height = height
		self.depth = depth
	def content(self):
		return self.width* self.height* self.depth
		