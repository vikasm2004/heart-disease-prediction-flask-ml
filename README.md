## heart-disease-prediction-flask-ml

## 📌 Project Overview
This project is an **end-to-end Heart Disease Prediction web application** built using **Machine Learning (K-Nearest Neighbors)** and deployed with **Flask**.  
The application predicts whether a patient is at risk of heart disease based on key clinical attributes provided by the user.

The project demonstrates the complete ML workflow—from data preprocessing and model selection to deployment and real-time inference.

---

## 🧠 Machine Learning Model
- **Algorithm Used:** K-Nearest Neighbors (KNN)
- **Model Selection:**  
  - Performed **10-fold cross-validation** to determine the optimal value of `K`
  - Selected the best-performing `K` based on highest mean accuracy

- **Data Scaling:**  
  - Applied **MinMaxScaler** to normalize feature values for improved KNN performance

---

## 📊 Dataset Information
- **Dataset File:** `heart_final.csv`
- **Target Variable:** `target`  
  - `0` → No heart disease  
  - `1` → Presence of heart disease

- **Selected Features:**
  - ST Slope
  - Exercise Angina
  - Chest Pain Type
  - Maximum Heart Rate

These features were chosen based on their medical relevance and predictive importance.

---

## ⚙️ Project Workflow
1. Load and preprocess the dataset using **Pandas**
2. Normalize features using **MinMaxScaler**
3. Perform **cross-validation** to identify the best `K`
4. Split data into training and testing sets
5. Train the **KNN classifier**
6. Evaluate the model using:
   - Accuracy Score
   - Confusion Matrix
   - Classification Report
7. Deploy the trained model using **Flask**
8. Generate real-time predictions via a web interface

---

## 📈 Model Performance
- Model performance is evaluated on unseen test data
- Metrics used:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix

These metrics ensure the reliability and robustness of the classification model.

---

## 🌐 Web Application
- **Framework:** Flask
- **Frontend:** HTML
- **Features:**
  - User input form for clinical data
  - Real-time heart disease prediction
  - Simple and user-friendly interface

- **Routes:**
  - `/` → Home page
  - `/predict` → Prediction endpoint

---

## 🛠️ Technologies Used
- Python
- Flask
- Pandas
- Scikit-learn
- K-Nearest Neighbors (KNN)
- HTML/CSS

---
heart-disease-prediction-flask-ml/
│
├── app.py
│   # Main Flask application and prediction logic
│
├── heart_final.csv
│   # Dataset used for training the model
│
├── requirements.txt
│   # Python dependencies
│
├── README.md
│   # Project documentation
│
├── templates/
│   └── webpage.html
│       # Frontend HTML form for user input and results
│
├── static/
│   ├── css/
│   │   └── style.css
│   │       # Styling for the web interface
│   └── images/
│       └── app_screenshot.png
│           # Screenshot for README (optional but recommended)
│
├── model/
│   ├── knn_model.pkl
│   │   # Trained KNN model
│   └── scaler.pkl
│       # Saved MinMaxScaler for consistent inference
│
├── notebooks/
│   └── knn_model_training.ipynb
│       # EDA, feature selection, and cross-validation
│
├── utils/
│   └── preprocessing.py
│       # Data preprocessing and helper functions
│
└── .gitignore
    # Files and folders to ignore in Git


## ▶️ How to Run the Project Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction-flask-ml.git
