import sql
import psycopg2

from tables import Video as db

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
            RETURNING id, published_at
        """
        res = db.execute_with_results(query, values=(kw.get("title"), kw.get("duration"), kw.get("pub")) )
        # NOTE return id
        return res[0]

    @classmethod
    def create_many(self, videos):
        """ Create many videos with one transaction. Rollback if it fails. Assumes that videos is an array of dicts"""
        query = """insert into video
            (title, duration, published_at) 
            VALUES (%(title)s, %(duration)s, %(pub)s)
        """
        db.execute_many(query, value_dicts=videos)

    @classmethod
    def find(self, **kw):

        query = """SELECT set_limit(0.5); 
            SELECT title
            FROM video
            WHERE title %% %s
        """
        results = db.execute_with_results(query, values=(kw.get("search"),))
        if results:
            return results[0]
        return None

