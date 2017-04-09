# Weather Forecast

##Brief Overview
A simple python web crawler to fetch weather forecast from http://www.weather-forecast.com

##INSTALLATION
After downloading or cloning the repo, run `python setup.py install` or if you have different versions of python then `python3 setup.py install`

HOW IT WORKS
---

It requests the forecast for the city's name that is taken as input and replaces the 'city' with the one entered
http://www.weather-forecast.com/locations/'city'/forecasts/latest

The source code of the requested webpage is decoded and string containing the forecast is searched, manipulated a little, and is displayed.
