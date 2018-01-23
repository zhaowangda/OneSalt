import  salt.config

import salt.client

import etcdFun

master_config=salt.config.client_config('/etc/salt/master')

#print(master_config)



def runningCommand(hosts,module,scripts):
    saltObj=salt.client.LocalClient()
    ret=saltObj.run_job(hosts,module,[scripts,])
    return ret


def runningCommandOnline(hosts,module,scripts):
    saltObj=salt.client.LocalClient()
    ret=saltObj.cmd(hosts,module,[scripts,])
    return ret