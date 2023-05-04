from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json

with open('config.json', 'r') as conf:
    params = json.load(conf)['params']

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# Quick test configuration. Please use proper Flask configuration options
# in production settings, and use a separate file or environment variables
# to manage the secret key!
app.secret_key = params['secretKey']

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USERNAME = 'ex@gmail.com',
    MAIL_PASSWORD = 'exPass'
)
# creating mail
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

class Gallery(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String, unique=False, nullable=False)
    slug = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.String, nullable=False)


# routes 
@app.route("/")
def home():
    galleries = Gallery.query.filter_by().all()
    return render_template('index.html', galleries=galleries)

@app.route("/about")
def about():
    galleries = Gallery.query.filter_by().all()
    return render_template('about.html', galleries=galleries)

@app.route("/services")
def services():
    galleries = Gallery.query.filter_by().all()
    return render_template('services.html', galleries=galleries)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    galleries = Gallery.query.filter_by().all()
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
        # mail.send_message(f'New message from @{name}SketchWeb', sender=email, recepients=['ex@gmail.com'], body= message)
    return render_template('contact.html', galleries=galleries)

@app.route("/gallery/<string:slug>", methods=['GET'])
def gallery(slug):
    galleries = Gallery.query.filter_by().all()
    gallery = Gallery.query.filter_by(slug=slug).first()
    return render_template('gallery.html', gallery=gallery, galleries=galleries)

@app.route("/admin", methods=['GET', 'POST'])
def dashboard():
    galleries = Gallery.query.filter_by().all()
    contacts = Contact.query.filter_by().all()
    if 'user' in session and session['user'] == params['admin_name']:
        return render_template('dashboard.html', galleries=galleries, contacts=contacts)
    elif request.method == 'POST':
        user = request.form.get('UserName')
        password = request.form.get('password')

        if user == params['admin_name'] and password == params['password']:
            session['user'] = user
            return redirect("/admin")

    return render_template("login.html", galleries=galleries)


@app.route("/edit/<string:slug>", methods=['GET','POST'])
def editGallery(slug):
    gallery = Gallery.query.filter_by(slug=slug).first()
    if request.method == 'POST':
        gallery.title = request.form.get("title")
        gallery.content = request.form.get("content")
        db.session.commit()
        return redirect("/admin")


    return render_template('editGallery.html',gallery=gallery)

app.run(debug=True)