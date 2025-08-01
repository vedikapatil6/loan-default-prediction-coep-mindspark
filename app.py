from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the trained model at startup
model = joblib.load('rf_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    data = request.form

    # Prepare input data for prediction
    input_data = [
        float(data['age']),
        float(data['income']),
        float(data['loan_amount']),
        int(data['education']),
        int(data['employment']),
        int(data['marital']),
        int(data['mortgage']),
        int(data['dependents']),
        int(data['purpose']),
        int(data['cosigner'])
    ]

    # Make prediction
    prediction = model.predict([input_data])
    result = 'Default' if prediction[0] == 1 else 'No Default'
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)  # Change to debug=False for production