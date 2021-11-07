import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model_n_estimators=400.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)
    
app = Flask('abalone')

@app.route('/predict', methods=['POST'])
def predict():
    
    shell = request.get_json()
    
    X = dv.transform([shell])
    y_pred = model.predict(X)[0]

    result = {
        'Abalone Age is': y_pred,
        'Abalone Rings': y_pred - 1.5
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)