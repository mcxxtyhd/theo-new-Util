from redisPackage.ReServer import RedisServer
from utils.EncryptUtils import pyhashlibMd5, pyEOR

# print(str(pyEOR(71593504,14131300)))


# 初始化redis连接
redis = RedisServer()
print(redis.getValue(75628546))
