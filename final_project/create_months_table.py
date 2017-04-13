import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import datetime


x={}
y={}
now = datetime.datetime.now()
month =now.month
year=now.year
while year >2015 :
    x.append(year & month)
    y.append(year & month-1)
print(year_month)
print(now.year)
