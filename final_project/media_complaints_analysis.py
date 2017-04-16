import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extensions import AsIs

conn = psycopg2.connect(database="projectdatabase", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("create table complaints_media_analysis_201704 as SELECT c.year_month, c.cleaned_company, c.complaints_count, sum(m.numsources) as mentions, avg (avgtone) as sentiment FROM ccdata_y2017_update c join mediadata_2017_update m on c.year_month = m.monthyear WHERE (m.sourceurl like  lower('%'||c.cleaned_company||'%') AND c.year_month = '201704') GROUP BY c.year_month, c.cleaned_company, c.complaints_count order by c.complaints_count DESC")

cur.execute("create table complaints_media_analysis_Combined as select * from
(select * from complaints_media_analysis_201704 
union select * from complaints_media_analysis_201703 
union select * from complaints_media_analysis_201702
union select * from complaints_media_analysis_201701 
union select * from complaints_media_analysis_201612 
union select * from complaints_media_analysis_201611 
union select * from complaints_media_analysis_201610 
union select * from complaints_media_analysis_201609 
union select * from complaints_media_analysis_201608 
union select * from complaints_media_analysis_201607 
union select * from complaints_media_analysis_201606 
union select * from complaints_media_analysis_201605 
union select * from complaints_media_analysis_201604 
union select * from complaints_media_analysis_201603 
union select * from complaints_media_analysis_201602 
union select * from complaints_media_analysis_201601) u 
order by u.year_month;")

conn.commit()
cur.close()
conn.close()

