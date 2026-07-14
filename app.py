from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

# ==========================================
# Flask App
# ==========================================

app = Flask(__name__)

# ==========================================
# Load Model and Scaler
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "models", "floods.save"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "transform.save"))

# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("home.html")

# ==========================================
# Prediction Page
# ==========================================

@app.route("/predict")
def predict_page():
    return render_template("index.html")

# ==========================================
# Prediction
# ==========================================

@app.route("/prediction", methods=["POST"])
def prediction():

    temp = float(request.form["Temp"])
    humidity = float(request.form["Humidity"])
    cloud = float(request.form["CloudCover"])
    annual = float(request.form["Annual"])
    janfeb = float(request.form["JanFeb"])
    marmay = float(request.form["MarMay"])
    junsep = float(request.form["JunSep"])
    octdec = float(request.form["OctDec"])
    avgjune = float(request.form["AvgJune"])
    sub = float(request.form["Sub"])

    data = pd.DataFrame([[
        temp,
        humidity,
        cloud,
        annual,
        janfeb,
        marmay,
        junsep,
        octdec,
        avgjune,
        sub
    ]],
    columns=[
        "Temp",
        "Humidity",
        "Cloud Cover",
        "ANNUAL",
        "Jan-Feb",
        "Mar-May",
        "Jun-Sep",
        "Oct-Dec",
        "avgjune",
        "sub"
    ])

    scaled = scaler.transform(data)

    prediction = model.predict(scaled)[0]

    if prediction == 1:
        return render_template("chance.html")

    return render_template("no_chance.html")

# ==========================================
# Run App
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)