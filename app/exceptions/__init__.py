'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 21:18:43 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:20:03
 */
'''
from .errorhandler import register_errorhandlers

def register_app_exception_handlers(app):
    """注册应用的错误处理句柄"""
    register_errorhandlers(app)