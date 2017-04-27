import psycopg2

conn = psycopg2.connect(database="projectdatabase", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

a="drop table if exists complaints_media_analysis_"


cur.execute(a+'Equifax')
cur.execute("create table complaints_media_analysis_Equifax as select * from  complaints_media_analysis_combined where cleaned_company ='Equifax' order by year_month DESC")

cur.execute(a+'Experian')
cur.execute("create table complaints_media_analysis_Experian as select * from  complaints_media_analysis_combined where cleaned_company ='Experian' order by year_month DESC")

cur.execute(a+'Transunion')
cur.execute("create table complaints_media_analysis_Transunion as select * from  complaints_media_analysis_combined where cleaned_company = 'Transunion' order by year_month DESC")

cur.execute(a+'WellFargo')
cur.execute("create table complaints_media_analysis_WellFargo as select * from  complaints_media_analysis_combined where cleaned_company = 'Wells-Fargo' order by year_month DESC")

cur.execute(a+'BoA')
cur.execute("create table complaints_media_analysis_BoA as select * from  complaints_media_analysis_combined where cleaned_company = 'Bank-of-America' order by year_month DESC")

cur.execute(a+'JPM')
cur.execute("create table complaints_media_analysis_JPM as select * from  complaints_media_analysis_combined where cleaned_company ='JPMorgan' order by year_month DESC")

conn.commit()
cur.close()
conn.close()
