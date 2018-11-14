#!/usr/bin/env python
# coding=utf-8
from atexit import register
from random import randrange
from threading import Thread,currentThread,Lock
from time import sleep,ctime

lock=Lock()
class CleanOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)
    
loops=(randrange(2,5) for x in xrange(randrange(3,7)))

remaining=CleanOutputSet()

def loop(nsec):
    myname=currentThread().name
    lock.acquire()
    remaining.add(myname)
    print '[%s] Started %s ' %(ctime(),myname)
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print '[%s] Compledted %s (%d secs)' %(ctime(),myname,nsec)
    print 'remainning :%s' %(remaining or 'NONE')
    lock.release()
def main():
    for pause in loops:
        Thread(target=loop,args=(pause,)).start()

    @register
    def _atexit():
        print 'all Done! at',ctime()
        

if __name__=='__main__':
   print 'remaining is :',remaining
   main()
