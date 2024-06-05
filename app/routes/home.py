"""
This is the login route for the application."""
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import db, login_manager
from app.models import User, Recipe
from app.forms.login import LoginForm, RegistrationForm
from flask import Blueprint
from werkzeug.security import check_password_hash

home_bp = Blueprint('home', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@home_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    This function handles the login route.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash('Login successful.', 'success')
            return redirect(url_for('home.index'))
        elif user and not check_password_hash(user.password, form.password.data):
            flash('Login failed. Please check your password.', 'danger')
        else:
            flash('Email not Found! Click on Register', 'danger')
    return render_template('login.html', form=form)

@home_bp.route('/logout')
@login_required
def logout():
    """
    This function handles the logout route.
    """
    logout_user()
    flash('Logout successful.', 'success')
    return redirect(url_for('home.login'))

@home_bp.route('/')
def index():
    """Home Page"""
    recipes = Recipe.query.order_by(Recipe.created_at.desc()).limit(6).all()
    return render_template('index.html', recipes=recipes)

@home_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email already exists.', 'danger')
        else:
            new_user = User(username=form.username.data,
                            email=form.email.data,
                            password=form.password.data)
            print(form.username.data, form.email.data, form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully.', 'success')
            return redirect(url_for('home.login'))
    return render_template('register.html', form=form)

@home_bp.route('/about')
def about():
    return render_template('about.html')
