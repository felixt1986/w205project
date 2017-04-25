#!/bin/bash

mkdir /data/project
mkdir /data/project/staging
mkdir /data/project/staging/mediadata

cd /data/project/staging
rm rows.csv
wget https://data.consumerfinance.gov/api/views/s6ew-h6mp/rows.csv 

cd /data/project/staging/mediadata
rm *.CSV
today=`date`
start_ts=$(date -d "2016-01-01" '+%s')
end_ts=$(date -d "$today" '+%s')
max=$(( ( end_ts - start_ts )/(60*60*24) ))
for ((i=2; i <=max; ++i))
do
    ONE=$i
    THEDATE=`date -d "$today - $ONE days" +%Y%m%d`
    wget 'http://data.gdeltproject.org/events/'$THEDATE'.export.CSV.zip'
    unzip $THEDATE'.export.CSV.zip'
done

cat *.CSV > finalmedia.CSV



