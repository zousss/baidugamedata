import os
import time
import datetime

while 1:
    h = 0
    cur_time = time.localtime(time.time())
    time.sleep(300)
    if h == cur_time.tm_hour:
        print "***current time is %s,spider start!***" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        os.system('scrapy crawl baidugameSpider')
        print "***current time is %s,spider waiting!***" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())