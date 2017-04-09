from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Weather Forecast',
    version='1.1.0',

    description='A simple web-crawler in python to fetch weather forecast',
    long_description=long_description,


    url='https://github.com/the-javapocalypse/weatherForecast',


    author='Muhammad Ali Zia',
    author_email='muhammad.17ali@gmail.com',


    classifiers=[

        'Development Status :: 4 - Beta',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],


    keywords='webcrawler weatherforecast webscrapper',


    install_requires=['re','urllib'],

   
)
