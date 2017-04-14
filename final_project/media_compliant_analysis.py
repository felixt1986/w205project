import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


conn = psycopg2.connect(database="projectdatabase", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("Create table media_compliant_analysis as SELECT c.year_month, c.cleaned_company, c.complaints_count, avg(m.avgtone) AS sentiment FROM ccdata_monthly c join mediadata2 m ON (c.year_month = m.monthyear) GROUP BY c.year_month, c.cleaned_company, c.complaints_count ORDER BY c.year_month DESC")
cur.execute("create index title_index2 On ccdata_monthly (year_month)")
cur.execute("create index title_index1 On mediadata2 (monthyear)")
conn.commit()
cur.close()
conn.close()

