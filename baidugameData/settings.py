# -*- coding: utf-8 -*-

# Scrapy settings for baidugameData project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random
BOT_NAME = 'baidugameData'

SPIDER_MODULES = ['baidugameData.spiders']
NEWSPIDER_MODULE = 'baidugameData.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baidugameData (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
def getCookie():
    cookie_list = [
        'BAIDUID=848C3717E3FACC7F6ED185AA8DB74EB0:FG=1; BIDUPSID=848C3717E3FACC7F6ED185AA8DB74EB0; PSTM=1490853140; MCITY=-179%3A; BDSFRCVID=Hi-sJeC62rOJXHRiYVEgbcq1Je2bPL6TH6aIiAwl4K-Id_FnbAlhEG0PtU8g0Ku-LSPSogKKKgOTHI6P; H_BDCLCKID_SF=tRk8oI-XJCvjD4-k247Hhn8thmT22-usbKcdQhcH0hOWsIOjj53xMqF-X-5vB6JXBmOmLbcH3tt5eDbxDUC0j6ObjaDJJ6njK67eQn7-bTrVhn3GhITjhPrMDJOlbMT-0bFHQq7FypnCjfTHyMjD-noLyx_H5qOrJHn7_JjY2ljbDKboqfrfBUKH-4QQaUQxtNRJ-CnjtpvhKqRb0hbobUPUyUJ9LUvAJH4E_DtyJILMhDvx-Jb5K-4X52TLJ-bta-o2WbCQWnIVqpcNLTDKKx4pW-7Nalcp3Cva3-DhWJKKHxJsjlO1j4_PMtQf2T3iHm5bMhQ8KqjSjh5jDh3M3jksD-Rtex7gLN7y0hvcWb3cShnVjl00-nDSHH_JJToP; pgv_pvi=6967550976; pgv_si=s600247296; BD_CK_SAM=1; PSINO=5; H_PS_PSSID=1460_21123_17001_22159; BD_UPN=12314353; H_PS_645EC=6f19bU9UkGL7tktTgpfDY2ey0xgXZLJehih3gZgqR6hcgGh0wKJg2M4seqo; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'
    ]
    cookie = random.choice(cookie_list)
    return cookie

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch, br",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
    'Cookie':'%s' % getCookie()
}

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'baidugameData.middlewares.BaidugamedataSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'baidugameData.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'baidugameData.pipelines.BaidugamedataPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# start MySQL database configure setting
MYSQL_HOST = '192.168.112.47'
MYSQL_DBNAME = 'spiderdata'
MYSQL_USER = 'zoujianwei'
MYSQL_PASSWD = 'KPhUIEd2t622uwtB1xtZ'
# end of MySQL database configure setting