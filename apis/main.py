from flask import Blueprint, render_template, current_app

main = Blueprint('Main', __name__)


@main.route('/')
def main_page():
    video_data = current_app.config['VIDEOS']
    category_data = current_app.config['CATEGORIES']
    video_list = []

    categories = sort_videos(video_data,category_data)

    # Format for output
    for i in range(len(categories)):
        cat_id = str(i + 1)
        video_row = categories[cat_id]
        video_list.append({"category": category_data[cat_id],
                           "videos": video_row})
    return render_page(video_list)


def render_page(video_list):
    # video_list = [{"category": "Category 1",
    #                 "videos": [["active",1,2,3,4,5],
    #                           ["",5,7]]},
    #                {"category": "Category 2",
    #                 "videos": [["active", 1, 2, 3, 5],
    #                           ["", 5, 7, 8]]}
    #                ]

    return render_template('main.html', video_list=video_list)


def sort_videos(video_data, category_data):
    categories = {}
    video_rows = [["active"] for _ in range(len(category_data))]

    # Sort videos into rows up to the limit by category. Add row to list if at limit
    for value in video_data.values():
        category = value['category_id']
        col = int(category) - 1
        if category not in categories:
            categories[category] = []

        video_rows[col].append({"title": value['title'],
                                "organization": value['organization'],
                                "views": value['views'],
                                "date_created": value['date_created'],
                                "thumbnail": value['thumbnail']})

        # If row at limit. Add to other rows with same category if no more than three rows already.
        if len(video_rows[col]) == current_app.config['VIDEO_ROW_LIMIT'] + 1 \
                and len(categories[category]) != current_app.config['VIDEO_ROW_DEPTH_LIMIT']:
            categories[category].append(video_rows[col])
            video_rows[col] = [""]

    # Adding incomplete rows that dont reach limit
    for index, row in enumerate(video_rows):
        if len(row) > 1:
            categories[str(index + 1)].append(row)

    return categories



