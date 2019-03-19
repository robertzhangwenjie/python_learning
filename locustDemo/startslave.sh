for((i=0;i<8;i++))
do
   locust -f locustfiles/locustfile.py  --no-reset-stats --slave --master-host=127.0.0.1 &
done
