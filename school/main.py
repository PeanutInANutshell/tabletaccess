from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
	return '<a href="https://www.google.com"> Google </a>'




if __name__ == '__main__':
	app.run()