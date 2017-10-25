import redis
r=redis.Redis(host='localhost',port=6379,db=0)
# d = {'0':123, '1':'345', '2':'678'}
# print(type(d['0']))
r.flushall()
r.hmset('tree',{'0':'123', '1':'345', '2':'678'})
b=r.hgetall('tree')
print(b)
# print(type(b))
# print(type(b['0']))
print (b['0'])

r.hmset('nodes',{'img_id':'abc.jpg','id':'1'})
c=r.hgetall('nodes')
print(c)
print (c['id'])
