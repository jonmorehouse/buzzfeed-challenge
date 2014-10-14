import unittest
from flask.ext.testing import TestCase

from app.app import app
from app import data_stores
from app import tables

# setup flask app
class BaseTest(TestCase):

    def create_app(self):
        return app

    def setUp(self):
        tables.VideoTable.create_if_not_exists()
        self.params = {
                "title": "Test Title", 
                "duration": 940000,
                "pub": "Wed, 28 May 2014 21:00:31 +0000",
        }

    def tearDown(self):
        tables.VideoTable.drop_if_exists()


