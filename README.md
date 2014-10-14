# BuzzFeed Code Challenge

## API Endpoints

### /video/guess [POST] -> PLAINTEXT

* post to create a new video with parameters similar to: 
  {
  }

#### Considerations

* handling duplicate title names
* normalizing title names. Cleansing data and escaping data before inserting it
  * this is handled by psycopg database

### /video/guess/TITLE [GET] -> PLAINTEXT

* return the closets match based upon the title that is passed in

#### Considerations

* how to query for the title names
* for now, lets use the "%like%" feature of Postgresql
* in the future, could use elastic search to query against titles for a larger data set and with more finetuned options for matching

## Setup

proper environment variables set in `.env`. Note that `$CONTAINER_HOST` and `$APP_HOST` refer to the location of Docker.

### Development 
~~~ sh
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt -r dev_requirements.txt

# set up postgres server
$ fig up -d postgres

~~~

### Deployment

~~~ sh

# start application running on port 8000 on your docker container host
$ fig up -d
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

## ToDo

1. Restructure code base so that modules are nested into packages. There should be a video package and a package that contains shared logic across the application

2. Switch PsycoPG2 to use a connection pool

3. Add in further tests for video_test (ie: check bad video, check bad video in create_many method etc)




