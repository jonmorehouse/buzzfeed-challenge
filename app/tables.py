from sql import *
import psycopg2
import data_stores

# TODO convert this class to use method_missing for simplifying the loc to implement query_one, query_many etc...
class Video(object):

    """ Handle queries and setup of the Accounts table. Use classmethods only """

    @classmethod
    def create_if_not_exists(cls):

        # NOTE originally used BIT VARYING(128) for password hash
        create_table = """CREATE TABLE IF NOT EXISTS video (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            title text UNIQUE NOT NULL,
            duration decimal,
            published_at timestamp with time zone
            );
        """

        create_index = """CREATE INDEX IF NOT EXISTS
            title_index on video 
            USING gist (title gist_trgm_ops);
        """

        cls.execute(create_table)
        cls.execute(create_index)


    @classmethod
    def drop_if_exists(cls):
        return cls.execute("DROP TABLE IF EXISTS video")
    
    @classmethod
    def query_one(cls, query, **kw):
        return cls.execute_with_results(query, "fetchone", **kw)

    @classmethod
    def query_many(cls, query, **kw):
        return cls.execute_with_results(query, "fetchmany", **kw)

    @classmethod
    def query_all(cls, query, **kw):
        return cls.execute_with_results(query, "fetchall", **kw)

    @classmethod
    def execute(cls, query, **kw):
        """ Run a query ignoring the cursor results """
        cursor = data_stores.pg_conn.cursor()

        try:
            cursor.execute(query, kw.get("values"))
            data_stores.pg_conn.commit()
        except psycopg2.Error as e:
            data_stores.pg_conn.rollback()
            raise e

        cursor.close() 

    @classmethod
    def execute_with_results(cls, query, method_name = "fetchone", **kw):
        """ Execute a query with an optional to call on the cursor for grabbing results """
        cursor = data_stores.pg_conn.cursor()

        # NOTE do this on purpose to notify any tests of method_name which is invalid ...
        method = getattr(cursor, method_name)

        try:
            cursor.execute(query, kw.get("values"))
            results = method()
            data_stores.pg_conn.commit()
        except psycopg2.Error as e:
            results = False
            data_stores.pg_conn.rollback()
            raise e

        cursor.close()
        return results

    @classmethod
    def execute_many(cls, query, **kw):
        """ Run a many query """
        cursor = data_stores.pg_conn.cursor()

        try:
            cursor.executemany(query, kw.get("value_dicts"))
            data_stores.pg_conn.commit()
        except psycopg2.Error as e:
            data_stores.pg_conn.rollback()
            raise e

        cursor.close() 



