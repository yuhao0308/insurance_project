from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import pandas as pd

# Load the trained model
with open('../models/ml_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

# Add root route


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Validate input data
    required_fields = ['value', 'gender',
                       'interaction_type', 'interaction_hour']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields in input data'}), 400

    # Preprocess input data
    gender = 1 if data['gender'] == 'Male' else 0

    # All possible interaction types from the training data
    interaction_types = [
        'interaction_type_app_usage',
        'interaction_type_call_center',
        'interaction_type_chat_support',
        'interaction_type_customer_support_call',
        'interaction_type_email_open',
        'interaction_type_policy_update',
        'interaction_type_purchase',
        'interaction_type_social_media_mention',
        'interaction_type_survey_response',
        'interaction_type_website_visit'
    ]

    # Create input data dictionary
    input_data = {
        'value': [data['value']],
        'gender': [gender],
        'interaction_hour': [data['interaction_hour']]
    }

    # Set all interaction types to 0 initially
    for interaction in interaction_types:
        input_data[interaction] = [1 if interaction ==
                                   f'interaction_type_{data["interaction_type"]}' else 0]

    input_df = pd.DataFrame(input_data)

    # Make prediction
    prediction = model.predict(input_df)[0]
    return jsonify({'prediction': int(prediction)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
