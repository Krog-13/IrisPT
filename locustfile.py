from locust import HttpUser, task, between, events
from common.auth import get_admin_token, get_user_token
from locust.runners import MasterRunner
import time

import logging
from http.client import HTTPConnection

# HTTPConnection.debuglevel = 1
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.ERROR)
# requests_log.propagate = False


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    if isinstance(environment.runner, MasterRunner):
        print("I'm on master node")
    else:
        print("I'm on a worker or standalone node")

class QuickstartUser(HttpUser):
    wait_time = between(2, 5)

    @task
    def view_items_1(self):
        self.client.get("/")

    @task(3)
    def get_category(self):
        self.client.get("/category")

    @task
    def view_product(self):
        for item_id in range(1, 10):
            self.client.get(f"/product/{item_id}", name="/productchik") # name групировка запросовconstant_pacing
            time.sleep(1)



    @task(4)
    def view_category(self):
        with self.client.get('/category/4/', catch_response=True) as response:
            if response.json()["id"] == 4:
                response.success()
            else:
                response.failure("Don't exist id")


    def on_start(self):
        self.token = get_user_token(self.client)
        self.client.headers = {'Authorization': f'Bearer {self.token}'}

    def on_stop(self):
        print("Stop Locust")
        pass
