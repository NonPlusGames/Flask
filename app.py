# ---- YOUR APP STARTS HERE ----

# -- Import section --
from flask import Flask
# from flask import render_template
# from flask import request
# from flask import redirect
# from model import shout

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --

# INDEX
@app.route('/')
@app.route('/index')
def index():
  return "hello world"

@app.route('/secret')
def secret():
    return "<h1>You found the secret!</h1>"

#  -- Create your own! --
# @app.route()
# def
#     return ""

# -- Render Template --
# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html')

# -- Jinja3 Templates --
# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'first_name': 'Rick'}
#     return render_template('index.html', title='Home', user=user)

# -- Props Dictonary --
# @app.route('/')
# @app.route('/index')
# def index():
#     props = {
#           'first_name': 'Rick',
#           'last_name': 'Sanchez'
#     }
#     return render_template('index.html', props=props)

#  -- Create your own! Build a 'resultspage.html'. Send at least one piece of information. --
# @app.route()
# def
#     return render_template()

# -- Form --
# @app.route('/sendBreakfast')
# def handleBreakfast():
#     return "Breakfast should appear here"

# -- Form with GET and POST --
# @app.route('/sendBreakfast', methods=['GET', 'POST'])
# def handleBreakfast():
#     if request.method == 'GET':
#         return "You're getting the breakfast page!"
#     else:
#         return "You're posting to the breakfast page"

# -- Model --
# @app.route('/form')
# def handleForm():
    # nickname = request.form['nickname']
    # breakfast = request.form['breakfast']
    # loud_name = shout(nickname)
    # return "Hello, " + loud_name + "! I hear you had " + breakfast + " for breakfast! Sounds delicious."

# -- ADVANCED TOPICS --

# -- Redirect --
# @app.route('/sendBreakfast', methods=['GET', 'POST'])
# def handleBreakfast():
#     if request.method == 'GET':
#         return redirect('/notFound')
#     else:
#         ... #code to handle `POST` request

# @app.route('/notFound')
# def handle404():
#     return render_template('404.html')
#     # Note that this assumes you've created a 404.html template

# -- Logic in Templates --
# @app.route('/logic')
# def logic():
#     name="Fred"
#     return render_template('logic.html', name=name)

# -- Block Content --
# @app.route('/blockcontent')
# def blockcontent():
#     name="Fred"
#     return render_template('blockcontent.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)