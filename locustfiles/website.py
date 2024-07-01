from locust import HttpUser, task, between, events
from common.auth import get_admin_token
from locust.runners import MasterRunner
import time

import logging
from http.client import HTTPConnection


class QuickAdminUser(HttpUser):
    wait_time = between(2, 5)

    def on_start(self) -> None:
        self.token = get_admin_token(self.client)
        self.client.headers = {'Authorization': f'Bearer {self.token}'}

    def on_stop(self):
        print("Stop Locust")

    @task
    def view_items_1(self):
        self.client.get("/")