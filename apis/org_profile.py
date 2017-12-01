from flask import Blueprint, render_template, request, current_app
from .carousel import format_videos
from .main import sort_main_categories

organization = Blueprint('Organization', __name__)


@organization.route('/organization_profile/', methods=['GET', 'POST'])
def org_profile():
    req = request.args.to_dict()
    org_id = "1"
    org = current_app.config['ORGANIZATIONS'][org_id]

    org_videos = get_organization_videos(org_id)
    sorted_videos = sort_main_categories(org_videos)
    video_list = format_videos(5, sorted_videos)

    return render_page(org, video_list)


def render_page(org, video_list):
    return render_template('org_profile.html', org=org, video_list=video_list)


def get_organization_videos(org_id):
    video_data = current_app.config['VIDEOS']
    org_videos = []
    for video in video_data.values():
        org_videos.append(video) if video['organization_id'] == org_id else ""
    return org_videos
