from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

@app.route('/')
def index():
    return 'HELLO WORLDS'

@app.route('/page')
def page():
    return render_template('Page.html')

@app.route('/api', methods=[ 'GET', 'POST'])
def api():
    if(request.method == 'GET'):
        dictionary = {
            'name': 'Ammad',
            'age': 27    
        }

        return jsonify(dictionary)