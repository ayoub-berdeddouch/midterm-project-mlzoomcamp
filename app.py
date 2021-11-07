from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model_file = 'model_n_estimators=400.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)
    


@app.route('/')
def hello_world():
    return render_template("Abalone_age.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    # int_features=[int(x) for x in request.form.values()]
    # final=[np.array(int_features)]
    # print(int_features)
    # print(final)

    if request.method == 'GET':
        return (render_template('Abalone_age.html'))
    
    if request.method =='POST':
        
        # Get inputs
        
        #gender as string
        s_sex = request.form['Sex']
        s_length = float(request.form['Length'])
        s_height = float(request.form['Height'])
        s_whole_weight = float(request.form['Whole_weight'])

        shell = {
                'sex' :s_sex,
                'length' : s_length,
                'height' :s_height,
                'whole_weight': s_whole_weight
            }

        X = dv.transform([shell])
        y_pred = model.predict(X)[0]

        result = {
            'Abalone Age is': y_pred,
            'Abalone Rings': y_pred - 1.5
        }

        return render_template('Abalone_age.html',pred='The Sea Shell Prediction are:\n Abalone Age is {} years, and number of Rings is: {}'.format(float(y_pred),int(y_pred - 1.5)),bhai="danger")


if __name__ == '__main__':
    app.run(debug=True)
