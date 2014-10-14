import basetest
from app.action_handler import action_handler
import os

class ActionHandlerTest(basetest.BaseTest):

    def setUp(self):

        super(ActionHandlerTest, self).setUp()
        self.filepath = os.path.join(os.path.dirname(__file__), "fixtures", "videos.xml")

    def test_load_from_file(self):

        action_handler("load_from_file", filepath = self.filepath)

        pass


    def test_find(self):

        action_handler("load_from_file", filepath = self.filepath) # load all items in first
        #action_handler("find", title = "title")

        pass

    
    def test_create(self):

        pass

