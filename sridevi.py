from bottle import template,route,run

@route('/')
@route('/sridevi')
def sridevi():
    return template('feedbac')

run(host="localhost",port=8080)