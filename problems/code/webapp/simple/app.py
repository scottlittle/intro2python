from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Nobody expects the Spanish Inquisition!"

if __name__ == "__main__":
    app.run(debug=True)
