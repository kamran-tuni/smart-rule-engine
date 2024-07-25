#!/bin/bash

source env/bin/activate

read -p "Enter your access token: " ACCESS_TOKEN
read -p "Enter the parameter name: " PARAMETER_NAME
read -p "Enter the parameter value: " PARAMETER_VALUE

mosquitto_pub -d -q 1 -h demo.thingsboard.io -p 1883 -t esp/telemetry -u "$ACCESS_TOKEN" -m "{\"$PARAMETER_NAME\":$PARAMETER_VALUE}"
