warning: CRLF will be replaced by LF in app.py.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in requirements.txt.
The file will have its original line endings in your working directory
[1mdiff --git a/__pycache__/app.cpython-37.pyc b/__pycache__/app.cpython-37.pyc[m
[1mindex 123e078..881dca8 100644[m
Binary files a/__pycache__/app.cpython-37.pyc and b/__pycache__/app.cpython-37.pyc differ
[1mdiff --git a/app.py b/app.py[m
[1mindex 1b0b2af..2e2ae07 100644[m
[1m--- a/app.py[m
[1m+++ b/app.py[m
[36m@@ -1,16 +1,25 @@[m
 from flask import Flask, render_template[m
[32m+[m[32mfrom flask_sqlalchemy import SQLAlchemy[m
[32m+[m[32mimport os[m
 [m
 app = Flask(__name__)[m
[32m+[m[32mapp.config.from_object(os.getenv('APP_SETTINGS'))[m
[32m+[m[32mapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False[m
[32m+[m[32mdb = SQLAlchemy(app)[m
 [m
[32m+[m[32mfrom models import Terr[m
 [m
 @app.route('/')[m
 def home():[m
     return render_template('i.html')[m
 [m
[31m-@app.route('/teste')[m
[32m+[m[32m@app.route('/terr')[m
 def home_2():[m
[31m-    print('teste')[m
[31m-[m
[32m+[m[32m    try:[m
[32m+[m[32m        territories=Terr.query.all()[m
[32m+[m[32m        return jsonify([e.serialize() for e in terr])[m
[32m+[m[32m    except Exception as e:[m
[32m+[m[32m        return(str(e))[m
     [m
 if __name__ == '__main__':[m
     app.run()[m
[1mdiff --git a/requirements.txt b/requirements.txt[m
[1mindex eb5f697..d3f6e6e 100644[m
[1m--- a/requirements.txt[m
[1m+++ b/requirements.txt[m
[36m@@ -1,17 +1,16 @@[m
[31m-beautifulsoup4==4.6.3[m
[31m-certifi==2018.11.29[m
[31m-chardet==3.0.4[m
[32m+[m[32malembic==1.0.10[m
 Click==7.0[m
[31m-Flask==1.0.2[m
[31m-gunicorn==19.9.0[m
[31m-html5lib==1.0.1[m
[31m-idna==2.7[m
[32m+[m[32mFlask==1.0.3[m
[32m+[m[32mFlask-Migrate==2.5.2[m
[32m+[m[32mFlask-Script==2.0.6[m
[32m+[m[32mFlask-SQLAlchemy==2.4.0[m
 itsdangerous==1.1.0[m
 Jinja2==2.10.1[m
[32m+[m[32mMako==1.0.12[m
 MarkupSafe==1.1.1[m
[31m-requests==2.20.1[m
[31m-six==1.11.0[m
[31m-urllib3==1.24.1[m
[31m-virtualenv==16.0.0[m
[31m-webencodings==0.5.1[m
[31m-Werkzeug==0.15.2[m
[32m+[m[32mpsycopg2-binary==2.8.3[m
[32m+[m[32mpython-dateutil==2.8.0[m
[32m+[m[32mpython-editor==1.0.4[m
[32m+[m[32msix==1.12.0[m
[32m+[m[32mSQLAlchemy==1.3.5[m
[32m+[m[32mWerkzeug==0.15.4[m
