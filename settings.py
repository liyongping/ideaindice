#-*-coding:utf-8-*-

import os.path

DEBUG = True
LISTEN_PORT = 8080

# db settting
if DEBUG:
    DB_CONNECT_STRING = 'mysql://root:34497267@localhost:3306/ideaindice?charset=utf8'
else:
    #import sae.const
    #sae.const.MYSQL_DB      # 数据库名
    #sae.const.MYSQL_USER    # 用户名
    #sae.const.MYSQL_PASS    # 密码
    #sae.const.MYSQL_HOST    # 主库域名（可读写）
    #sae.const.MYSQL_PORT    # 端口，类型为，请根据框架要求自行转换为int
    #sae.const.MYSQL_HOST_S  # 从库域名（只读）
    DB_CONNECT_STRING = 'mysql://root:34497267@localhost:3306/ideaindice?charset=utf8'
    #DB_CONNECT_STRING = 'mysql://'+sae.const.MYSQL_USER+':'+sae.const.MYSQL_PASS+'@'+sae.const.MYSQL_HOST+':'+sae.const.MYSQL_PORT+'/'+sae.const.MYSQL_DB+'?charset=utf8'
DB_ECHO = False
DB_ENCODING = 'utf-8'
POOL_RECYCLE=5

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# 使用SAE Storage服务保存上传的附件，需在SAE管理面板创建
STORAGE_DOMAIN_NAME = 'upload' 

BASE_PATH = os.path.dirname(__file__)
# the address path which the file will be uploaded in
FILE_MANAGER_PATH = os.path.join(BASE_PATH, u"static/upload/")

# the app will use this template
CURRENT_TEMPLATE_NAME = "default"
