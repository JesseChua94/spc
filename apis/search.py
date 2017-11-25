from flask import Blueprint, render_template, request, current_app
import re
search = Blueprint('Search', __name__)


@search.route('/search_input/', methods=['GET', 'POST'])
def search_input():
    req = request.form.to_dict()
    string = ",?" + req['input'] + ",?"

    return render_page(primary_search(string))


def primary_search(string):
    video_list = []
    video_data = current_app.config['VIDEOS']
    for video in video_data.values():
        match = re.search(string, str(video['primary_tags']))
        if not match:
            continue
        video_list.append({"id": video['id'],
                           "title": video['title'],
                           "thumbnail": video['thumbnail'],
                           "category": video['category'],
                           "description": video['description'],
                           "views": video['views'],
                           "date_created": video['date_created']})

    return video_list


def render_page(video_list):
    return render_template('results.html', video_list=[1,2,3,4,5])
