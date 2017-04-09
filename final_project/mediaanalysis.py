from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

cur.close()
conn.close()


conn = psycopg2.connect(database="projectdatabase", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("CREATE TABLE mediadata2 AS SELECT
monthyear,
numsources, 
actor1geo_countrycode, 
Actor2Geo_countryCode, 
ActionGeo_countryCode, 
sourceurl,
avgtone
FROM mediadata
WHERE (
actor1geo_countrycode = 'US' OR 
Actor2Geo_countryCode = 'US' OR
ActionGeo_countryCode ='US'") 

cur.close()
conn.close()
