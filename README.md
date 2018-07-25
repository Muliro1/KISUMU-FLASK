# KISUMU-FLASK-DIARY-APP
[![Build Status](https://travis-ci.org/Muliro1/KISUMU-FLASK.svg?branch=ft-Routes-159099006)](https://travis-ci.org/Muliro1/KISUMU-FLASK)   <a href="https://codeclimate.com/github/codeclimate/codeclimate/test_coverage"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage" /></a> [![Coverage Status](https://coveralls.io/repos/github/Muliro1/KISUMU-FLASK/badge.svg)](https://coveralls.io/github/Muliro1/KISUMU-FLASK)

This is a set of API endpoints with various functionality
clone the repository
```
https://github.com/Muliro1/KISUMU-FLASK
```
install virtualenv
```
python -m pip install virtualenv
```
cd into the directory and create a virtual environment like so
```
virtualenv venv
```
activate the virtualenv with
```
venv\Scripts\activate remember s is caps
```

install requirements.txt file and flask
```
python -m pip install flask

```
open command prompt and type:
```
python routes.py
```
open postman and type these links
```
GET http://localhost:5000/api/v1/entries
Get http://localhost:5000/api/v1/entries/<int:id>
POST http://localhost:5000/api/v1/entries/create_entry
DELETE http://localhost:5000/api/v1/entries/delete_entry/<int:id>
```
Ensure that when posting data the the create_entry url, it has all the required data ie
```
title, content, date, time, data_id
