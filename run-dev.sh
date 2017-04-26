#!/bin/bash
# simple script to run django commands local with dev setting
source venv/bin/activate
python manage.py $1 $2 $3 $4 --settings=BrightnessMonitorWeb.settings.dev