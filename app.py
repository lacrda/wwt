from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func
import os

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost:5432/wwt'
db = SQLAlchemy(app)


# home
@app.route('/')
def home():
    return render_template('i.html')

@app.route('/terr')
def home_2():
    from models import Terr
    try:
        territories=Terr.query.all()
        return jsonify([i.serialize() for i in territories])
    except Exception as e:
        return(str(e))

@app.route('/teste')
def teste():
    from models import Terr
    try:
        territory=Terr.query.filter_by(id = "28").first()
        territory.position = "[0, 15]"
        db.session.add(territory)
        # lacerda = Terr("terr0","lacerda","[30,30]")
        # db.session.add(lacerda)
        db.session.commit()
        return("adicionado")
    except Exception as e:
        return(str(e))

@app.route('/init')
def home3():
    from game import return_g
    from models import Terr
    g = return_g()
    try:
        # owners = Owners.query.all()
        # return jsonify([i.serialize() for i in owners])
        a = 0
        gv = list(g.values())
        gk = list(g.keys())
        for i in g:
            b = Terr(str("terr"+str(a)),gv[a],gk[a])
            db.session.add(b)
            a += 1
        db.session.commit()
        return render_template('game.html', g=g)
    except Exception as e:
        return(str(e))


    
if __name__ == '__main__':
    app.debug=True
    app.run()
