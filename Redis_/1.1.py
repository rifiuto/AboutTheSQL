from redis import StrictRedis
import base64
from time import sleep
'''Redis Keys'''
redis = StrictRedis(host='localhost', port=6379, db=0, password=base64.b16decode(b'32373178756665692E'))
redis.set('name', 'zhouguoliang')
print(redis.get('name'))
print(redis.ttl('name'))
print(redis.dbsize())
print(redis.keys('*'))
redis.expire('name', 10)
for i in range(10):
    print(redis.ttl('name'))
    sleep(1)

