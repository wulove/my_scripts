import time
from datetime import datetime,timedelta
import logging
import sys
import math

if (len(sys.argv) < 2):
	exit()
now = datetime.now()
zone_cn = timezone(timedelta(hours=8))
now_cn = now.astimezone(zone_cn)
logging.warning(f'服务器时间：{now}, 北京时间：{now_cn}')
target_time = sys.argv[1]
logging.warning(f'参数值：{target_time}')
target_time = datetime.strptime(now_cn.strftime("%Y-%m-%d ") + target_time, "%Y-%m-%d %H:%M:%S.%f")
logging.warning(f'目标时间：{target_time}')
if (now_cn < target_time):
	td = target_time - now_cn
	logging.warning(f'需要沉睡：{td.seconds}秒')
	time.sleep(td.seconds+math.floor(td.microseconds/1000)/1000)
logging.warning(f'当前时间：{datetime.now()}')
