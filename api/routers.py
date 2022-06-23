from flask_cors import CORS
from flask_bootstrap import Bootstrap
from flask import render_template, request, Flask, jsonify

app = Flask(__name__)
Bootstrap(app)
cors = CORS(app, resources={r'/*': {"origins": '*'}})
app.config['CORS_HEADER'] = 'Content-Type'

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


@app.route("/search", methods=['GET'])
def search():
    print("searching...")
    if request.method == 'GET':
        q = request.args.get("q", None)
        return jsonify({
            "status": "success",
            "query": q,
            "result": "Hello world!"
        })


@app.route("/calculate", methods=["POST"])
def calculate():
    print("calculate...")
    print(request.method)
    if request.method == "POST":
        a = request.json['a']
        b = request.json['b']
        return jsonify({
            "status": "success",
            "a": a,
            "b": b,
            "sum": a + b
        })
    else:
        return jsonify({
            "status": "fail"
        })
