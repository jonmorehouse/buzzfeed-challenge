import basetest
import json

class AppTest(basetest.BaseTest):

    def setUp(self):

        super(AppTest, self).setUp()
        self.headers = {'Content-Type': 'application/json'}


    def test_create(self):
        
        res = self.client.post("/video/guess", data=json.dumps(self.params), headers=self.headers)
        self.assertEquals(res.status_code, 201)

    def test_create_duplicate(self):

        res = False
        for i in range(2):
            res = self.client.post("/video/guess", data=json.dumps(self.params), headers=self.headers)
        
        self.assertEquals(res.status_code, 400)

    def test_create_missing_param(self):
        
        del self.params["title"]
        res = self.client.post("/video/guess", data=json.dumps(self.params), headers=self.headers)
        self.assertEquals(res.status_code, 400)

    def test_create_nonjson(self):

        res = self.client.post("/video/guess", data=json.dumps(self.params), headers={})
        self.assertEquals(res.status_code, 400)

    def test_find_video(self):
        """ This is pretty thoroughly tested otherplaces, just need to check status code""" 
        self.client.post("/video/guess", data=json.dumps(self.params), headers=self.headers)
        res = self.client.get("/video/guess/%s" % self.params.get("title"))
        self.assertEquals(res.status_code, 200)

