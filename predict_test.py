#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

shell = {
    'sex' :'M',
    'length' : 0.2,
    'height' :0.2,
    'whole_weight': 0.40
}

response = requests.post(url, json=shell).json()
print(response)

print('Abalone Age is = {} \n'.format( response))
print('Abalone Rings = {}'.format(response - 1.5))
