from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)  # note that datebase must initial first check datebase.py


class User(db.Model):
    # primary_key=True means that id mstbe unique
    def __init__(self):
        self.id = db.Column(db.Integer, primary_key=True)
        self.username = db.Column(db.String(20), unique=True, nullable=False)
        self.email = db.Column(db.String(120), unique=True, nullable=False)
        self.image_file = db.Column(db.String(20), unique=False,
                                    nullable=False, default='default.jpg')
        self.password = db.Colum(db.String(60), nullable=False)
        self.post = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User: {self.username} Email: {self.email} Pic: {self.image_file}"


class Post(db.Model):
    def __init__(self):
        self.id = db.Column(db.Integer, primary_key=True)
        self.title = db.Column(db.String(100), null=False)
        self.date_posted = db.Column(
            db.DateTime, nullable=False, default=datetime.now())
        self.content = db.Column(db.txt, nullable=False)
        self.user_id = db.Column(
            db.Integer, db.Foreignkey('user.id', nullable=False))


posts = [{'author': 'walker',
         'title': 'Blog Post 1',
          'content': 'First post content',
          'date_posted': 'April 21 2024'},
         {'author': 'frank',
         'title': 'Blog Post 2',
          'content': 'Second post content',
          'date_posted': 'April 22 2024'}]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'walker3354827@gmail.com' and form.password.data == 'frank':
            flash('You have been logged in!', 'success')
            return redirect('home')
        else:
            flash('Login unsuccessful Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
