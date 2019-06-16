from flask import Flask, render_template
def before_request():
    app.jinja_env.cache = {}

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':
    app.before_request(before_request)
    app.run(debug=True)
