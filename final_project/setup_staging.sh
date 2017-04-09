#!/bin/bash

mkdir /data/project
mkdir /data/project/staging
cd /data/project/staging
rm rows.csv
wget https://data.consumerfinance.gov/api/views/s6ew-h6mp/rows.csv 
wget http://data.gdeltproject.org/events/20170407.export.CSV.zip
