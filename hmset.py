import cPickle   
import time           
from rediscluster import StrictRedisCluster
startup_nodes = [{"host": "127.0.0.1", "port": "7000"}]
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=False)

f = open("/home/smacar-user/Downloads/db.pckl","rb")   
mydict = cPickle.load(f)       
f.close()                    
home=time.time()
for key in mydict:
	field_list=list(range(0,len(mydict[key])))
	val_list=mydict[key].tolist()
	data=dict(zip(field_list,val_list))
	rc.hmset(str(key),data)
	print("end time:",time.time()-home)
	break

