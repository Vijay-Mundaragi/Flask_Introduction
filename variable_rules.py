from flask import Flask

app = Flask(__name__)

@app.route("/welcome/<name>")
def welcome_name(name):
	return "Welcome %s!" % name

@app.route("/int/<int:number>")
def print_number(number):
	return "You entered %d number" % number

@app.route("/float/<float:number>")
def print_float_number(number):
	return "You entered %f number" % number

@app.route("/canonical_url/")
def canonical_path():
	return "/canonical_url and /canonical_url/ both return same output"

if __name__ == "__main__":
	app.run(debug=True)
