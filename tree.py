import redis

r=redis.Redis(host='localhost',port=6379,db=0)

# to delete all the keys in currently connecting db
r.flushdb() 

# to delete all db
r.flushall()


r.hmset('tree',{'0':'123', '1':'345', '2':'678'})
b=r.hgetall('tree')
print(b)
# # print(type(b))
# # print(type(b['0']))
# print (b['0'])

r.hmset('nodes',{'img_id':'abc.jpg','id':'1'})
c=r.hgetall('nodes')
print(c)
print (c['id'])

# to delete the particular key
r.delete('nodes')

# to list all the keys 
print(r.scan())

# to print all the keys matching specified pattern
keys = r.scan_iter(match='aa*') 

#pipeline
# Use the pipeline() method to create a pipeline instance
pipe = r.pipeline()
# The following SET commands are buffered
pipe.set('bing', 'baz')
pipe.set('foo', 'bar')
pipe.get('bing')
# the EXECUTE call sends all buffered commands to the server, returning a list of responses, one for each command.
pipe.execute()


