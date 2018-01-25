# WEATHER FORECAST

A simple python web crawler to fetch [weather forecast](http://www.weather-forecast.com)

## Getting Started

### Installation

After downloading or cloning the repo, Navigate to the directory containing the files and double click on **setup.py** or run 
```python setup.py install```
or if you have different versions of python then 
```python3 setup.py install``` 
to install the dependencies.

### HOW IT WORKS

It prompts to enter a city name to get the forecast for and requests the forecast for the city's name that is taken as input and replaces 'city' in url with the one entered
http://www.weather-forecast.com/locations/<city_name_entered>/forecasts/latest

The source code of the requested webpage is decoded and `<div>` containing the forecast string is searched, manipulated a little, fomatted and is displayed.

## Built With

1. Python 3.4
2. re

## Contributing

1. Fork it
2. Create your feature branch: git checkout -b my-new-feature
3. Commit your changes: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Submit a pull request

## Authors

+ Muhammad Ali Zia

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/the-javapocalypse/weatherForecast/blob/master/License.txt) file for details
