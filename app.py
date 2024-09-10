from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
from training_program import scaler, classifier
import numpy as np

app = Flask(__name__)

CORS(app)

@app.route('/predict', methods=['GET','POST', 'OPTIONS'])
def predict_diabetes():
    # Automatically handle OPTIONS requests via Flask-CORS
    if request.method == 'OPTIONS':
        # CORS should automatically handle this, but this return ensures the server is working correctly
        return jsonify({"status": "CORS preflight successful"}), 200

    try:
        # Extract JSON data from the request body
        data = request.json
        input_data = [
            data.get('pregnancies', 0),
            data.get('glucose', 0),
            data.get('bloodPressure', 0),
            data.get('skinThickness', 0),
            data.get('insulin', 0),
            data.get('bmi', 0),
            data.get('diabetesPedigreeFunction', 0),
            data.get('age', 0)
        ]

        # Convert input data to numpy array and reshape
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Standardize data and make a prediction
        std_data = scaler.transform(input_data_reshaped)
        prediction = classifier.predict(std_data)

        # Return prediction result as JSON
        result = "The person is likely non-diabetic" if prediction[0] == 0 else "The person is  likely diabetic"
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
