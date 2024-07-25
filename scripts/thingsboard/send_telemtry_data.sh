#!/bin/bash

source env/bin/activate
mosquitto_pub -d -q 1 -h demo.thingsboard.io -p 1883 -t esp/telemetry -u "WvamlBFvRGYgGsM7VN1u" -m "{temperature:21}"