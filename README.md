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

## 📁 Project Structure
- heart-disease-prediction-flask-ml/
- │
- ├── app.py # Flask application
- ├── heart_final.csv # Dataset
- ├── templates/
- │ └── webpage.html # Frontend HTML page
- └── README.md # Project documentation
