'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 16:59:50 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:44:30
 */
'''
from flask import request

from . import api_v1_main
from app.utils.responecode.api_resone_code import API_RESPONE_CODE

@api_v1_main.route('/', methods=['GET', 'POST'])
def index():
    return {'code':API_RESPONE_CODE.API_RESPONE_SUCCESS, 'message':None, 'data':'Hello Flask'}