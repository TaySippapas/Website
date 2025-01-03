from flask import render_template,Blueprint,session
home_bp = Blueprint('home', __name__)
@home_bp.route('/')
def home():
    logged_in = session.get('logged_in', False)
    profile_pic_url = session.get('profile_pic_url', '/static/default_profile.png')
    return render_template('home.html', logged_in=logged_in, profile_pic_url=profile_pic_url)
