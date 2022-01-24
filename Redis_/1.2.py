from redis import StrictRedis
import base64
from time import sleep

'''Redis String'''
redis = StrictRedis(host='localhost', port=6379, db=1, password=base64.b16decode(b'32373178756665692E'))

redis.set('name', 'zhouguoliang')
redis.append('name', 'haoshuai')
# 先获取再设置
print(redis.getset('name', 'queshi'))
print(redis.get('name'))
# 如果不存在直接就是创建
# redis.append('age', '2')

print(redis.get('age'))
print(redis.type('age'))
if redis.exists('height'):
    redis.get('height')
else:
    redis.set('height', 180)
    print(redis.get('height'))
print(redis.keys('*'))
# 添加 10 岁
redis.incrby('age', 10)
print(redis.get('age'))
# 获取长度
redis.strlen('age')
# redis 中截取和 Python 非常的相似啊
print(redis.substr('age', 1, -1))
# 没了划不来
redis.setex('name', 1, 'haohao')
sleep(1)
redis.get('name')

print(redis.keys('*'))
redis.setex('name1', 1, '2')
print(redis.keys('*'))
sleep(1)
print(redis.keys('*'))
redis.set('mykey', '1')
# 不存在则设置，设置成功返回 True, 否则是 False
print(redis.setnx('mykey', 'faa'))
# redis 中使用的是 shell 的通配符，不是正则表达式
print(redis.keys('user:{1, 3}'))