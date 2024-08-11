#!/bin/bash

source env/bin/activate
python -m unittest core.tests.usecases.rule_engine.test_rule_engine
python -m unittest core.tests.usecases.iot_platform.test_iot_platform
