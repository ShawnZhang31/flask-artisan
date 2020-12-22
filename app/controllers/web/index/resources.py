'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 17:15:03 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 22:50:07
 */
'''
from flask import current_app
from . import index_bp
import os

@index_bp.route('/', methods=['GET'])
def index():
    return os.path.abspath(os.path.dirname(__file__))