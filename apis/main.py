from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def test():
    return render_template('main.html', videos=[["active",1,2,3,4],["",5,6,7,8]])

