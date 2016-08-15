import requests
import json
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore

log = logging.getLogger(__name__)

class Client(object):
  """The propsd client

  Keyword Args:
    propsd_server (str): The server hostname/ip address (default localhost)
    propsd_port (int): The server port (default 9100)
  """
  def __init__(self, propsd_server='localhost', propsd_port=9100):
    self.propsd_server = propsd_server
    self.propsd_port = propsd_port
    self.__scheduler = BackgroundScheduler({
       'apscheduler.jobstores.default': {
           'class': 'apscheduler.jobstores.memory:MemoryJobStore',
       },
       'apscheduler.executors.default': {
          'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
          'max_workers': '1'
       },
       'apscheduler.job_defaults.coalesce': 'true',
       'apscheduler.job_defaults.max_instances': '1',
       'apscheduler.timezone': 'UTC',
    })

  """Gets a specific property

  Args:
    key (str): The key to retrieve

  Return:
    str: The property value, or None.
  """
  def get(self, key):
    try:
      response = requests.get("http://%s:%d/v1/conqueso/api/roles/default/properties/%s" % (self.propsd_server, self.propsd_port, key))
      return response.text
    except:
      log.warn("Could not retrieve property value")

  """Gets all propsd properties

  Return:
    dict: The complete propsd property set
  """
  def properties(self):
    try:
      response = requests.get("http://%s:%d/v1/properties" % (self.propsd_server, self.propsd_port))
      return json.loads(response.text)
    except:
      log.warn("Could not retrieve property value")

  """Gets the status of the propsd service

  Return:
    dict: A dictionary containing the status parameters.
  """
  def status(self):
    response = requests.get("http://%s:%d/v1/status" % (self.propsd_server, self.propsd_port))
    return json.loads(response.text)

  """Gets the health of the propsd service

  Return:
    dict: A dictionary containing the health parameters.
  """
  def health(self):
    response = requests.get("http://%s:%d/v1/health" % (self.propsd_server, self.propsd_port))
    return json.loads(response.text)