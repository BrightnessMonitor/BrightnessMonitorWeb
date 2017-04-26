#!/bin/bash

# set SECRET_KEY
heroku config:set SECRET_KEY=22222222222

# set DJANGO_SETTINGS_MODULE
heroku config:set DJANGO_SETTINGS_MODULE=BrightnessMonitorWeb.settings.production

# set WEB_CONCURRENCY
heroku config:set WEB_CONCURRENCY=2

# disable collectstatic
heroku config:set DISABLE_COLLECTSTATIC=1