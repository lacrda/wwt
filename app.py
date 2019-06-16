from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('i.html')

@app.route('/teste')
def home2():
    return 'teste'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1000')
