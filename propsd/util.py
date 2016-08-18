class PropsdDictionary(dict):
  """A dictionary backed by propsd

  This dictionary enables the use of a standard python dictionary
  that is backed by the propsd service. The dictionary must be
  refreshed by calling the refresh method.

  """

  def __init__(self, propsd_client):
    self.__propsd_client = propsd_client

  def refresh(self):
    """Refreshes the dictionary with properties from propsd
    """
    self.update(self.__propsd_client.properties())
