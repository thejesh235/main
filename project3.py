from flask import Flask, render_template, request, jsonify
import pickle
import webbrowser
from threading import Timer

app = Flask(__name__)

# Load ML model
model = pickle.load(open('model/house_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

# Form-based prediction (Browser)
@app.route('/predict', methods=['POST'])
def predict():
    area = int(request.form['area'])
    bedrooms = int(request.form['bedrooms'])

    prediction = model.predict([[area, bedrooms]])
    price = round(prediction[0], 2)

    return render_template('index.html', result=f"₹ {price}")

# 🔗 REST API (JSON)
@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()

    area = data['area']
    bedrooms = data['bedrooms']

    prediction = model.predict([[area, bedrooms]])
    price = round(prediction[0], 2)

    return jsonify({
        "predicted_price": price
    })

# Auto open browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)
