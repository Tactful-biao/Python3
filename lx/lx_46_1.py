#!/usr/bin/env python3

# 练习：
# 假设你获取了用户输入的日期和时间如2017-5-3 16:34:30，以及一个时区信息如
# UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

import re
from datetime import datetime,timedelta,timezone

def to_timestamp(dt_str,tz_str):
    # 正则表达式匹配+或者- 时 分
    utc = re.match(r'^[UTC|utc]{3}([\+\-]+)(\d+):(\d{2})$',tz_str)
    # str转成detatime
    time = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    # 设置时区为0
    time_utc = time.replace(tzinfo=timezone.utc)
    # 根据 + - 设置时区
    # 时间戳是按0时区当前时间算，所以+7区的当前时间要减去时间差算出当前0时区时间
    if utc.group(1)=='+':
        dt = time_utc - timedelta(hours = int(utc.group(2)),minutes = int(utc.group(3)))
    elif utc.group(1)=='-':
        dt = time_utc + timedelta(hours = int(utc.group(2)),minutes = int(utc.group(3)))
    return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('Pass')
