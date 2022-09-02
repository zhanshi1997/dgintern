from flask import Flask, request,render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/') # access the homepage of some site
def home(): # define what the homepage looks like
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Total Balance for this year should be {} millions of dollars'.format(output))

if __name__ == "__main__":
    app.run(port = 5001, debug=True)