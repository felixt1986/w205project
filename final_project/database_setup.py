
# Connect to the database
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
#conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#cur = conn.cursor()
#cur.execute("CREATE DATABASE projectdatabase")
#cur.close()
#conn.close()


conn = psycopg2.connect(database="projectdatabase", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

#cur.execute('''CREATE TABLE ccdata
#       (Date_received date ,Product varchar(200) ,Sub_product varchar(200) ,Issue varchar(400) ,Sub_issue varchar(400) ,Consumer_complaint_narrative text ,Company_public_response text ,Company varchar(200) ,State varchar(2) ,ZIP_code varchar(5) ,Tags varchar(200) ,Consumer_consent_provided varchar(200) ,Submitted_via varchar(100) ,Date_sent_to_company date ,Company_response_to_consumer varchar(200) ,Timely_response varchar(10) ,Consumer_disputed varchar(10) ,Complaint_ID bigint);''')
#cur.execute("truncate ccdata;")
#cur.execute("COPY ccdata FROM '/data/project/staging/rows.csv' WITH DELIMITER ',' CSV HEADER;")


cur.execute('''CREATE TABLE mediadata
       (GlobalEventID varchar(200), Day varchar(200), MonthYear varchar(200), Year varchar(200), FractionDate varchar(200), Actor1Code varchar(200), Actor1Name varchar(200), Actor1CountryCode varchar(200), Actor1KnownGroupcode varchar(200), Actor1EthnicCode varchar(200), Actor1Region1Code varchar(200), Actor1Religion2Code varchar(200), Actor1Type1Code varchar(200), Actor1Type2Code varchar(200), Actor1Type3Code varchar(200), Actor2Code varchar(200), Actor2Name varchar(200), Actor2CountryCode varchar(200), Actor2KnownGroupcode varchar(200), Actor2EthnicCode varchar(200), Actor2Region1Code varchar(200), Actor2Religion2Code varchar(200), Actor2Type1Code varchar(200), Actor2Type2Code varchar(200), Actor2Type3Code varchar(200), IsRootEvent int, EventCode varchar(200), EventBaseCode varchar(200), EventRootCode varchar(200), QuadClass varchar(200), GoldsteignScale varchar(200),NumMentions int, NumSources int, NumArticles int, AvgTone real, Actor1Geo_type int, Actor1Geo_fullname varchar(200), Actor1Geo_countrycode varchar(200), Actor1Geo_ADM1Code varchar(200), Actor1Geo_lat varchar(200), Actor1Geo_long varchar(200), Actor1Geo_FeatureID varchar(200), Actor2Geo_type varchar(200), Actor2Geo_fullname varchar(200), Actor2Geo_countrycode varchar(200), Actor2Geo_ADM1Code varchar(200), Actor2Geo_lat varchar(200), Actor2Geo_long varchar(200), Actor2Geo_FeatureID varchar(200), ActionGeo_type varchar(200), ActionGeo_fullname varchar(200), ActionGeo_countrycode varchar(200), ActionGeo_ADM1Code varchar(200), ActionGeo_lat varchar(200), ActionGeo_long varchar(200), ActionGeo_FeatureID varchar(200), Dateadded varchar(200), sourceurl varchar(400));''')

cur.execute("truncate mediadata;")

cur.execute("COPY mediadata FROM '/data/project/staging/mediadata/finalmedia.CSV' WITH DELIMITER '\t' csv NULL AS 'null';")

conn.commit()
cur.close()
conn.close()
