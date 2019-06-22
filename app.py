from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('i.html')

@app.route('/teste')
def home_2():
    print('teste')

    
if __name__ == '__main__':
    app.run()
