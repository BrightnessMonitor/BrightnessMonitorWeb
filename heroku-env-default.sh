#!/bin/bash

# log into python env
source env/bin/activate

# set SECRET_KEY
heroku config:set SECRET_KEY=22222222222

# set DJANGO_SETTINGS_MODULE
heroku config:set DJANGO_SETTINGS_MODULE=BrightnessMonitorWeb.settings.production