import basetest

from app import video

class VideoTest(basetest.BaseTest):

    """ create video interactions ie: create, find, create_many """
    def setUp(self):
        super(VideoTest, self).setUp()

        self.many_params = ( 
                {"title": "1", "duration": 93000, "pub": "Wed, 28 May 2014 21:00:31 +0000"},
                {"title": "2", "duration": 93000, "pub": "Wed, 28 May 2014 21:00:31 +0000"},
                {"title": "3", "duration": 93000, "pub": "Wed, 28 May 2014 21:00:31 +0000"},
        )


    def test_create(self):

        res_video = video.Video.create(**self.params)
        self.assertIsNotNone(res_video)
        self.assertEquals(res_video["title"], self.params["title"])
        self.assertEquals(str(res_video["published_at"]), self.params["pub"])
        self.assertEquals(int(res_video["duration"]), self.params["duration"])

    def test_create_many(self):

        try:
            insert = video.Video.create_many(self.many_params)
        except any as E:
            # kind of hacky ... but make sure no exception is thrown ...
            self.assertIsNotNone(None)


    def test_find(self):

        video_id = video.Video.create(**self.params)
        self.assertIsNone(video.Video.find(search="aaa"))
        self.assertIsNotNone(video.Video.find(search="test"))


    
