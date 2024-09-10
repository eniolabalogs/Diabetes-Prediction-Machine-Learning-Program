// src/DiabetesPrediction.js
import React, { useState } from 'react';
import './DiabetesPrediction.css';

const DiabetesPrediction = () => {
  const [formData, setFormData] = useState({
    Pregnancies: '',
    Glucose: '',
    BloodPressure: '',
    SkinThickness: '',
    Insulin: '',
    BMI: '',
    DiabetesPedigreeFunction: '',
    Age: '',
  });

  const [result, setResult] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Send a POST request to the Flask backend
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': 'http://127.0.0.1:5000/predict' },
        body: JSON.stringify({
          pregnancies: Number(formData.Pregnancies),
          glucose: Number(formData.Glucose),
          bloodPressure: Number(formData.BloodPressure),
          skinThickness: Number(formData.SkinThickness),
          insulin: Number(formData.Insulin),
          bmi: Number(formData.BMI),
          diabetesPedigreeFunction: Number(formData.DiabetesPedigreeFunction),
          age: Number(formData.Age),
        }),
      });

      // Check if the response is ok
      if (!response.ok) {
        throw new Error('Failed to fetch prediction');
      }

      // Extract JSON data from the response
      const data = await response.json();
      setResult(data.prediction);
    } catch (error) {
      setResult('An error occurred: ' + error.message);
    }
  };

  return (
    <div className="container">
      <h2>Diabetes Prediction System</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <div className="input-group" key={key}>
            <label>{key.replace(/([A-Z])/g, ' $1')}</label>
            <input
              type="number"
              name={key}
              value={formData[key]}
              onChange={handleChange}
              required
            />
          </div>
        ))}
        <button type="submit">Predict</button>
      </form>
      {result && <div className="result">{result}</div>}
    </div>
  );
};

export default DiabetesPrediction;
