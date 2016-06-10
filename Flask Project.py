from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.secret_key = 'ifjrgdoiuertjiofgjohipijgtoijk'
    app.run(debug=True)
