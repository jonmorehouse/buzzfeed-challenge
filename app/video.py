import sql
import psycopg2

from tables import Video as db

class Video(object):

    pass

    #def __init__(self, **kw):

        #self.account_id = kw.get("account_id")
        #self.table = sql.Table("accounts")

    #""" Account is the backing for creating, retrieving, and removing accounts """
    #def signup(self, **kw):

        #form = kw.get("form")

        ## NOTE create the user
        #query = """insert into accounts
            #(phone_number, username, password_hash)
            #VALUES (%s, %s, crypt(%s, gen_salt('md5')))
            #RETURNING id, phone_number, username
            #"""
        #values = (form.get("phone_number"), form.get("username"), "some_password")
        #try:
            #result = db.query_one(query, values = values)
        #except psycopg2.Error as e:
            #raise e
            #return False

        ## NOTE pull apart the result tuple and trigger a new "activation"
        #self.account_id = account_id = result[0]
        #phone_number = result[1]
        #username = result[2]

        #activation.Activation(account_id = account_id).trigger(phone_number = phone_number)
        #return {"account_id": account_id, "username": username}

    #def login(self, **kw):

        #pass

    #def logout(self, **kw):

        #pass

    #def activate(self):
        #self._execute_activation_change(True)

    #def deactivate(self):
        #self._execute_activation_change(False)

    #""" PROTECTED METHODS """
    #def _execute_activation_change(self, value):
        #query = """UPDATE accounts
            #SET activated = %s
            #WHERE account_id = %s
            #RETURNING id, username
        #"""
        #values = (value, self.account_id)
        #try:
            #result = db.query_one(query, values = values)
        #except psycopg.Error as e:
            #raise e
            #return False

        #account_id = result[0]
        #username = result[1]
        #return {"account_id": account_id, "username": username}



