#!/bin/bash

#starting postres
/data/start_postgres.sh


#Change to the w205 user
su - w205


#switching to data
cd /data

 
#creating project directories
mkdir /data/project

mkdir /data/project/staging

#navigating to staging directory
cd /data/project/staging


#downloading data from consumer financial protection bureau
wget https://data.consumerfinance.gov/api/views/s6ew-h6mp/rows.csv 

#Connecting to the PostgreSQL instance: Log into postgres as the postgres user:

psql -U postgres



#Create a database:
create database projectdatabase;

#Connect to the database:
\c projectdatabase

#create the table with cc data
CREATE TABLE ccdata(
  Date_received date ,Product varchar(200) ,Sub_product varchar(200) ,Issue varchar(400) ,Sub_issue varchar(400) ,Consumer_complaint_narrative text ,Company_public_response text ,Company varchar(200) ,State varchar(2) ,ZIP_code varchar(5) ,Tags varchar(200) ,Consumer_consent_provided varchar(200) ,Submitted_via varchar(100) ,Date_sent_to_company date ,Company_response_to_consumer varchar(200) ,Timely_response varchar(10) ,Consumer_disputed varchar(10) ,Complaint_ID bigint  ); 

#truncate ccdata table
truncate ccdata;

#load data into ccdata table
COPY ccdata FROM '/data/project/staging/rows.csv' WITH DELIMITER ',' CSV HEADER;


#testing ccdata table
select * from ccdata limit 10;



