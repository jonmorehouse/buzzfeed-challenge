# BuzzFeed Code Challenge


## Overview

I put a 4 hour hard time limit on this project for myself. I attempted to build the basis of a professional api that could be maintained and extended beyond the requirements of this project. I purposely used flask and some low level postgres queries, to keep things as simple and fluid as possible. By exposing a module called `action_handler` I created some metaprogramming based responses to handle actions `create, find, process_file`. These action_handler methods were called from the api and the solutions.py file to solve the challenges at hand and meet requirements.

I wrote some minor tests, just to help the process of building this project go faster. I plan on extending the tests to get more unit test coverage. As of now, the app has been tested manually and with the 

I decided to use a postgres module called pg_trgm (popular text search index) to handle text search. This is not only highly efficient but fairly accurate and easy to maintain, its also something I haven't used before so that was a good experience. 

The entire development environment is created and managed with docker. By running `fig up -d postgres` you can start a docker container running postgres and can connect to it by setting the correct environment variables. All configuration is done via the environment and you can find defaults to get set up properly in the `.env` file. 

## Setup

proper environment variables set in `.env`. Note that `$CONTAINER_HOST` and `$APP_HOST` refer to the location of Docker.

### Prerequisites

##### Setup docker

Install docker (assumes you are using mac)
~~~ sh
# set up docker and export docker environment variables
$ brew install docker-osx # if you aren't running docker already
$ docker-osx start
$ eval `docker-osx env`
~~~

##### Setup Environment

Use my bashenv script to load the environment in just a few keystrokes :)
~~~ sh
# install bashenv
$ brew tap jonmorehouse/tap
$ brew update
$ brew install bashenv

# export environment as declared in .env file
$ \. bashenv .env
~~~

### Testing Requirements

~~~ sh
$ ./solution.py init_db load_db match_unknowns
~~~

### Development 

Start application for testing 
~~~ sh
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt -r dev_requirements.txt

# set up postgres server
$ fig up -d postgres

# run test suite
$ python -m unittest discover test '_test.py'
~~~


## Design Approach

1. I approached this project as if I was building out a production app to display some of my api design skills and how I approach building an api that should be maintained and easily workable by many developers

2. I prefer to let the database do as much work for me. Note, I could have written out a text comparator function for checking closest matches, but I used "like" from postgresql for an easy, one off solution. If I were building something like this to work at the scale of BuzzFeed, I would most likely use ElasticSearch or write a service to compare titles and generate results based upon the requirements of my team.

3. I modularized a lot of things to make extensibility of this api easier. For instance, I moved all of my query execution logic to the "Video" table which I declare in app/tables.py

4. I implemented method_missing to help make things more extensible. This is something I do in almost all of my python projects because it gives me a lot of control over various classes. In this case, I used method_missing for validations so that I could write a generic validation script to handle all validation logic for the "VideoActions" class.

5. I chose to include a primary id that uses uuid_generation for the id for each video entry. I could have used auto_increment but that would have made things harder if we ever sharded this postgres cluster. By using uuid I also would argue that you could use that as an external uuid or resource identifier if you ever wanted to expose an api for looking up videos by id.

6. All cleansing and escaping of sql information is performed by using Psychopg for injecting information. This is a best practice in the python community that I'm adhering to here.

7. I handle all exceptions at the flask level. If any method throws an exception, then the flask handler will return a json representation of that. I'm going to change that to plaintext when I get achance to dig a little deeper into the flask api docs. I've only used flask for json before this

8. I'd like to move all validation logic for file completeness/validity to the video_validations_method. This brings about a few unique challenges as I want to avoid reading a file twice and I'd like to be cognizant of memory (ie: I dont want to pass the file contents back)

9. I'm building this inherently synchronous from teh start. If I need to scale this up, I would approach the problem by either using parallel docker containers to run the app or gevent.

10. On all file insertions, we assume that one failed insertino means the file has been compromised and therefore no videos will be inserted. This is for safety and predictability.

11. I'm directly inserting the publication date string into the query and letting postgresql convert it for me. Any bad sql statements will be caught by pscyopg and this will err if there is a bad date that looks safe, making the transaction safe and atomic

12. I'm using pg_trgm to do a levenstein match based search for titles. This involves querying an index which is created in tables.py

13. I'd like to consider moving all the table statements to procs on the database server, but for now, its pretty nice to have them in tables

14. Store published_at as a string each time. This is more cpu efficient and saves us having to create a time string representation from the timestamp value from Postgres. Ideally, this should change in the future but because of project requirements, this hack works pretty well :)

15. For loading in multiple videos at once, we assume that no validation needs to be done to ensure there's a maximum. For now, the project requirements lead us to assume that only 100 at any given time would be inserted (based upon page 1 of 12 limit 100/page message on top of videos.xml page). If this requirement changes, we can easily change the video_actions logic to encompass this

## ToDo

1. Restructure code base so that modules are nested into packages. There should be a video package and a package that contains shared logic across the application

2. Switch PsycoPG2 to use a connection pool

3. Add in further tests for video_test (ie: check bad video, check bad video in create_many method etc)

4. clean up video_router logic. Move flask response handlers into a module or their own function


