import requests
import json
#etcdServer = "192.168.1.5:2379"
#etcdServerUrl = "http://" + etcdServer +"/version"
#print etcdServerUrl
#=====================================================================================
#get etcd server version



def getEtcdVersion(etcdServerIp="127.0.0.1",etcdPort="2379"):
	"""example: getEtcdVersion("192.168.1.5","2379")"""

	etcdServerUrl = "http://" + etcdServerIp+":"+etcdPort +"/version"
	response = requests.get(etcdServerUrl)
	dictResult = json.loads(response.text)
	#print "etcd server Version : %s" % dict1.get('etcdserver')
	#print "etcd cluster Version : %s" % dict1.get('etcdcluster')
	return dictResult.get('etcdserver') #just return etcdServer version


	"""
	etcdVersion = getEtcdVersion("192.168.1.5","2379")
	print etcdVersion
	#print getEtcdVersion.__doc__
	"""
#---------------------------------------------------------------------
#read etcd key

def readEtcdDir(etcdServerIp="127.0.0.1",etcdPort="2379",path="/"):
	etcdServerUrl = "http://" + etcdServerIp+":"+etcdPort +"/v2/keys"+path
	try:
		response = requests.get(etcdServerUrl)
	except (IOError ,ZeroDivisionError),e:
			pass
	dictResult = json.loads(response.text)
	return dictResult


"""
result = readEtcdDir("192.168.1.5","2379","/")

if result.get('errorCode'):
	print result
else:
	print result

#print result
#print result.get('node').get('dir')
"""
#---------------------------------------------------------------------

def operateEtcdDir(etcdServerIp="127.0.0.1",etcdPort="2379",path="/",type="create|delete"):
	""" create or delete etcd dir !
	exp: 
		operateEtcdDir("192.168.1.5","2379","/dir1","create")
		operateEtcdDir("192.168.1.5","2379","/dir1","delete")
		print operateEtcdDir.__doc__
	"""
	etcdServerUrl = "http://" + etcdServerIp+":"+etcdPort +"/v2/keys"+path
	if type == "create":
		response = requests.put(etcdServerUrl,params={'dir':'true'})
		dictResult = json.loads(response.text)
		return dictResult
	elif type == "delete":
		response = requests.delete(etcdServerUrl,params={'dir':'true'})
		dictResult = json.loads(response.text)
		return dictResult

"""
response = createEtcdDir("192.168.1.5","2379","/dir1","delete")
print response

"""
#---------------------------------------------------------------------

def operateEtcdKey(etcdServerIp="127.0.0.1",etcdPort="2379",path="/",keyValue="",type="get|create|set|delete"):
	"""
	operate etcd keys: return dict object
		operateEtcdKey("192.168.1.5","2379","/key1","testkeyss","create")
		operateEtcdKey("192.168.1.5","2379","/key1","testkeyss","set")
		operateEtcdKey("192.168.1.5","2379","/key1","testkeyss","get")
		operateEtcdKey("192.168.1.5","2379","/key1","testkeyss","delete")
		print operateEtcdKey.__doc__
	"""
	etcdServerUrl = "http://" + etcdServerIp+":"+etcdPort +"/v2/keys"+path
	if type == "get":
		response = requests.get(etcdServerUrl)
		dictResult = json.loads(response.text)
		return dictResult
	elif type == "create" or type == "set":
		response = requests.put(etcdServerUrl,params={'value': keyValue })
		dictResult = json.loads(response.text)
		return dictResult
	elif type == "delete":
		response = requests.delete(etcdServerUrl)
		dictResult = json.loads(response.text)
		return dictResult
"""
operateEtcdKey("192.168.1.5","2379","/key1","testkeyss","create")
operateEtcdKey("192.168.1.5","2379","/key1","testkeyss","set")
operateEtcdKey("192.168.1.5","2379","/key1","testkeyss","get")
operateEtcdKey("192.168.1.5","2379","/key1","testkeyss","delete")
"""
#---------------------------------------------------------------------

