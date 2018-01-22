#coding=utf-8
import MySQLdb
import os, sys,string
import ConfigParser

conn= MySQLdb.connect(
        host='192.168.1.5',
        port = 3306,
        user='root',
        passwd='root',
        db ='salt',
        charset='utf8'
        )

cur = conn.cursor()




def getMinionAlljobs(minionid):
	command = "select * from salt_returns where id = '"+minionid + "' order by alter_time "
        resultList=[]
	result = cur.execute(command)
        records = cur.fetchmany(result)
        for record in records:
            resultList.append(record[5])
        return resultList


#result = getMinionAlljobs('icms.openzwd.com')

#print result

cur.close()
