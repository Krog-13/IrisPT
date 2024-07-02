# config.py file contains all the constants used in the project

BASE_URL = "http://83.97.77.248:3000"

ADMIN_CREDENTIAL = {
    "phoneNumber": "phone",
    "password": "password"
}

USER_CREDENTIAL = {"phoneNumber": "phone",
                     "password": "password"}
USERS_CREDENTIAL = [("phone", "password"),
                    ("11", "11"),
                    ("11", "11")]


endpoints = {"login": "/auth/login",
             "category": "/category",
             "product": "/product",
             "cart": "/cart",
             }
