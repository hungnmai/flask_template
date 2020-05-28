import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = '/'.join(dir_path.split('/')[:-1])
sys.path.append(dir_path)
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from database.connection import MongoDB
from flask import render_template, request, Flask, jsonify

app = Flask(__name__)
Bootstrap(app)
cors = CORS(app, resources={r'/*': {"origins": '*'}})
app.config['CORS_HEADER'] = 'Content-Type'

mongo = MongoDB()
app.config["JSON_SORT_KEYS"] = False


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Flask template')


@app.route('/endpoint', methods=['POST', 'GET'])
def endpoint():
    try:
        if request.method == 'POST':
            q = request.form['q']
        else:
            q = request.args.get('q')

        return jsonify({"q": q, "status": "success"})
    except Exception as e:
        return jsonify({"status": "fail", "cause": str(e)})
