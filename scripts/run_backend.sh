#!/bin/bash

source env/bin/activate
python backend/manage.py runserver 0.0.0.0:8000
