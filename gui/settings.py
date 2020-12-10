################ Database-Backed Settings ################
# settings in this section are synced with the DB

# dSIPRouter settings
# dSIPRouter will need to be restarted for any changes to take effect - except for Teleblock settings
# unless hot reloading settings is enabled when updating settings, see shared.updateConfig()

DSIP_ID = 1
DSIP_CLUSTER_ID = 1
DSIP_CLUSTER_SYNC = False
DSIP_PROTO = 'https'
DSIP_PORT = '5000'
DSIP_USERNAME = 'admin'
DSIP_PASSWORD = b'8b6024af48f57058846d3ba24d3ec68050c0941c4ec6a06e67c6aad124da505c6e97160d63fb911b144f1afad53d656635a91ed0d48f06bd874ff1b48049a2f88bd12b2358fff518e45dee577cb9c607d58d3b0f2bc112b0ac34c30663d16f78f16e7f5a03c01bd4a8df00bc28e00019180a11875cf464ed52d2eb175e4788bc'
DSIP_API_TOKEN = b'2f757123fbe899fbf386548b75634e949a7790f1ee7b7fac7a469ee127e841a4db8dc79c9c2c334241bf3d1f81d6dd6db4bb513e4c4916f921212e242ca647f6e4a33505246e1719e656125c977a9dfb'
DSIP_API_PROTO = 'https'
DSIP_API_PORT = 5000
DSIP_PRIV_KEY = '/etc/dsiprouter/privkey'
DSIP_PID_FILE = '/var/run/dsiprouter/dsiprouter.pid'
DSIP_UNIX_SOCK = '/var/run/dsiprouter/dsiprouter.sock'
DSIP_IPC_SOCK = '/var/run/dsiprouter/ipc.sock'
DSIP_IPC_PASS = b'd06038ac3ac211199be45e90310c9eed8e321f981a6f1ea4d562e29ef77a6b63430ceab08b3ebfa9cce4660cd11a915239732740f932b5b5888243c051929fd30b7fa071d22b46cae8d2940138df6a18'
# dsiprouter logging settings
# syslog level and facility values based on:
# <http://www.nightmare.com/squirl/python-ext/misc/syslog.py>

DSIP_LOG_LEVEL = 3
DSIP_LOG_FACILITY = 18

# dSIPRouter SSL settings
# ssl key / cert are absolute paths
# email for re-certification must match certs
DSIP_SSL_KEY = '/etc/dsiprouter/certs/dsiprouter.key'
DSIP_SSL_CERT = '/etc/dsiprouter/certs/dsiprouter.crt'
DSIP_SSL_EMAIL = 'admin@VI-Update'
DSIP_CERTS_DIR = '/etc/dsiprouter/certs'

# dSIPRouter internal settings

VERSION = '0.64'
DEBUG = False
# '' (default)  = handle inbound with domain mapping from endpoints, inbound from carriers and outbound to carriers
# 'outbound'    = act as an outbound proxy only (no domain routing)
# 'inout'       = inbound from carriers and outbound to carriers only (no domain routing)
ROLE = ''
GUI_INACTIVE_TIMEOUT = 20

# MySQL settings for kamailio

# Database cluster
#KAM_DB_HOST = ['64.129.84.11','64.129.84.12','50.237.20.11','50.237.20.12']
# Single Host
KAM_DB_HOST = 'localhost'
# Database Engine Driver to connect with (leave empty for default)
# supported drivers:    mysqldb | pymysql
# see sqlalchemy docs for more info: <https://docs.sqlalchemy.org/en/latest/core/engines.html>
KAM_DB_DRIVER = ''
KAM_DB_TYPE = 'mysql'
KAM_DB_PORT = '3306'
KAM_DB_NAME = 'kamailio'
KAM_DB_USER = 'kamailio'
KAM_DB_PASS = b'd418827a9e48be90097cba6244cd65b4a71f872c653e1c6b0bc160f4cc9ba416f80746df3b8e4d6fa2ca4633d0c1b8267b8012fcf12f0adb44ee9082459c2d1e2f6a5e35a7315405801dd5147b068eab'

