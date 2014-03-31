Diary
=====

*Diary* is simple diary web based application developed with Python, Flask, MongoDB and love.


## Get started!
First clone or [download](https://github.com/GruPy-RN/agenda_flask/archive/master.zip) this repository:

```sh
$ git clone git@github.com:GruPy-RN/agenda_flask.git
```

the next step is create a virtualenv to install all dependencies to:

```sh
$ cd agenda_flask
$ vritualenv --no-site-packages .venv
$ source .venv/bin/activate
```

once the virtualenv is created and activated, we can install all dependencies with pip:

```sh
$ pip install -r requirements
```

Don't forget to set the `MONGO_URI` environment variable like so:

```sh
$ export MONGO_URI='mongodb://username:password@host:27017/diary'
```

Now, start the server and have fun!

```sh
$ python manage.py runserver
```
