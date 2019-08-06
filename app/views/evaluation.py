from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import db
from app.email import send_email
from app.forms.property import PropertyForm
from app.models.property import Property

bp = Blueprint('evaluation', __name__)


@bp.route('/', methods=['GET', 'POST'])
def new():

    form = PropertyForm()
    if form.validate_on_submit():
        property = Property()
        form.populate_obj(property)
        send_email('New Deal Notification!',
                   sender='contact@tryofferly.com',
                   recipients=['john@johnlopez.org'],
                   text_body=render_template('emails/new_deal.txt',
                                             property=property),
                   html_body=render_template('emails/new_deal.html',
                                             property=property),
                   attachments=[],
                   sync=True)

        db.session.add(property)
        db.session.commit()
        submitter_phone = db.Column(db.String(255))
        submitter_email = db.Column(db.String(255))
        user_data = {
            'email': property.submitter_email,
            'phone': property.submitter_phone
        }
        return redirect(url_for('.complete', **user_data))

    default_step_id = 'selectStepOne'
    if len(request.args) != 0:
        default_step_id = 'selectStepTwo'
        line_1 = request.args.get('line_1')
        if line_1 is not None:
            form.address.street_address.data = line_1
        locality = request.args.get('city')
        if locality is not None:
            form.address.locality.data = locality
        state_code = request.args.get('state_code')
        if state_code is not None:
            form.address.administrative_area_level_1.data = state_code
        postal_code = request.args.get('postal_code')
        if postal_code is not None:
            form.address.postal_code.data = postal_code
        country = request.args.get('country')
        if country is not None:
            form.address.country.data = country

    return render_template('evaluation/wizard.html',
                           form=form,
                           default_step_id=default_step_id)


@bp.route('/success', methods=['GET'])
def complete():
    phone = request.args.get('phone')
    email = request.args.get('email')
    if phone is None or email is None:
        return redirect(url_for('.new'))
    return render_template('evaluation/complete.html', phone=phone, email=email)
