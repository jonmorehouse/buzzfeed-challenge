import sql
import psycopg2
from app_config import Config

import tables

class Video(object):

    @classmethod
    def create(self, **kw):
        """ Create a single video with one transaction/cursor """
        
        # to_timestamp('05 Dec 2000', 'DD Mon YYYY')
        # you don't need to cast the timestamp unless requirements change :)
        #VALUES (%s, %s, to_timestamp(%s, 'Dy, DD Month YYYY HH:MI:SS ))
        query = """insert into video
            (title, duration, published_at) 
            VALUES (%s, %s, %s) 
            RETURNING title, duration, published_at
        """
        res = tables.VideoTable.execute_with_results(query, values=(kw.get("title"), kw.get("duration"), kw.get("pub")) )
        return self._normalize_results(res)

    @classmethod
    def create_many(self, videos):
        """ Create many videos with one transaction. Rollback if it fails. Assumes that videos is an array of dicts"""
        query = """insert into video
            (title, duration, published_at) 
            VALUES (%(title)s, %(duration)s, %(pub)s)
        """
        for video in videos:
            self.create(**video)
        #tables.VideoTable.execute_many(query, value_dicts=videos)

    @classmethod
    def find(self, **kw):

        """ Note ... this uses the pg_trgm extension which indexes the text. We can switch the value later (this probably shouldn't be hardcoded)"""

        query = """ SELECT title, duration, published_at, title <-> %s AS similarity
            FROM video 
            WHERE similarity(title, %s)::numeric > 0.00
            ORDER BY similarity LIMIT 1
        """
        results = tables.VideoTable.execute_with_results(query, values=(kw.get("search"), kw.get("search")))
        if results:
            return self._normalize_results(results)
        return None

    @classmethod
    def _normalize_results(self, results):
        return {"title": results[0], "duration": str(results[1]), "published_at": results[2]}


