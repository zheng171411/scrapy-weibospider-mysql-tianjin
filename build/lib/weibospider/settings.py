# -*- coding: utf-8 -*-

# Scrapy settings for weibospider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibospider'

SPIDER_MODULES = ['weibospider.spiders']
NEWSPIDER_MODULE = 'weibospider.spiders'
ITEM_PIPELINES={#'weibospider.pipelines.WeibospiderPipeline':300}
                'weibospider.user_imagepipelines.UserImagesPipeline':400, 
                'weibospider.pipelines.WeibospiderPipeline':300
               }
#Mysql数据库配置
MYSQL_HOST = '10.1.46.170'
MYSQL_DBNAME = 'cauc_microblog'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root123'

#Oracle数据库配置
#ORACLE_DSN = '10.1.46.170/orcl'
#ORACLE_USER = 'bupt'       #'ZTQ'
#ORACLE_PASSWD = 'bupt'     #'fnl12345678'

#蚂蚁代理配置
#APPKEY = "153754507"
#SECRET = "a24846208df1fa61dc23c87d3fbc38fe"
#SERVERIP = "123.56.251.212:8123" #蚂蚁代理服务器地址

#微博爬取内容配置
USER_NAME = '18600299007'   #'13920979915'   #'18600299007'
#PASS_WORD = '19911007'      #'wangjie42685' #'19911007'
#PAGE_NUM = 1   #爬取微博内容页面数


#图片下载配置
#IMAGES_STORE = '/home/hadoop_user/scrapy-weibospider/weibospider/userphoto'  #图片存储位置
IMAGES_STORE = '/home/cauc/workspace/cauc_microblog/WebContent/resources/images/userphoto'  #图片存储位置
IMAGES_EXPIRES = 90          #图片失效期限天数
IMAGES_THUMBS = {'small':(40,40)}  #设置图片缩略图长度和宽度

#cookie失效期限设置，单位为秒
EXPIRES = 345600 #4天

#请求超时时间设置
REQUEST_TIMEOUT = 5
#日志log配置文件
#LOG_ENABLED = False

#User-Agent 或代理IP轮换
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

PROXIES = [
    {'ip_port': '43.241.237.4:808', 'user_pass': None},
    #{'ip_port': '101.200.215.7:808', 'user_pass': None},
    #{'ip_port': '101.200.147.205:808', 'user_pass': None},
] 


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibospider (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10 

RETRY_TIMES = 2
RETRY_HTTP_CODES = [400,403,408,500,502,503,504] #遇到此Http code时进行重新请求，重新请求次数为RETRY_TIMES参数值
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False
#COOKIES_DEBUG=True
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'weibospider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'weibospider.middlewares.RotateUserAgent': 1,  #动态随机设置UserAgent
    'weibospider.middlewares.RotateHttpProxy': None, #100, #动态代理IP设置
    'weibospider.middlewares.MayiHttpProxy': None, #100, #蚂蚁动态代理IP设置
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None  #110
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'weibospider.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
