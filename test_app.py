import os
import unittest

from app import divide, login


class TestApp(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_login_with_valid_credentials(self):
        os.environ["ADMIN_USER"] = "admin"
        os.environ["ADMIN_PASSWORD"] = "secret"
        self.assertTrue(login("admin", "secret"))

    def test_login_with_invalid_credentials(self):
        os.environ["ADMIN_USER"] = "admin"
        os.environ["ADMIN_PASSWORD"] = "secret"
        self.assertFalse(login("admin", "wrong"))

    def test_login_without_configured_env_returns_false(self):
        os.environ.pop("ADMIN_USER", None)
        os.environ.pop("ADMIN_PASSWORD", None)
        self.assertFalse(login("admin", "secret"))


if __name__ == "__main__":
    unittest.main()
