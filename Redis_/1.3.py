from redis import StrictRedis
import base64
from time import sleep

'''Redis List'''
redis = StrictRedis(host='localhost', port=6379, db=1, password=base64.b16decode(b'32373178756665692E'))
redis.flushdb()
# 队列的头插法
redis.lpush('zgl', 'zhou')
redis.lpush('zgl', 'guo')
redis.lpush('zgl', 'liang')
# 获取所有的元素
print(redis.lrange('zgl', 0, -1))
# 队列的尾插法
redis.rpush('zgl', 'hao')
redis.rpush('zgl', 'shuai')
print(redis.lrange('zgl', 0, -1))
# 移除操作
print(redis.lpop('zgl'))
print(redis.rpop('zgl'))
print(redis.lrange('zgl', 0, -1))
# 获取列表的长度
print(redis.llen('zgl'))
# 按照索引查找
print(redis.lindex('zgl', 0))
# 移除指定的数值，需要指定次数
print(redis.lrem('zgl', 1, 'hao'))
# 截取列表
redis.lpush('zgl', 'zhou')
redis.lpush('zgl', 'guo')
redis.lpush('zgl', 'liang')
print(redis.lrange('zgl', 0, -1))
# 会改变列表
print(redis.ltrim('zgl', 1, 4))
print(redis.lrange('zgl', 0, -1))
# 组合操作
print(redis.rpoplpush('zgl', 'list'))
print(redis.lrange('zgl', 0, -1))
print(redis.lrange('list', 0, -1))
# 在指定的位置赋值，超过索引会报错，不存在也是报错（替换，更新操作
redis.lset('zgl', 1, 'shabi')
print(redis.lrange('zgl', 0, -1))
# 无法在 key 中插入 key
redis.lset('zgl', 1, 'list')
print(redis.lrange('zgl', 0, -1))
# 在指定位置插入，有多个的时候，从左边第一个开始
redis.linsert('zgl', 'before', 'list', 'woshi')
redis.linsert('zgl', 'before', 'guo', 'woshi')
print(redis.lrange('zgl', 0, -1))
print(redis.dbsize())
'''总体操作和 Python 的列表操作差不多'''
