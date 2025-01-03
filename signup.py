from flask import request, jsonify,render_template,Blueprint
import sqlite3

# Route for serving the signup page
signup_bp=Blueprint('signup',__name__)
@signup_bp.route('/signup',methods=['GET'])
def home():
    return render_template('signup.html')  # This will render the signup.html file
@signup_bp.route('/signup',methods=['POST'])
def signup():
    data=request.get_json()
    gmail=data.get('gmail')
    username=data.get('username')
    password=data.get('password')
    conn=sqlite3.connect('my_database.db')
    cursor=conn.cursor()
    try:
        # Insert the data into the signup table
        cursor.execute('''
            INSERT INTO signup (gmail, username, password) 
            VALUES (?, ?, ?)
        ''', (gmail, username, password))
        conn.commit()
        
        return jsonify({"success": True}), 200
    except sqlite3.IntegrityError as e:
        return jsonify({"success": False, "error": "Username or email already exists"}), 400
    finally:
        conn.close()