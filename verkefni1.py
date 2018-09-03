from sys import argv

from bottle import *

@route('/')
def index():
    return """
<h2>Verkefni 1</h2>
<a href="/heimur">Halló</a>
<a href="/about">About</a>
<a href="/bio">Biography</a>
<a href="/pic">Pictures</a>
"""

@route('/heimur')
def heimur():
    return "Halló Heimur"

@route('/about')
def about():
    return "This is the about page"

@route('/bio')
def bio():
    return "This is the biography page"

@route('/pic')
def pic():
    return "This is the pictures page"

#run()

bottle.run(host='0.0.0.0', port=argv[1])
