from flask import Blueprint, render_template, request

search = Blueprint('Search', __name__)


@search.route('/search_input/', methods=['GET', 'POST'])
def search_input():
    req = request.form.to_dict()
    print(req)
    return render_page()

def render_page():
    return render_template('results.html')
