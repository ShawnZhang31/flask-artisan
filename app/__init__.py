'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 16:01:11 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:38:28
 */
'''
import os
import click
import flask
from flask import Flask

from .settings import config
from .bootstrap import boot

__version__ = '0.0.1'


def create_app(config_name='development'):
    """flask的工厂函数"""
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    
    app = Flask('app')
    app.config.from_object(config[config_name])
    # # 注册flask扩展工具
    # register_extensions(app)
    # # 注册应用蓝本
    # register_blueprints(app)
    # # 注册shell环境变量
    # register_shell_contex(app)
    # # 注册错误处理句柄
    # register_errorhandlers(app)

    # 启动app的相关服务
    boot(app)

    return app

def register_extensions(app):
    """注册flask的扩展"""
    # 初始化csrf
    csrf.init_app(app)
    ## 剥离不使用csrf保护的蓝本或路由
    csrf.exempt(api_v1_main)
    # 初始化数据库服务
    db.init_app(app)
    # 初始化数据库迁移工具
    migrate.init_app(app)
    # 初始化邮箱工具
    mail.init_app(app)
    # 初始化redis工具
    redis_cli.init_app(app)

def register_blueprints(app):
    """注册应用的蓝本"""
    # app
    app.register_blueprints(index_bp)

    # api
    app.register_blueprints(api_v1_main, url_prefix='api/v1')

def register_shell_contex(app):
    """注册应用的shell环境变量"""
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)

def register_errorhandlers(app):
    """注册应用的错误处理方法"""
    @app.errorhandler(400)
    def forbidden(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('errors/413.html'), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500
    














