from flask import Flask

app = Flask(__name__) # creating an object of Flass Class. This will be our WSGI application

#binding url to function using decorator
@app.route("/")
def index():
	return "Hello World"

def routing_example():
	return "Inroduction to Flask"

app.add_url_rule("/welcome", "routing_example", routing_example)	#binding url to function using add_url_rule method of app object

if __name__ == "__main__":
	app.run(debug=True)