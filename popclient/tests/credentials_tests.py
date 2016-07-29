from popclient.lib.credentials import CreateAccount
import unittest


class TestCreateAccount(unittest.TestCase):
    def __init__(self):
        account = CreateAccount('/var/db/', 'mailaccount.db')
    def test_db_exists(self):
        if account.db_exists():
            assert True
        else:
            assert False
