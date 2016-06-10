from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/test")
def test():
    mail = "me@tbmc.fr"
    t = "truc"
    return "test : {} --- {}".format(mail, t)

if __name__ == '__main__':
    app.secret_key = 'ifjrgdoiuertjiofgjohipijgtoijk'
    app.run(debug=True)
