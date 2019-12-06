from flask import Blueprint, render_template, redirect, url_for
# from frontend.forms import TextForm

diagnose_blueprint = Blueprint('diagnose', __name__)


# @diagnose.route('/diagnose', methods=["GET", "POST"])
# def diagnose():
#     form = TextForm()
#     if form.validate_on_submit():
#         return redirect(url_for('result'))
#     return render_template('diagnose/diagnose.html', title='Diagnose', form=form)