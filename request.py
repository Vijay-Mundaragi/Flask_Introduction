from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def request_info():
	return render_template("/request/info.html")


if __name__ == '__main__':
	app.run(debug=True)