from locust import HttpUser, task, between, events
from common.auth import get_admin_token
from locust.runners import MasterRunner
import time

import logging
from http.client import HTTPConnection


class QuickAdminUser(HttpUser):
    wait_time = between(2, 10)

    def on_start(self) -> None:
        self.token = get_admin_token(self.client)
        self.client.headers = {'Authorization': f'Bearer {self.token}'}

    def on_stop(self):
        print("Stop Locust")

    @task
    def get_lotoday(self):
        self.client.get("/lotoday")

    @task
    def view_globalconfig(self):
        self.client.get("/globalConfig")

    @task
    def view_prizes(self):
        self.client.get("/prize/all")

    @task(3)
    def get_cart(self):
        self.client.get("/globalConfig")
