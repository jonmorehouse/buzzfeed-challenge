import xmltodict
import video

# NOTE this is called safely once validations are run on the kw
class VideoActions:

    @staticmethod
    def find(**kw):
        return video.Video.find(**kw)

    @staticmethod
    def create(**kw):

        return video.Video.create(**kw)

    @staticmethod
    def load_from_file(**kw):
    
        """ Parse xml file and load all videos accordingly """
        video_dicts = []
        with open(kw.get("filepath")) as r:
            
            xml = xmltodict.parse(r.read())
            for entry in xml["rss"]["channel"]["item"]:
                current_video = {
                    "title": entry["media:title"],
                    "duration": entry["media:content"][0]["@duration"],
                    "pub": entry["pubDate"]
                }
                video_dicts.append(current_video)
        
        video.Video.create_many(video_dicts)

