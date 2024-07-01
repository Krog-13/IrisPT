from locust import task, between, events, FastHttpUser, constant_throughput
from common.auth import get_user_token
from locust.runners import MasterRunner
import random
from collections.abc import Generator
from contextlib import contextmanager
from locust.contrib.fasthttp import RestResponseContextManager

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


class RestUserThatLooksAtErrors(FastHttpUser):
    abstract = True
    TOKEN = None

    @contextmanager
    def rest(self, method, url, **kwargs) -> Generator[RestResponseContextManager, None, None]:
        if not self.TOKEN:
            self.TOKEN = get_user_token(self.client)
        extra_headers = {"Authorization": f"Bearer {self.TOKEN}"}
        with super().rest(method, url, headers=extra_headers, **kwargs) as resp:
            if resp.js and "error" in resp.js and resp.js["error"] is not None:
                resp.failure(resp.js["error"])
            yield resp


class MyOtherRestUser(RestUserThatLooksAtErrors):
    # wait_time = between(0.5, 10)
    # wait_time = constant(180)  # be nice to postman-echo.com, and dont run this at scale.
    wait_time = constant_throughput(0.5)  # be nice to postman-echo.com, and dont run this at scale.

    @task
    def t(self):
        languages = ("EN", "RU", "KZ")
        random_language = random.choice(languages)
        with self.rest("PATCH", "/profile/18/change-language", json={"language": random_language}) as _resp:
            if _resp.js["lang"] != random_language:
                _resp.failure("Language was not changed")

    @task(2)
    def t1(self):
        with self.rest("GET", "/users/me/profile") as _resp:
            if _resp.js["phoneNumber"] != "7472010101":
                _resp.failure("Phone number is not what we expected")

        with self.rest("GET", "/profile/18") as _resp:
            if _resp.js["userId"] != 18:
                _resp.failure("Phone number is not what we expected")

    @task(3)
    def t2(self):
        for id in range(4, 7):
            with self.rest("GET", f"/category/{id}", name="/category") as _resp:
                if _resp.js["id"] != id:
                    _resp.failure("Phone number is not what we expected")

    @task(4)
    def t3(self):
        with self.rest("GET", "/order") as _resp:
            pass
        with self.rest("GET", "/model", json={"all": 1, "deal": 0}) as _resp:
            pass
