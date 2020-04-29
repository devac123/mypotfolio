from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import json


with open('portfol.json','r') as c:
    shubham = json.load(c)["params"]



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  shubham['local_server']
db =SQLAlchemy(app)
class client_detail(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    subject = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)



@app.route("/")
def home():
    return render_template(shubham['templates'],email = shubham)

@app.route("/contact",methods=['GET','POST'])
def Contact():
    if ( request.method == 'POST'):

        name=request.form.get('name')
        email=request.form.get('email')
        msg= request.form.get('message')
        subject = request.form.get('subject')



        entry = client_detail(name = name ,subject =subject,message=msg,email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html')

app.run(debug=True)

