'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 17:14:04 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 17:14:45
 */
'''
from flask import Blueprint
index_bp = Blueprint('index', __name__)
from . import resources