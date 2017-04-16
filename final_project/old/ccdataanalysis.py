import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="projectdatabase", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("create table ccdata_2015on_update as select EXTRACT(YEAR from date_received) || to_char(EXTRACT(Month from date_received), '00') as year_month, company, Null as cleaned_company from ccdata where date_received >= '01/01/2015'")

cur.execute("ALTER TABLE ccdata_2015on_update alter column cleaned_company type text")

cur.execute("update ccdata_2015on_update Set year_month = regexp_replace(year_month, ' ', '', 'g')")

cur.execute("update ccdata_2015on_update Set cleaned_company = regexp_replace(company, ',', '', 'g')")
cur.execute("update ccdata_2015on_update Set cleaned_company = regexp_replace(cleaned_company, ' ', '-', 'g')")

cur.execute("create table ccdata_2015on_update2 as select year_month, company, cleaned_company, count(company) as complaints_count from ccdata_2015on_update group by year_month, company, cleaned_company order by year_month DESC, complaints_count DESC"
)
conn.commit()
cur.close()
conn.close()
