from flask import Blueprint, render_template, request, current_app
import re
search = Blueprint('Search', __name__)


@search.route('/search_input/', methods=['GET', 'POST'])
def search_input():
    req_string = request.form.to_dict()
    input = req_string['input']
    if not input:
        return render_page([], "")
    query_string = ",?" + input + ",?"

    return render_page(primary_search(query_string), input)


def primary_search(string):
    video_list = []
    video_data = current_app.config['VIDEOS']
    for video in video_data.values():
        match = re.search(string.lower(), str(video['primary_tags']).lower())
        if not match:
            continue
        category = current_app.config['CATEGORIES'][video['category_id']]
        video_list.append({"id": video['id'],
                           "title": video['title'],
                           "thumbnail": video['thumbnail'],
                           "organization": video['organization'],
                           "organization_id": video['organization_id'],
                           "category": category,
                           "description": video['description'],
                           "views": video['views'],
                           "date_created": video['date_created']})

    return video_list


def render_page(video_list, req_string):
    return render_template('results.html', video_list=video_list, req=req_string)
