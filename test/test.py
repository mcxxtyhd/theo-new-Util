# #创建redis链接对象
# r = redisPackage.Redis(host='127.0.0.1',port=6379,decode_responses=True)
#
# # #存储键值对
# # r.set('site','qqqqq')
#
# # #获取值
# print('这是结果')
# print(r.get('site'))
from redisPackage.ReServer import RedisServer

# RedisServer.testprint()
rserver=RedisServer()
print(rserver.getValue('12098860'))



