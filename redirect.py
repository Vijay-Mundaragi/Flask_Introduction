from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/info")
def info():
	return render_template("/redirect/info.html") 

@app.route("/welcome/<string:name>/<int:usn>")
def welcome(name, usn):
	return render_template("/redirect/hello.html", name=name, usn=usn)

#temporary redirect
@app.route("/")
def redirect_info():
	return redirect(url_for("info")) #default return code is 302


#moved permanenlty
@app.route("/hello")
def hello():
	return redirect(url_for("welcome", name="Admin", usn=100), code=301) # return code - 301


if __name__ == '__main__':
	app.run(debug=True)