from flask import Blueprint, render_template, url_for

pages = Blueprint('pages', __name__)
 
@pages.route('/')
@pages.route('/home')
def home():

    return render_template('home.html')


@pages.route('/resume')
def resume():
    return render_template('resume.html')

@pages.route('/')
@pages.route('/projects')
def projects():

    return render_template('projects.html')
