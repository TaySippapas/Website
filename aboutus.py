from flask import Blueprint,render_template
aboutus_bp=Blueprint('aboutus',__name__)
@aboutus_bp.route('/aboutus')
def research_home():
    return render_template('aboutus.html')