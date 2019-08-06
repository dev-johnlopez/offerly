from flask import Blueprint, render_template, redirect, url_for
from app.forms.property import LandingAddressForm
from app.models.address import Address
from app.models.property import Property

bp = Blueprint('landing', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = LandingAddressForm()
    if form.validate_on_submit():
        if form.validate_on_submit():
            address_data = {
                'line_1': form.street_number.data + " " + form.route.data,
                'city': form.locality.data,
                'state_code': form.administrative_area_level_1.data,
                'postal_code': form.postal_code.data,
                'country': form.country.data
            }

            return redirect(url_for('evaluation.new', **address_data))
    return render_template('landing/index.html', form=form)


@bp.route('/about', methods=['GET'])
def about():
    return render_template('landing/about.html')


@bp.route('/contact', methods=['GET'])
def contact():
    return render_template('landing/contact.html')


@bp.route('/privacy', methods=['GET'])
def privacy():
    return render_template('landing/privacy.html')


@bp.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('landing/services.html')


@bp.route('/terms', methods=['GET'])
def terms():
    return render_template('landing/terms.html')


@bp.route('/pricing', methods=['GET', 'POST'])
def pricing():
    form = LandingAddressForm()
    if form.validate_on_submit():
        address_data = {
            'line_1': form.street_number.data + " " + form.route.data,
            'city': form.locality.data,
            'state_code': form.administrative_area_level_1.data,
            'postal_code': form.postal_code.data,
            'country': form.country.data
        }

        return redirect(url_for('evaluation.new', **address_data))
    return render_template('landing/pricing.html', form=form)
