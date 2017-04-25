import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


conn = psycopg2.connect(database="projectdatabase", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("CREATE TABLE mediadata_2016_update AS SELECT monthyear, numsources, sourceurl, avgtone FROM mediadata WHERE (actor1geo_countrycode = 'US' OR Actor2Geo_countryCode = 'US' AND year='2016')")
cur.execute("create index monthyear ON mediadata_2016_update(monthyear)")

cur.execute("CREATE TABLE mediadata_2017_update AS SELECT monthyear, numsources, sourceurl, avgtone FROM mediadata WHERE (actor1geo_countrycode = 'US' OR Actor2Geo_countryCode = 'US' AND year='2017')")
cur.execute("create index monthyear ON mediadata_2017_update(monthyear)")

conn.commit()
cur.close()
conn.close()
