from flask import Blueprint, render_template, request, current_app
from .carousel import format_videos
import json

drilldown = Blueprint('Drilldown', __name__)


@drilldown.route('/drill_down/', methods=['GET', 'POST'])
def drill_down():
    req = request.args.to_dict()
    if not req['video']:
        return "Didn't select a video"
    video = json.loads(req['video'].replace("\'", "\""))
    print(video)
    related_videos = get_related_videos(video['related_videos'])
    video_list = format_videos(3, [{"category": "Related videos", "videos": related_videos}])
    comments = get_video_comments(video['comments'])
    return render_page(video_list, comments)


def render_page(video_list, comments):
    return render_template('drill_down.html', video_list=video_list, comments=comments)


def get_related_videos(related_list):
    video_data = current_app.config['VIDEOS']
    return [video_data[vid_id] for vid_id in related_list]


def get_video_comments(video_comments):
    comment_data = current_app.config['COMMENTS']
    return [comment_data[comment_id] for comment_id in video_comments]
