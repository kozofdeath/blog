import os
from flask import Flask

app = Flask(__name__) # you need to do this first, as other modules are going to be using the app
config_path = os.environ.get("CONFIG_PATH", "blog.config.DevelopmentConfig") # trying to get an environment variable that will set path to our config path

app.config.from_object(config_path) # takes a string containing a file path, directory or class and uses the variables in the corresponding object to populate the config object; you can use different configurations for different environments

from . import views
from . import filters