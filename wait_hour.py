import time
from datetime import datetime,timedelta
import logging
import sys
import math

if (len(sys.argv) < 2):
	exit()
now = datetime.now()
logging.warning(f'当前时间：{now}')
target_hour = 0
hour = now.hour
for i in range(1, len(sys.argv)):
	if (hour < int(sys.argv[i])):
		target_hour = int(sys.argv[i])
		break
if target_hour == 0:
	logging.error(f'木有匹配到对应的参数: {sys.argv[1:]}')
	exit()
logging.warning(f'匹配到的参数为: {target_hour}')

if target_hour == 24:
	target_hour = 0
target_time = datetime(now.year, now.month, now.day, target_hour)
if target_hour == 0:
	target_time = target_time + timedelta(days=1)
logging.warning(f'当前时间: {now}, 目标时间: {target_time}')
	
td = target_time - now
if td.seconds > 3600:
	logging.error('时间差大于1小时，退出')
	exit()
logging.warning(f'需要沉睡：{td.seconds}秒')
wait = td.seconds+math.floor(td.microseconds/1000)/1000
time.sleep(wait)
logging.warning(f'当前时间：{datetime.now()}')