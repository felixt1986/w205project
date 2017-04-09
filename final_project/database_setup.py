import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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



conn.commit()

cur.close()
conn.close()
