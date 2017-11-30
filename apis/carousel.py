from flask import current_app


def format_videos(categories):
    for category in range(len(categories)):
        video_rows = []
        video_row = ["active"]
        for video in categories[category]['videos']:
            video_row.append({"title": video['title'],
                              "id": video['id'],
                              "related_videos": video['related_videos'],
                              "category_id": video['category_id'],
                              "organization": video['organization'],
                              "organization_id": video['organization_id'],
                              "views": video['views'],
                              "date_created": video['date_created'],
                              "thumbnail": video['thumbnail']})

            if len(video_row) == current_app.config['VIDEO_ROW_LIMIT'] + 1 and len(video_rows) != 4:
                video_rows.append(video_row)
                video_row = [""]
        if len(video_row) > 1:
            video_rows.append(video_row)

        categories[category]['videos'] = video_rows
    return categories

