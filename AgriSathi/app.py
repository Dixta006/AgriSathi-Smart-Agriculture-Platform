import webbrowser
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/farmers")
def farmers():
    return render_template("farmers.html")

@app.route("/market")
def market():
    return render_template("market.html")

@app.route("/schemes")
def schemes():
    return render_template("schemes.html")

@app.route("/experts")
def experts():
    return render_template("experts.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")
@app.route("/chat")
def chat():
    return render_template("chat.html")

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
    
