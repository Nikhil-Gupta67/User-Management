import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev-secret-key",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'users.db')}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        users = User.query.order_by(User.id.desc()).all()
        return render_template('index.html', users=users)

    @app.route('/add', methods=['POST'])
    def add_user():
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        age_value = request.form.get('age', '').strip()

        if not name or not email or not age_value:
            flash('Please fill out all fields.', 'error')
            return redirect(url_for('home'))

        if '@' not in email or '.' not in email:
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('home'))

        try:
            age = int(age_value)
        except ValueError:
            flash('Age must be a whole number.', 'error')
            return redirect(url_for('home'))

        if age < 1 or age > 120:
            flash('Age must be between 1 and 120.', 'error')
            return redirect(url_for('home'))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('A user with that email already exists.', 'error')
            return redirect(url_for('home'))

        new_user = User(name=name, email=email, age=age)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!', 'success')
        return redirect(url_for('home'))

    @app.route('/delete/<int:user_id>', methods=['POST'])
    def delete_user(user_id):
        user = db.session.get(User, user_id)
        if user is None:
            flash('User not found.', 'error')
            return redirect(url_for('home'))

        db.session.delete(user)
        db.session.commit()
        flash('User removed successfully!', 'success')
        return redirect(url_for('home'))

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)