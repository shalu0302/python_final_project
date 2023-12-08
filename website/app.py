from flask import Flask, render_template
import sqlite3
import pathlib

app = Flask(__name__)

base_path = pathlib.Path().cwd()
db_name = "eng_5.db"
file_path = base_path / db_name

@app.route('/')
def index():
    return render_template('index_fillin.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    titanic_data = cursor.execute("SELECT * FROM eng_5 LIMIT 15").fetchall()
    con.close()
    return render_template('data_table_fillin.html',titanic_data=titanic_data)

if __name__ == "__main__":
    app.run(debug=True)