from email.mime import application
from email.mime.multipart import MIMEMultipart
import flask
from flask import Flask, jsonify, request
import json
from API.Getting_Data_To_API import API_Data
import numpy as np
import pickle

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])

def predict():
    request_json = request.get_json()
    x = request_json['input']
    xin = np.array(x).reshape(1,-1)
    model = load_models()
    prediction = model.predict(xin)[0]
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)