#!/bin/bash

source env/bin/activate
celery -A task_manager worker -l info
