today=`date`
start_ts=$(date -d "2013-04-01" '+%s')
end_ts=$(date -d "$today" '+%s')
max=$(( ( end_ts - start_ts )/(60*60*24) ))
for ((i=1; i <=max; ++i))
do
    ONE=$i
    THEDATE=`date -d "$today - $ONE days" +%Y%m%d`
    output='http://data.gdeltproject.org/events/'$THEDATE'.export.CSV.zip'
    echo $output
done
