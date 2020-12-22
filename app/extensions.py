'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 16:31:16 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:37:47
 */
'''
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_redis import FlaskRedis

# CSRF保护
csrf = CSRFProtect()
# db orm
db = SQLAlchemy()
# db migrate
migrate = Migrate()
# mail
mail = Mail()
# redis
redis_cli = FlaskRedis()

def register_extensions(app):
    """注册flask的扩展"""
    # 初始化csrf
    csrf.init_app(app)
    # 初始化数据库服务
    db.init_app(app)
    # 初始化数据库迁移工具
    migrate.init_app(app)
    # 初始化邮箱工具
    mail.init_app(app)
    # 初始化redis工具
    redis_cli.init_app(app)