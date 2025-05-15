# Breast Cancer Prediction App Deployment

This project provides a complete CI/CD pipeline to deploy an ML model for 
breast cancer prediction using the Wisconsin Breast Cancer dataset. 
The solution includes model selection, Flask web app development, 
GitHub Actions for CI/CD, and deployment to Heroku.

---

## Overview

This project retrains the best-performing 'rbf' Kernal ML algorithm on the same breast cancer dataset, 
saves the model as a pickle file, and serves predictions via a Flask web app. The app is deployed on 
Heroku, and CI/CD is managed via GitHub Actions.

---

## Dataset

- **Name:** Breast Cancer Wisconsin (Diagnostic) Data Set
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(original))
- **File:** `Breast_Cancer_Data.csv`

---

## Project Structure

```
Noble_ANA-680_2-1/
│
├── app.py                # Flask application
├── model.pkl             # Trained ML model (pickled)
├── requirements.txt      # Python dependencies
├── Procfile              # For Heroku deployment
├── py-app.yml            # GitHub Actions workflow file
├── templates/index       # Web form for user input
├── static                # (Optional) CSS/JS assets
└── Breast_Cancer_Data.csv
```

## Model Training

1. **Algorithm Selection**  
   The algorithm yielding the highest accuracy (Kernal ('rbf') was selected, retrained, and the model was saved as `model.pkl`.

2. **Saving the Model**  
   The trained model is serialized using `pickle` and loaded by the Flask app for inference.

## Flask App

- **`python-app.py`**  
  - Loads the trained model (`model.pkl`).
  - Renders `index.html` for user input.
  - Accepts user input, preprocesses it, runs prediction, and displays the result.

- **`templates/index.html`**  
  - Simple form for entering feature values.

## CI/CD with GitHub Actions

- **`.github/workflows/ci-cd.yml`**  
  - Installs dependencies.
  - Runs tests (if any).
  - Deploys to Heroku on push to main branch.

## Deployment to Heroku

- **`Procfile`**  
  - Specifies the command to run the Flask app on Heroku.

- **Deployment Steps:**  
  - App is automatically deployed via GitHub Actions when pushed to the main branch.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/Noble_ANA-680_2-1.git
   cd Noble_ANA-680_2-1
   ```

2. **Set up a Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```bash
   python app.py
   ```
   Access the app at `http://localhost:5000/`.

## Submitting URLs

- **GitHub Repository URL:**  
  Submit the URL of your project repository (e.g., `https://github.com/<your-username>/Noble_ANA-680_2-1`).

- **Heroku App URL:**  
  Submit the public Heroku URL for your deployed application.

## Troubleshooting

- If the application is not working:
  - Check the Heroku logs:  
    ```bash
    heroku logs --tail --app <your-heroku-app-name>
    ```
  - Review all error logs and describe the actions you took to troubleshoot the error.
  - Ensure all files (`Procfile`, `requirements.txt`, `model.pkl`, etc.) are present in the project root.

---

## References

- [UCI Breast Cancer Wisconsin Dataset](https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(original))
- [Heroku Flask Deployment Guide](https://devcenter.heroku.com/articles/getting-started-with-python)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

````
