# config.py file contains all the constants used in the project

BASE_URL = "http://83.97.77.248:3000"

ADMIN_CREDENTIAL = {
    "phoneNumber": "7777777777",
    "password": "admin123"
}

USERS_CREDENTIAL = [("7777777777", "admin123"),
                    ("11", "11"),
                    ("11", "11")]


endpoints = {"login": "/auth/login",
             "category": "/category",
             "product": "/product",
             "cart": "/cart",
             }
