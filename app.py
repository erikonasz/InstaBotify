from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(500)
def internal_server_error(error):
    return str(error), 500

if __name__ == "__main__":
    app.run()