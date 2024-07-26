#!/bin/bash

source env/bin/activate
python3 backend/manage.py create_tenant_superuser  --schema=public
