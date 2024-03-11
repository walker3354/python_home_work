from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    webpage_title = "walker's first flask"
    return render_template("index.html", title=webpage_title)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
