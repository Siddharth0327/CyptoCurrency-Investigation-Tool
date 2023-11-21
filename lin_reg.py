import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


data = pd.read_csv("C:\\Users\\arusu\\Desktop\\VIT SEM-7 MATERIALS\\LEAN STARTUP MANAGEMENT\\REVIEW-3 SMART CHAIR\\pressure_readings.csv")
le = LabelEncoder()
data['Encoded_label'] = le.fit_transform(data['label'])
data = data.drop('label',axis=1)

X = data.drop('Encoded_label', axis=1)
y = data['Encoded_label']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred_1 = model.predict([[38,4,11,11,34,5,28,40,40,23,28,6]])
print(y_pred_1)

# Evaluate the model's performance using mean squared error
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)