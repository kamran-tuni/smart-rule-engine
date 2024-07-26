#!/bin/bash

source env/bin/activate
python backend/manage.py migrate_schemas
