# WEATHER FORECAST

BRIEF OVERVIEW
---
A simple python web crawler to fetch weather forecast from http://www.weather-forecast.com

INSTALLATION
---
After downloading or cloning the repo, Navigate to the directory containing the files and double click on **setup.py** or run `python setup.py install` or if you have different versions of python then `python3 setup.py install` to install the dependencies.

HOW IT WORKS
---

It requests the forecast for the city's name that is taken as input and replaces 'city' in url with the one entered
http://www.weather-forecast.com/locations/'city'/forecasts/latest

The source code of the requested webpage is decoded and `<div>` containing the forecast string is searched, manipulated a little, and is displayed.


BUGS
---
If the name of the city is misspelled, there will be an error.
