# Job Track

Have you ever been overwhelmed by the sheer number of positions you have applied
to, which one was which, is the person emailing you back from a top 10 company
or a bottom 5 company?

Job searching can take a long time, you might apply to a position and finally hear
back from the company six months later or a day later. You never know what
you're going to get and its challenging to stay organized.

I'm building Job Track to help take care of that. Let's keep you organized and
on top of your job search.

## Technology

* Django
* Selenium
* More to come

## Installation

Clone this repo and start a new virtualenv with python3.

`$ pip install -r requirements.txt`

You'll need to create a user and database in Postgres

```
$ createuser -d jobtrack -P
Enter password for new role: jobtrack
Enter it again: jobtrack
$ createdb -O jobtrack jobtrack
```

And then try to run it!

`$ python manage.py runserver`


### Authors

Jasen Carroll  
Oct 19th, 2015  
jasen.c@icloud.com
