# Voltaic API
The back-end Django application served at api.voltaic.io.

## Requirements
1. Python 3.4

## Setup
Create venv:
```
$ cd && mkdir .venv && cd .venv
$ pyvenv-3.4 voltaic
$ source ./voltaic/bin/activate
```

Clone the repo and install requirements:
```
$ git clone https://github.com/voltaicio/voltaic_api.git
$ cd voltaic_api
$ pip install -r requirements.txt
```

Create /voltaic_api/api/conf.py:
```
CONF = {"VOLTAIC_SECRET_KEY": "<your_secret_key_here>"}
```

Build the project:
```
$ ./bin/do build
```
