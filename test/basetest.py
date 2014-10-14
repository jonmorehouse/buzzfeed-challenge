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
        tables.Video.create_if_not_exists()

    def tearDown(self):
        tables.Video.drop_if_exists()


