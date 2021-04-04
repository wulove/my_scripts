import time
from datetime import datetime, timedelta, timezone
import logging
import sys
import math

if (len(sys.argv) < 2):
	exit()
now = datetime.now()
zone_cn = timezone(timedelta(hours=8))
now_cn = now.astimezone(zone_cn)
logging.warning(f'服务器时间：{now}, 北京时间：{now_cn}')
logging.warning(f'参数值：{sys.argv[1]}')
target_time = datetime.strptime(now_cn.strftime("%Y-%m-%d ") + sys.argv[1], "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=zone_cn)
# 当前时间在设置时间前，则默认目标时间设置为第二天
if now_cn.strftime("%H:%M:%S.%f") > sys.argv[1]:
	target_time = target_time + timedelta(days=1)
logging.warning(f'目标时间：{target_time}')
td = target_time - now_cn
# 当目标时间与当前时间相差过大时，直接跳过
if td.seconds > 3600 * 2:
	logging.error('当前时间与目标时间相差过大，直接跳过')
	exit()
logging.warning(f'需要沉睡：{td.seconds}秒')
time.sleep(td.seconds+math.floor(td.microseconds/1000)/1000)
logging.warning(f'当前时间：{datetime.now()}')
