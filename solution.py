#!/usr/bin/env python

import getopt, sys

from app import app_config
from app import app # primary app
from app import action_handler # action handle controls 
from app import tables # handles all table actions

def initialize_database():
    tables.VideoTable.create_if_not_exists()

def load_videos():
    action_handler.action_handler("load_from_file", filepath="videos.xml")

def start_server():
    app.app.run(port = int(app_config.Config.PORT))

if __name__ == '__main__':

    opts, args = getopt.getopt(sys.argv[1:], "ho:v")

    if "init_db" in args:
        initialize_database()

    if "fill_db" in args:
        load_videos()

    if "match_unknowns" in args:
        start_server()
