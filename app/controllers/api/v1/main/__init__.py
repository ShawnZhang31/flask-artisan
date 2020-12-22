'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 16:57:59 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 16:59:33
 */
'''
from flask import Blueprint
from flask_cors import CORS
api_v1_main = Blueprint('api_v1', __name__)
# 跨域支持
CORS(api_v1_main)

from . import resoureces