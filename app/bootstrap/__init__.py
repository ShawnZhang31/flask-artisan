'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 20:48:33 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:21:46
 */
'''
from ..extensions import register_extensions
from ..routes import register_app_blueprints
from .console.context import register_app_context
from ..exceptions import register_app_exception_handlers
from .console.commands import register_shell_commands
def boot(app):
    # 注册扩展模块
    register_extensions(app)
    # 注册蓝图
    register_app_blueprints(app)
    # 注册app的上下文环境
    register_app_context(app)
    # 注册app的异常处理句柄
    register_app_exception_handlers(app)
    # 注册app的shell命令
    register_shell_commands(app)
