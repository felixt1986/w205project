import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="projectdatabase", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("create table ccdata_2015on_update as select EXTRACT(YEAR from date_received) || to_char(EXTRACT(Month from date_received), '00') as year_month, company as cleaned_company, count(company) as complaints_count from ccdata where date_received >= '01/01/2015' group by year_month, cleaned_company order by complaints_count DESC")

cur.execute("ALTER TABLE ccdata_2015on_update alter column cleaned_company type text")
cur.execute("update ccdata_2015on_update Set year_month = regexp_replace(year_month, ' ', '', 'g')")

cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'TransUnion Intermediate Holdings, Inc.', 'Transunion', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'Wells Fargo & Company', 'Wells-Fargo', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'JPMorgan Chase & Co.', 'JPMorgan', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'Nationstar Mortgage', 'Nationstar', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'Navient Solutions, LLC.', 'Navient', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'Synchrony Financial', 'Synchrony', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'U.S. Bancorp', 'Bancorp', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'Ditech Financial LLC', 'Ditech', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'Encore Capital Group', 'Encore Capital', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'PNC Bank N.A.', 'PNC Bank', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'Portfolio Recovery Associates, Inc.', 'Portfolio Recovery', 'g')")
cur.execute("update ccdata_2015on_update set cleaned_company = regexp_replace(cleaned_company, 'Select Portfolio Servicing, Inc', 'Select Portfolio', 'g')")
cur.execute("update ccdata_2015on_update Set cleaned_company = regexp_replace(cleaned_company, ' ', '-', 'g')")
cur.execute("update ccdata_2015on_update Set cleaned_company = regexp_replace(cleaned_company, '[.,]', '', 'gi')")
cur.execute("create index year_month ON ccdata_2015on_update(year_month)")


cur.execute("create table ccdata_Y2015_update as select * from ccdata_2015on_update where year_month BETWEEN '201501' AND '201512'")
cur.execute("create table ccdata_Y2016_update as select * from ccdata_2015on_update where year_month BETWEEN '201601' AND '201612'")
cur.execute("create table ccdata_Y2017_update as select * from ccdata_2015on_update where year_month BETWEEN '201701' AND '201712'")

cur.close()
conn.close()
