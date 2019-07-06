from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func
import os

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Terr
engine = create_engine('postgresql://postgres:postgres@localhost:5432/wwt')

# home
@app.route('/')
def home():
    return render_template('i.html')

@app.route('/terr')
def home_2():

    try:
        territories=Terr.query.all()
        return jsonify([i.serialize() for i in territories])
    except Exception as e:
        return(str(e))
    
if __name__ == '__main__':
    app.debug=True
    app.run()
