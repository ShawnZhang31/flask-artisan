'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 20:56:30 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:09:28
 */
'''

from .api import register_api_blueprints
from .web import register_web_blueprints

def register_app_blueprints(app):
    """注册app的蓝本"""
    register_api_blueprints(app)
    register_web_blueprints(app)