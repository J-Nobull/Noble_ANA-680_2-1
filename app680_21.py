from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
with open("cancer_model.pkl", "rb") as f:
    scaler, model = pickle.load(f)

# Feature list
features = [
    "Clump_thickness",
    "Uniformity_of_cell_size",
    "Uniformity_of_cell_shape",
    "Marginal_adhesion",
    "Single_epithelial_cell_size",
    "Bare_nuclei",
    "Bland_chromatin",
    "Normal_nucleoli",
    "Mitoses"
]

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
    
