from flask import Flask, request
import pickle
import os 

# assets
filepath = './assets/iris_classifier/predictor.pkl'
target_classes = ['setosa', 'versicolor', 'virginica']
model = pickle.load(open(filepath, 'rb'))

app = Flask(__name__)

@app.route("/api/v1/status", methods=["GET"])
def status():
    return "OK!"

@app.route("/api/v1/predict_iris_type", methods=["GET","POST"])
def predict():
    pl = int(request.args.get('pl',''))
    pw = int(request.args.get('pw',''))
    sl = int(request.args.get('sl',''))
    sw = int(request.args.get('sw',''))
    pred = model.predict([[pl, pw, sl, sw]])
    print(pred)
    if pred:
        return target_classes[pred[0]]
    else:
        return 'Error!'
        # add error handling
        
if __name__ == "__main__":
    app.run(debug=True)