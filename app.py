from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/terr")
def get_terr_map():
    return render_template('polygons.html')

# @app.route("/details")
# def get_book_details():
#     author=request.args.get('author')
#     published=request.args.get('published')
#     return "Author : {}, Published: {}".format(author,published)

if __name__ == '__main__':
    app.run()
