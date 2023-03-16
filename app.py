# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 23:27:45 2023

@author: 91751
"""
import numpy as np 
from flask import Flask,request,jsonify,render_template,url_for

import pickle



app=Flask(__name__)
model=pickle.load(open('forest_pickle','rb'))

@app.route('/predict',methods=['POST'])
def predict():
    float_features = [int(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    output = prediction
    return render_template("index.html",data=prediction)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    
    output = prediction[0]
    return output

if __name__ == '__main__':
    app.run(port=5000)
    