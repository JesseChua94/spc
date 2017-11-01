from flask import Blueprint, Flask
from apis.main import main

app = Flask(__name__)

app.register_blueprint(main, url="/")







app.debug = True

if __name__ == '__main__':
	app.run(host='0.0.0.0')



