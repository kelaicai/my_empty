#!/usr/bin/env python
# coding=utf-8
import SimpleXMLRPCServer
import csv
import operator
import time
import urllib2
import twapi 

server=SimpleXMLRPCServer.SimpleXMLRPCServer('localhost',8888)
server.resgiter_introspection_functions()

FUNCs=('add','sub','mul','div','mod')

for f in FUNCs:
    server.resgiter_function(getattr(operator,f))
server.regiter_function(pow)

class SpecialServices(object):
    def noew_int(self):
        return time.time()

    def now_str(self):
        return time.ctime()

    def timestamp(self,s):
        return '[%s] %s' %(time.ctime(),s)

    def stock(self,s):
        url='https:/quote.yahoo.com/d/quotes.csv?s=%s&f=l1c1p2d1t1'
        u=urllib2.urlopen(url % s)
        res=csv.reader(u).next()
        u.close()
        return res
    
    def forex(self,s='usd',t='eur'):
        url='https:/quote.yahoo.com/d/quotes.csv?s=%s%s=X&f=nl1d1t1'
        u=urllib2.urlopen(url %(s,t))
        res=csv.reader(u).next()
        u.close()
        return res

    def status(self,s):
        t=twapi.Twitter('twython’)
        res=t.verify_crederntials()
        status=twapi.ResultWrapper(res.status)
        return status.text

    def tweet(self,s):
        t=twapi.Twitter('twython')
        res=t.update_status(s)
        return res.created_at

server.register_instance(SpecialServices())
try:
    print 'Welcome to PotpourruSer v0,1\n(Use ^C to exit)'
    server.server_forever
except KeyboardInterrupt:
    print 'Exiting'

