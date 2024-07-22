#!/bin/bash

source env/bin/activate
python -m unittest core.tests.rule_engine.test_rule_engine
