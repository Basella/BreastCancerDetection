from flask import Blueprint, render_template, redirect, url_for
from frontend.forms import TextForm

diagnose = Blueprint('diagnose', __name__)


@diagnose.route('/diagnose', methods=["GET", "POST"])
def diagnosepatient():
    form = TextForm()
    if form.validate_on_submit():
        return redirect(url_for('result'))
    return render_template('diagnose/diagnose.html', title='Diagnose', form=form)