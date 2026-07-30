import os

API_KEY = os.getenv("API_KEY", "")


def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be 0")
    return a / b            #a/b


def login(username, password):
    expected_user = os.getenv("ADMIN_USER", "admin")
    expected_password = os.getenv("ADMIN_PASSWORD", "secret")

    return username == expected_user and password == expected_password