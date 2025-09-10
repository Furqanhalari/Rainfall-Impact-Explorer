from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load dataset once (for preview on homepage)
df = pd.read_csv("data/merged_data.csv")

@app.route("/")
def home():
    # Show first 5 rows as preview
    preview_data = df.head().to_html(classes="table table-striped", index=False)
    return render_template("index.html", preview_data=preview_data)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
