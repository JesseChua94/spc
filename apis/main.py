from flask import Blueprint, render_template, current_app
from .carousel import format_videos

main = Blueprint('Main', __name__)


@main.route('/')
def main_page():
    video_data = current_app.config['VIDEOS']
    sorted_videos = sort_main_categories(video_data.values())
    video_list = format_videos(5, sorted_videos)
    return render_page(video_list)


def render_page(video_list):
    return render_template('main.html', video_list=video_list)


# output
# video_list = [{"category": "Category 1",
#                 "videos": [["active",1,2,3,4,5],
#                           ["",5,7]]},
#                {"category": "Category 2",
#                 "videos": [["active", 1, 2, 3, 5],
#                           ["", 5, 7, 8]]}
#                ]

def sort_main_categories(video_data):
    category_data = current_app.config['CATEGORIES']
    categories = {}
    for video in video_data:
        category = video['category_id']
        if category not in categories:
            categories[category] = []
        video_limit = 5 * \
            current_app.config['VIDEO_ROW_DEPTH_LIMIT']
        if len(categories[category]) != video_limit:
            categories[category].append(video)

    sorted_videos = [{"category": category_data[cat_id],
                      "videos": categories[cat_id]} for cat_id in category_data]

    return sorted_videos




