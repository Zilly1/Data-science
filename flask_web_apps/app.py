from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():

    return "<p>Hello, World! How are you? fine thank you We are learning coding with Codanics</p>"
if __name__ == "__main__":
    app.run(debug=True)
