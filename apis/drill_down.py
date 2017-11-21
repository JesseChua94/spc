from flask import Blueprint, render_template, request

drilldown = Blueprint('Drilldown', __name__)


@drilldown.route('/drill_down/', methods=['GET', 'POST'])
def drill_down():
    req = request.args.to_dict()
    print(req)
    return render_page()

def render_page():
    return render_template('drill_down.html')