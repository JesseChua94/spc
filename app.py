from flask import Flask
from apis.main import main
from apis.search import search
from apis.drill_down import drilldown

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(search)
app.register_blueprint(drilldown)

app.debug = True

if __name__ == '__main__':
	app.run(host='0.0.0.0')



