from flask import Blueprint, render_template

main = Blueprint('Main', __name__)


@main.route('/')
def main_page():
    return render_page()

def render_page():
    return render_template('main.html',
                           videos_list=[{"category": "Category 1",
                                    "videos": [["active",1,2,3,4,5],
                                              ["",5,7]]}
                                   ,{"category": "Category 2",
                                    "videos": [["active", 1, 2, 3, 5],
                                              ["", 5, 7, 8]]}
                                   ]
                           )

