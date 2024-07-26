#!/bin/bash

source env/bin/activate
python backend/manage.py makemigrations tenant app
