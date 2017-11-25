from flask import Blueprint, render_template, request

organization = Blueprint('Organization', __name__)


@organization.route('/organization_profile/', methods=['GET', 'POST'])
def org_profile():
    req = request.args.to_dict()
    print(req)
    return render_page()


def render_page():
    return render_template('org_profile.html')