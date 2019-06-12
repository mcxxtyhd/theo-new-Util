
import redis


class RedisServer:

    def __init__(self):
        # 创建连接池
        self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
        # 创建链接对象
        self.r = redis.Redis(connection_pool=self.pool)

    # 获得 值
    def getValue(self,key):
        return self.r.get(str(key).strip())

    # 设置 值
    def setValue(self, key,value):
        return self.r.set(str(key).strip(),str(value).strip())