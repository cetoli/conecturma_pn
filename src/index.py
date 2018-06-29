from bottle import default_app
from control.bulma_controller import *

import bottle
import os

view_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'view')
bottle.TEMPLATE_PATH.insert(0, view_path)

application = default_app()


@route('/error403')
def error403():
    return template('error403.tpl')


if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, reloader=False, debug=True)
