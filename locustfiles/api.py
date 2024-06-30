from locust import HttpUser, task, between, events
from common.auth import get_token
from locust.runners import MasterRunner
import time

import logging
from http.client import HTTPConnection

HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")