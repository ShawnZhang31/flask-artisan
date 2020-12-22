'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 17:49:26 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 22:48:10
 */
'''
import click
import secrets
import dotenv
import os
def register_shell_commands(app):
    """注册shell的命令"""
    register_command_generate_secretkey(app)


def register_command_generate_secretkey(app):
    @app.cli.command()
    def generate_secretkey():
        """生成并配置.env文件的SECRET_KEY"""
        SECRET_KEY = secrets.token_urlsafe(16)
        basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
        envPath = os.path.join(basedir,'.env')
        if os.path.exists(basedir):
            dotenv.set_key(envPath, 'SECRET_KEY', SECRET_KEY)
            click.echo('SECRET_KEY={}'.format(SECRET_KEY))
            click.echo('请重新激活pipenv')
        else:
            click.echo('请先创建.env文件')
