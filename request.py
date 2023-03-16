# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 23:56:14 2023

@author: 91751
"""

import requests

url = 'http://127.0.0.1:5000/predict'
r = requests.post(url,json={'State_Name':2,'District_Name':64,'Crop Year':1,'Season':4,'Crop':41,'Temperature':37,'humidity':40,'Soil moisture':46,'area':7356.0})

print(r.json())