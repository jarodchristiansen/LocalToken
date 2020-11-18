from flask import render_template,request,Blueprint,redirect
from companyblog.models import BlogPost, User
from companyblog.core.forms import TextGenForm
import requests
core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    users = User.query.all()
    return render_template('index.html', users=users)

@core.route('/info')
def info():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('info.html')
