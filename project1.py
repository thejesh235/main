from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model/house_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = int(request.form['area'])
    bedrooms = int(request.form['bedrooms'])

    prediction = model.predict([[area, bedrooms]])
    price = round(prediction[0], 2)

    return render_template('index.html', result=f"₹ {price}")

if __name__ == '__main__':
    app.run(debug=True)
