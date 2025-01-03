from flask import Flask
from home import home_bp  # Import the homepage blueprint
from login import login_bp  # Import the login blueprint
from signup import signup_bp
from research import research_bp
from product import product_bp
from aboutus import aboutus_bp
from logout import logout_bp
from predict import predict_bp
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mae_mueng_pen_gay'
# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(research_bp)
app.register_blueprint(product_bp)
app.register_blueprint(aboutus_bp)
app.register_blueprint(predict_bp)
if __name__ == '__main__':
    app.run(debug=True)
