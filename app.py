import os

API_KEY = os.getenv("API_KEY", "")


def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be 0")
    return a / b            #a/b


def login(username, password):
    expected_user = os.getenv("ADMIN_USER")
    expected_password = os.getenv("ADMIN_PASSWORD")

    if not expected_user or not expected_password:   #aaaa
        return False

    return username == expected_user and password == expected_password