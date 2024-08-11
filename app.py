from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/madhav_web'
db = SQLAlchemy(app)

class Forms(db.Model):
    sno = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(80) , nullable = False)
    age = db.Column(db.String(12) , nullable = False)
    






@app.route("/" , methods = ['GET' , 'POST'])
def form():
    if (request.method == 'POST'):
        name = request.form.get('name')
        age = request.form.get('age')

        entry = Forms(name = name , age = age)
        db.session.add(entry)
        db.session.commit()
    return render_template("index.html")


if __name__ == "__main__":
    app.run()(debug = True)