import time
from datetime import datetime,timedelta
import logging
import sys
import math

if (len(sys.argv) < 2):
	exit
logging.warning(f'当前时间：{datetime.now()}')
target_time = sys.argv[1]
logging.warning(f'参数值：{target_time}')
now = datetime.now()
target_time = datetime.strptime(now.strftime("%Y-%m-%d ") + target_time, "%Y-%m-%d %H:%M:%S.%f")
logging.warning(f'目标时间：{target_time}')
if (datetime.now() < target_time):
	td = target_time - datetime.now()
	logging.warning(f'需要沉睡：{td.seconds}秒')
	time.sleep(td.seconds+math.floor(td.microseconds/1000)/1000)
logging.warning(f'当前时间：{datetime.now()}')
