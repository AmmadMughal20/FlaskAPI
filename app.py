from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return 'HELLO WORLDS'

@app.route('/page')
def page():
    return render_template('Page.html')