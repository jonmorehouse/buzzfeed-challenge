import unittest
from mock import patch
from flask.ext.testing import TestCase

from app.app import app
from app.tables import Account
from app.data_stores import pg_conn
from app.data_stores import redis_conn
from app import activation

# setup flask app
class BaseTest(TestCase):

    def create_app(self):
        return app

    def setUp(self):
        Account.create_if_not_exists()
        self.params = {
            "password": "mypass",
            "username": "jon",
            "phone_number": "5134107771"
        }

    def tearDown(self):
        Account.drop_if_exists()

    def signup(self, activate = True):

        with patch.object(activation.Activation, 'send_sms', return_value=None):
            # NOTE create account and activate it
            self.account_id = self.client.post("/account", data=self.params).json["account_id"]
            self.activation_code = redis_conn.hget("activation", self.account_id)

            if activate:
                print "ACTIVATED"
                self.client.put("/account/%s/activate" % self.account_id, data = {"code": self.activation_code})


