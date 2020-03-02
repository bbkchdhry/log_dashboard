from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
