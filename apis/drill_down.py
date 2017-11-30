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
    related_videos = get_related_videos(video['related_videos'])
    video_list = format_videos(related_videos)
    return render_page(video_list)


def render_page(video_list):
    return render_template('drill_down.html', video_list=video_list)


def get_related_videos(related_list):
    retval = []
    video_data = current_app.config['VIDEOS']
    for vid_id in related_list:
        retval.append(video_data[vid_id])
    return retval
