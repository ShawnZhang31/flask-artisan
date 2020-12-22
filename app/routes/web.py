'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 21:07:03 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:39:16
 */
'''
from ..controllers.web.index import index_bp

def register_web_blueprints(app):
    """注册web的蓝本"""
    app.register_blueprint(index_bp)