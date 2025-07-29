
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = [float(x) for x in request.form.values()]
    prediction = model.predict([np.array(data)])
    return render_template("index.html", prediction_text=f"Predicted Iris Species: {prediction[0]}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

