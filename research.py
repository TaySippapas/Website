from flask import Blueprint,render_template
research_bp=Blueprint('research',__name__)
@research_bp.route('/research')
def research_home():
    return render_template('research.html')