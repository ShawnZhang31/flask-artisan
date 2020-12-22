'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 21:04:17 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:39:07
 */
'''
from ..controllers.api.v1.main import api_v1_main
from ..extensions import csrf

def register_api_blueprints(app):
    csrf.exempt(api_v1_main)
    app.register_blueprint(api_v1_main, url_prefix='/api/v1')