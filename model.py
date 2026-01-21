from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

df = pd.read_csv('./heart_final.csv')

selected_features = ['ST slope', 'exercise angina', 'chest pain type', 'max heart rate']
x = df[selected_features]
y = df['target']

scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

k_range = range(1,31)
cv_score = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    score = cross_val_score(knn, x_scaled, y, cv=10, scoring='accuracy')
    cv_score.append(score.mean())

best_score = max(cv_score)
best_index = cv_score.index(best_score)
best_k = k_range[best_index]

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.3, random_state=42)

model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
class_rep = classification_report(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {acc:.2f}')
print('\nClassification Report:\n', class_rep)
print('\nConfusion Matrix:\n', cm)

@app.route('/')
def home():
    return render_template('webpage.html')

@app.route('/predict', methods=['POST'])
def predict():
    st_slope = float(request.form['st_slope'])
    ex_agina = float(request.form['exercise_agina'])
    cp_type = float(request.form['chest_pain_type'])
    max_hr = float(request.form['max_heart_rate'])

    input_data = [[st_slope, ex_agina, cp_type, max_hr]]

    prediction = model.predict(input_data)

    predicted_class = prediction[0]

    result = str(predicted_class)
    
    return render_template('webpage.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
