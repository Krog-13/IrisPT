from locust import HttpUser, task, between
from common.auth import get_token
import time


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

    @task
    def get_cart(self):
        self.client.get("/cart")

    def on_start(self):
        self.token = get_token(self.client)
        self.client.headers = {'Authorization': f'Bearer {self.token}'}
