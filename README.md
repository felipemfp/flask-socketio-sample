# Flask and Socket.IO Sample

A really simple sample that show how to use [Flask](http://flask.pocoo.org/) and [Socket.IO](https://socket.io/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

Make sure that you have [Python 3.x](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installing/) and [git](https://help.github.com/articles/set-up-git/) installed.

### Installing

You have to clone this repository (or you can [download a .zip](https://github.com/felipemfp/flask-socketio-sample/archive/master.zip))

```
git clone https://github.com/felipemfp/flask-socketio-sample.git
```

Now you have to install all [requirements](requirements.txt). Note that I'm using [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) to make cross-origin requests possible, so it's a opcional requirement if you don't need that.

```
cd flask-socketio-sample
pip install -r requirements.txt
```

After that, you should be able to start the app

```
python app.py
```

## Deployment

It is already able to be deployed on Heroku. Read more about how to deploy [here](https://flask-socketio.readthedocs.io/en/latest/#deployment).

## Built With

* [Flask](http://flask.pocoo.org/)
* [Socket.IO](https://socket.io/)
* [Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

## Contributing

I just want to keep it simple, but you can fork and do whatever you want.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