KAM_KAMCMD_PATH = '/usr/sbin/kamcmd'
KAM_CFG_PATH = '/etc/kamailio/kamailio.cfg'
KAM_TLSCFG_PATH = '/etc/kamailio/tls.cfg'
RTP_CFG_PATH = '/etc/kamailio/kamailio.cfg'

# SQLAlchemy Settings

# Will disable modification tracking
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_SQL_DEBUG = False

# These constants shouldn't be modified
# FLT_CARRIER/FLT_PBX:          type in dr_gateway table
# FLT_OUTBOUND/FLT_INBOUND:     groupid in dr_rules table
# FLT_LCR_MIN/FLT_FWD_MIN:      range of groupid in dr_rules table
FLT_CARRIER = 8
FLT_PBX = 9
FLT_MSTEAMS = 17
FLT_OUTBOUND = 8000
FLT_INBOUND = 9000
FLT_LCR_MIN = 10000
FLT_FWD_MIN = 20000

# The domain used to create user accounts for PBX and Endpoint registrations
DOMAIN = 'sip.dsiprouter.org'

# Teleblock Settings
TELEBLOCK_GW_ENABLED = 0
TELEBLOCK_GW_IP = '62.34.24.22'
TELEBLOCK_GW_PORT = '5066'
TELEBLOCK_MEDIA_IP = ''
TELEBLOCK_MEDIA_PORT = ''

# Flowroute API Settings
FLOWROUTE_ACCESS_KEY = ''
FLOWROUTE_SECRET_KEY = ''
FLOWROUTE_API_ROOT_URL = 'https://api.flowroute.com/v2'

# updated dynamically! These values will be overwritten
INTERNAL_IP_ADDR = '67.205.140.139'
INTERNAL_IP_NET = '67.205.140.*'
EXTERNAL_IP_ADDR = '67.205.140.139'
EXTERNAL_FQDN = 'sip.dsiprouter.org'

# upload folder for files
UPLOAD_FOLDER = '/tmp'

# Cloud Platform
# The cloud platform the dSIPRouter is installed on
# The installer will update this
# '' = other or native install
# AWS = Amazon Web Services, GCP = Google Cloud Platform, AZURE = Microsoft Azure, DO = Digital Ocean, VULTR = Vultr Cloud
CLOUD_PLATFORM = 'DO'

# email server config
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_ASCII_ATTACHMENTS = False
MAIL_DEFAULT_SENDER = 'dSIPRouter 1-1 <>'.format(str(DSIP_CLUSTER_ID), str(DSIP_ID), MAIL_USERNAME)
MAIL_DEFAULT_SUBJECT = 'dSIPRouter System Notification'

# backup settings
BACKUP_FOLDER = '/var/backups/dsiprouter'
################# End DB-Backed Settings #################

################# Local-Only Settings ####################
# settings in this section are not stored on the DB

# where the project was installed
DSIP_PROJECT_DIR = '/opt/dsiprouter'
# where the dsip docs are served from
DSIP_DOCS_DIR = '/opt/dsiprouter/docs/build/html'

# dr_routing prefix matching supported characters
# refer to: <https://kamailio.org/docs/modules/5.1.x/modules/drouting.html#idp26708356>
DID_PREFIX_ALLOWED_CHARS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '#', '*'}

# micosoft teams settings
MSTEAMS_DNS_ENDPOINTS = ["sip.pstnhub.microsoft.com:5061;transport=tls","sip2.pstnhub.microsoft.com:5061;transport=tls","sip3.pstnhub.microsoft.com:5061;transport=tls"]
MSTEAMS_IP_ENDPOINTS = ["52.114.148.0","52.114.132.46","52.114.75.24","52.114.76.76","52.114.7.24","52.114.14.70"]

# Where to sync settings from
# file  - load from setting.py file
# db    - load from dsip_settings table
LOAD_SETTINGS_FROM = 'file'
############### End Local-Only Settings ##################
