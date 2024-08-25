from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_w():
    return render_template('index.html')

app.run(host='127.0.0.1', port='4011', debug=True)
# if __name__ == "__main__":
    # app.run(host='127.0.0.1', port='4011')