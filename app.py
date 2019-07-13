from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func, update
import os

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost:5432/wwt'
db = SQLAlchemy(app)


# home
@app.route('/')
def home():
    from game import return_g, return_colors
    from models import Terr, Owners
    try:
        o = Owners.query.filter().order_by(Owners.id)
        oo = [i.serialize() for i in o]
        print(oo)
        t = Terr.query.filter().order_by(Terr.id)
        tt = {}
        for i in t:
            tt[i] = i.owner
        print(tt)
        # tt = [i.serialize() for i in t]
        colors = return_colors()
    except Exception as e:
        return(str(e))

    return render_template('i.html', oo = oo, tt = tt)

@app.route('/terr')
def home_2():
    from models import Terr
    try:
        territories=Terr.query.filter().order_by(Terr.id)
        return jsonify([i.serialize() for i in territories])
    except Exception as e:
        return(str(e))

@app.route('/nround')
def new_round():
    from models import Terr, Owners
    from rounds import go_round
    try:
        terrs = go_round()
        atacante = Terr.query.filter_by(position=str(terrs[0])).first()
        new_owner = atacante.owner
        new_color = atacante.color
        atacado = Terr.query.filter_by(position=str(terrs[1])).first()
        round_info = [atacado.owner, atacado.position]
        atacado.owner=new_owner
        atacado.color=new_color
        own_atacante = Owners.query.filter_by(owner=atacante.owner).first()
        own_atacante.quant = Terr.query.filter_by(owner=atacante.owner).count()
        own_atacado = Owners.query.filter_by(owner=round_info[0]).first()
        own_atacado.quant = Terr.query.filter_by(owner=round_info[0]).count()
        db.session.commit()

        # stmt = update(terr).where(Terr.position==terrs[1]).values(owner=new_owner)

        # return jsonify([i.serialize() for i in atacante])
        # return jsonify([i.serialize() for i in atacado])
        return render_template('game.html', g=new_owner, h=round_info)
    except Exception as e:
        return(str(e))

@app.route('/init')
def home3():
    from game import return_g, return_colors
    from models import Terr,Owners
    g = return_g()
    try:
        colors = return_colors()
        a = 0
        gv = list(g.values())
        gk = list(g.keys())
        ck = list(colors.keys())
        cv = list(colors.values())
        for i in g:
            b = Terr(str("terr"+str(a)),gv[a][0],gk[a],gv[a][1])
            db.session.add(b)
            a += 1
        db.session.commit()
        # id, owner, color, quant
        for k,v in colors.items():
            q = Terr.query.filter_by(owner=k).count()
            a = Owners(k,v,q)
            db.session.add(a)
            db.session.commit()

        return render_template('game.html', g=g)
    except Exception as e:
        return(str(e))

@app.route('/owners')
def list_owners():
    from models import Owners
    try:
        territories=Owners.query.filter().order_by(Owners.id)
        return jsonify([i.serialize() for i in territories])
    except Exception as e:
        return(str(e))

    
if __name__ == '__main__':
    app.debug=True
    app.run()
