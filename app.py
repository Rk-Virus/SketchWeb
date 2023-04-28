from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask import request
import json

with open('config.json', 'r') as conf:
    params = json.load(conf)['params']

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USERNAME = 'ex@gmail.com',
    MAIL_PASSWORD = 'exPass'
)
#creating mail
mail = Mail(app)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = params['local_url']
# initialize the app with the extension
db.init_app(app)

#models...
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    subject = db.Column(db.String, nullable=True)
    message = db.Column(db.String, nullable=False)

@app.route("/")
def home():
    flash("This site is under construction...")
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''fetching contact details'''
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        #creating entry
        entry = Contact(name=name, email=email, subject=subject, message=message)
        #adding entry
        db.session.add(entry)
        db.session.commit()

        #sending mail
        mail.send_message(f'New message from @{name}SketchWeb', sender=email, recepients=['ex@gmail.com'], body= message)
    return render_template('contact.html')

@app.route("/gallery-single")
def gallerySingle():
    return render_template('gallery-single.html')


app.run(debug=True)