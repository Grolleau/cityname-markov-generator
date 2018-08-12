#!/bin/bash

python generator.py -n 1000 | sort | uniq > towns.csv
