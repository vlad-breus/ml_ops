from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import pickle

# train and save a model for iris
data = load_iris()
X = data['data']
y = data['target']

# split and preprocess data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_pred, y_test))

# dump model and scaler to file
pickle.dump(model, open('assets/iris_classifier/predictor.pkl', 'wb'))