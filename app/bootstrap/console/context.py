'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 21:12:25 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:50:03
 */
'''

from app.extensions import db

def register_app_context(app):
    """注册app的上下文"""
    register_shell_contex(app)

def register_shell_contex(app):
    """注册应用的shell环境变量"""
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)
        