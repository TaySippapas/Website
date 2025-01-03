from flask import Blueprint,render_template
product_bp=Blueprint('product',__name__)
@product_bp.route('/product')
def product_home():
    return render_template('product.html')