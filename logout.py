from flask import session,Blueprint,redirect,url_for
logout_bp=Blueprint('logout',__name__)
@logout_bp.route('/logout',methods=['POST'])
def logout():
    session.pop('logged_in',None)
    return redirect(url_for('home.home'))
