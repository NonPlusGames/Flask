# ---- YOUR APP STARTS HERE ----

# -- Import section --
from flask import Flask
# from flask import render_template
# from flask import request


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
# @app.route('/sendBreakfast', methods=['GET', 'POST'])
# def handleBreakfast():
#     return "Breakfast should appear here"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)