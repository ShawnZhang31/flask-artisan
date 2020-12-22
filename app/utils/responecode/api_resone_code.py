'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 17:09:06 
 * @Last Modified by:   Shawn Zhang 
 * @Last Modified time: 2019-09-08 17:09:06 
 */
'''
class API_RESPONE_CODE:
    '''Api返回的状态码'''
    API_RESPONE_SUCCESS=200 #请求处理成功

    # 参数填写错误
    REQUEST_ARGUMENTS_ERROR=4100 #API参数填写错误

    # 阿里发送短信的状态码
    ALI_SEND_SMS_ERROR=5100 #阿里发送短信验证码失败
    ALI_SEND_SMS_TIME_PERIMIT=5101 #发送验证码过于频繁

    # 数据库操作错误
    SERVER_DB_QUREY_ERROR=5200 #数据库相关的错误

    # 数据运算错误
    SERVER_FACEMODULE_ERROR = 5300 # facecloud基础算法错误