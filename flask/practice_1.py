from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    paragraphs = ["section 1", "section 2", "section 3"]
    return render_template("index.html", title="Home page", data=paragraphs)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
