from flask import Flask
from apis.main import main
from apis.search import search
from apis.drill_down import drilldown
from apis.org_profile import organization
import json

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(search)
app.register_blueprint(drilldown)
app.register_blueprint(organization)

app.config['VIDEO_ROW_DEPTH_LIMIT'] = 3

json_data = open(app.root_path + '/videos.json')
app.config['VIDEOS'] = json.load(json_data)
json_data = open(app.root_path + '/categories.json')
app.config['CATEGORIES'] = json.load(json_data)
json_data = open(app.root_path + '/organizations.json')
app.config['ORGANIZATIONS'] = json.load(json_data)
json_data = open(app.root_path + '/comments.json')
app.config['COMMENTS'] = json.load(json_data)

app.debug = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)



