from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Create Flask App
app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)


# User Model

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), nullable=False)

    age = db.Column(db.Integer, nullable=False)

# Create Database Tables
with app.app_context():
    db.create_all()

# Home Route
@app.route('/')
def home():

    users = User.query.all()

    return render_template('index.html', users=users)

# Add User Route
@app.route('/add', methods=['POST'])
def add_user():

    name = request.form['name']
    email = request.form['email']
    age = request.form['age']

    # Create New User
    new_user = User(
        name=name,
        email=email,
        age=age
    )

    # Save to Database
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)