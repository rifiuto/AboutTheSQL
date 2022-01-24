from redis import StrictRedis
import base64
from time import sleep

'''Redis Hash: Hash 本质和 String 没有区别，只是用 name 指定 hash 表格'''
redis = StrictRedis(host='localhost', port=6379, db=1, password=base64.b16decode(b'32373178756665692E'))
redis.hset('zgl', 'name', 'zhouguoliang')
redis.hmset('zgl', {'age': 12, 'height': 170})
print(redis.hgetall('zgl'))
# 获取长度，返回的 Hash 表的 key 的个数
print(redis.hlen('zgl'))
# 区别于 String 多了一个 hvals hgetall
print(redis.hvals('zgl'))
print(redis.hkeys('zgl'))
print(redis.hgetall('zgl'))
for item in redis.hkeys('zgl'):
    print(f"the value of {item.decode('utf8')} is {redis.hget('zgl', item).decode('utf8')}, type is {type(item)}")
print("-" * 50)
print(redis.hincrby('zgl', 'age', 10))
for item in redis.hkeys('zgl'):
    print(f"the value of {item.decode('utf8')} is {redis.hget('zgl', item).decode('utf8')}, type is {type(item)}")
'''用于用户信息的保存，适合变动的，对象用 Hash'''
