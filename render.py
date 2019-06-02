from flask import Flask, render_template

app = Flask("wwt")

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

app.run()