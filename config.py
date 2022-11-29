# config.py: Edit this to fit your application, or the config will be loaded from config,yaml which means you can use
# the web setting page on 'yourdomain'/firstuse
import yaml
import os

filepath = os.path.join(os.getcwd(), './config/config.yaml')
with open(filepath, 'r') as f:  # 用with读取文件更好
    configs = yaml.load(f, Loader=yaml.FullLoader)
print(type(configs))  # <class 'dict'>
print(configs["app_name"]['app_name'])
print(configs["app_name"]['app_version'])


# app name
app_name = configs["app_name"]['app_name']
app_version = configs["app_name"]['app_version']

# app settings
secret_key = configs["app_settings"]['secret_key']
initial_integral = int(configs["app_settings"]['initial_integral'])

# onedrive
redirect_url = configs["onedrive"]['redirect_url']
"""
client_secret = 'your_client_secret'
client_id='your_client_id'
api_base_url='https://api.onedrive.com/v1.0/'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
"""
# alist
alist_url = configs["alist"]['alist_url']
alist_home = configs["alist"]['alist_home']
alist_passwd = configs["alist"]['alist_passwd']
alist_path = configs["alist"]['alist_path']

# mysql
database = configs["mysql"]['database']
user_name = configs["mysql"]['user_name']
passwd = configs["mysql"]['passwd']
host = configs["mysql"]['host']
port = configs["mysql"]['port']

# first_use
is_first_use = configs["first_use"]['is_first_use']
