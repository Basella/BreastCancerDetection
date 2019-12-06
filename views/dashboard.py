from flask import Blueprint, render_template

dashboard_blueprint = Blueprint('dashboard', __name__)

# @dashboard.route(url_for('dashboard'))
# def dashboard():
#     return render_template('dashboard/dashboard.html')