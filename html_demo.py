from flask import Flask

app = Flask(__name__)

@app.route("/")
def html_demo():
	html = """
			<h1>Author List</h1>
			{author_list}
	"""
	authors_list = ["ABC", "PQR", "XYZ"]
	data = "<ul>"
	data += "\n".join(["<li>{author}</li>".format(author = author) for author in authors_list])
	data +="</ul>"

	return html.format(author_list=data)

if __name__ == "__main__":
	app.run(debug=True)