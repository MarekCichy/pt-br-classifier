from flask import Flask, jsonify,request
from flask_cors import CORS
from joblib import load

#specific path for PythonAnywhere
classifier = load('/home/Mariankowlak/mysite/ptclassifier.joblib')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route("/predict/",methods=['GET'])
def return_price():
    text = request.args.get('text')
    prediction = classifier.predict([text])
    proba = classifier.predict_proba([text])
    if (prediction[0] == 0):
        prediction = 'PT'
        confidence = proba[0][0]
    else:
        prediction = 'BR'
        confidence = proba[0][1]

    classifier.predict_proba([text])
    pred_dict = {
                'sotaque': prediction,
                'confidence' : confidence
            }
    return jsonify(pred_dict)