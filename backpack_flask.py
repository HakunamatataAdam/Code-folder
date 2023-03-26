from flask import Flask,g, render_template
import sqlite3 

app = Flask(__name__)

DATABASE = 'backpack.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    cursor = get_db().cursor()
    sql = "SELECT * FROM contents"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)
    
@app.route('/add')
def add():
    cursor = get_db().cursor()
    sql = "INSERT INTO FROM contents(name, discription) VALUES (?,?)"
    cursor.execute(sql,)
    return render_template("contents.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)