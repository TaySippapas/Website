from flask import request, jsonify,render_template,Blueprint,session
import sqlite3
login_bp = Blueprint('login', __name__)
@login_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')
@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    EmailOrUsername = data.get('EmailOrUsername')
    password = data.get('password')
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM signup WHERE (gmail=? OR username=?) AND password = ?', (EmailOrUsername,EmailOrUsername,password))
        user = cursor.fetchone()
    if user:
        session['logged_in'] = True
        return jsonify({"success": True, "message": "Login successful!"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid username or password!"}), 401
@login_bp.route('/check_login', methods=['GET'])
def check_login():
    """Route to check login status."""
    if 'logged_in' in session and session['logged_in']:
        return jsonify({"logged_in": True,'profile_pic_url': session.get('profile_pic_url', '/static/default_profile.png')}), 200
    else:
        return jsonify({"logged_in": False}), 200
