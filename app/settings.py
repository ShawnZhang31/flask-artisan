'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 16:02:36 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:51:13
 */
'''
import os
import sys
import secrets
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

if os.path.exists(os.path.join(basedir, '.env')) is False:
    print('工程根目录下缺少.env文件，创建.env文件...')
    envContents=""
    if os.path.exists(os.path.join(basedir, '.env.example')) is True:
        with open(os.path.join(basedir, '.env.example'), 'r') as envExample:
            envContents = envExample.readlines()
            envExample.close()
    else:
        envContents="#应用秘钥\nSECRET_KEY="

    with open(os.path.join(basedir, '.env'),'w+') as envFile:
            envFile.writelines(envContents)
            envFile.close()

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'



class BaseConfig:
    """基础配置"""

    # 安全秘钥
    SECRET_KEY = os.getenv('SECRET_KEY')
    if SECRET_KEY is None or SECRET_KEY == '':
        SECRET_KEY = secrets.token_urlsafe(16)
        print('SECRET_KEY没有配置,临时设置为:{}'.format(SECRET_KEY))
    
    # 数据库设置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN=True
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_RECORD_QUERIES = True

class DevelopmentConfig(BaseConfig):
    """开发环境配置"""
    if os.path.exists(os.path.join(basedir, 'data-dev.db')) is False:
        with open(os.path.join(basedir, 'data-dev.db'),'w') as dbfile:
            dbfile.close()
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')

class ProductionConfig(BaseConfig):
    """生成环境配置"""
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONNECTION')+"://"+os.getenv('DB_USERNAME')+":"+os.getenv('DB_PASSWORD')+"@"+os.getenv('DB_HOST')+":"+os.getenv('DB_PORT')+"/"+os.getenv('DB_DATABASE')
    
class TestingConfig(BaseConfig):
    """测试环境配置"""
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' #使用内存进行

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}