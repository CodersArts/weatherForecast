# weatherForecast
A simple python web crawler to fetch weather forecast from http://www.weather-forecast.com

It requests the forecast for the city's name that is taken as input and replaces the <city> with the one entered
http://www.weather-forecast.com/locations/<city>/forecasts/latest

The source code of the requested webpage is decoded and string containing the forecast is searched, manipulated a little, and is displayed.
