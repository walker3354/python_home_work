from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home_page')
def index():
    paragraphs = ["section 1", "section 2", "section 3"]
    return render_template("index.html", title="Home page", data=paragraphs)


@app.route('/about_page')
def about():
    return "<h1>About page</h1>"


if __name__ == '__main__':
    app.run(debug=True, port=3000)
