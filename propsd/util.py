class PropsdDictionary(dict):
	"""A dictionary backed by propsd
	"""

	def __init__(self, propsd_client):
		self.__propsd_client = propsd_client

	def refresh(self):
		self.update(self.__propsd_client.properties())
