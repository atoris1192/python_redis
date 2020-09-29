print("Hello python!!!")

import redis
# r = redis.Redis(host='redis', port=6379, db=0)

redis_pool = redis.ConnectionPool(host='redis', port=6379, db=0, max_connections=4)
conn = redis.StrictRedis(connection_pool=redis_pool)
# 値のset
conn.set('key01', 'value01')  # 成功するとTrueが返る

# 値のget
value = conn.get('key01')  # バイナリ値で取得

#print(type(value))
# <class 'bytes'>

#print(str(value, encoding='utf-8'))  # str()で変換
# 'value01'

print(conn.get("keyxx"))

conn.set('key01', 'new value')
print(conn.get('key01'))

conn.delete('key01')
conn.delete('key02','key03')
