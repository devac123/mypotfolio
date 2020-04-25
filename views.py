from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:@localhost/client_details'

db =SQLAlchemy(app)
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    subject = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/",methods=['GET','POST'])
def Contact():
    if ( request.method == 'POST'):

        name=request.form.get('name')
        email=request.form.get('email')
        msg= request.form.get('message')
        subject = request.form.get('subject')


        entry = Contacts(name = name ,subject =subject,message=msg,email=email)
        db.session.add(entry)
        db.session.commit()
    else:
        return render_template('index.html')

app.run(debug=True)

