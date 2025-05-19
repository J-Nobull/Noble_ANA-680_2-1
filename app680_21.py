from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
with open("cancer_model.pkl", "rb") as f:
    scaler, model = pickle.load(f)

# Feature list
features = ["mean_radius", "mean_texture", "mean_perimeter", "mean_area", "mean_smoothness"]  # Adjust based on dataset

@app.route('/')
def home():
    return render_template('index.html', features=features)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = [float(request.form[feature]) for feature in features]
        values_scaled = scaler.transform([values])
        prediction = model.predict(values_scaled)[0]
        return f"The prediction is: {prediction}"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
    
