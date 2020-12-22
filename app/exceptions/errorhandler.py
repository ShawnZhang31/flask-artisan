'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 21:17:40 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-08 21:18:02
 */
'''
from flask import render_template

def register_errorhandlers(app):
    """注册应用的错误处理方法"""
    @app.errorhandler(400)
    def forbidden(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('errors/413.html'), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500