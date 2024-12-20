# Insurance Claim Prediction System

## Overview
This project implements a machine learning-based system to predict the likelihood of an insurance claim filing based on customer interactions. It handles both structured and unstructured data and provides real-time prediction capabilities through a web interface.

## Features
- **Data pipeline for processing customer interaction data**
- **Machine learning model for claim prediction**
- **Web interface for real-time predictions**
- **Support for multiple interaction types**
- **Integration with a PostgreSQL database**
- **PySpark processing for unstructured data**

## System Requirements
- **Python 3.8+**
- **PostgreSQL**
- **Apache Spark**

### Required Python Packages
```bash
pip install flask flask-cors pandas scikit-learn pyspark sqlalchemy psycopg2-binary
```

## Project Structure
```
.
├── data/
│   ├── structured_data.csv
│   ├── unstructured_data.csv
│   └── combined_data.csv
├── models/
│   └── ml_model.pkl
├── scripts/
│   ├── extract_data.py
│   ├── process_unstructured.py
│   ├── combine_data.py
│   ├── train_model.py
│   └── flask_api.py
└── templates/
    └── index.html
```

## Setup and Configuration
### Database Configuration
```python
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
```

## Data Pipeline
### 1. Data Extraction
Extracts customer and claim data from the PostgreSQL database:
```sql
SELECT
    c.CustomerID,
    c.FirstName,
    c.LastName,
    c.Gender,
    cl.ClaimDate,
    cl.SettlementDate
FROM Customer c
LEFT JOIN Contract co ON c.CustomerID = co.CustomerID
LEFT JOIN Claim cl ON co.ContractID = cl.ContractID;
```

### 2. Unstructured Data Processing
Processes JSON interaction data using PySpark:
```python
# Define schema explicitly
schema = StructType([
    StructField("CustomerID", IntegerType(), True),
    StructField("interaction_type", StringType(), True),
    StructField("value", FloatType(), True),
    StructField("timestamp", TimestampType(), True)
])
```

### 3. Data Combination
Merges structured and unstructured data:
```python
# Combine datasets on 'customerid'
combined_df = pd.merge(
    structured_df,
    unstructured_df,
    on='customerid',
    how='inner'
)
```

## Machine Learning Model
The system uses a **Random Forest Classifier** with the following features:
- Customer interaction value
- Gender
- Interaction hour
- Interaction type (one-hot encoded)

### Model Training Code Example
```python
# Define features and target
features = ['value', 'gender', 'interaction_hour'] + \
    [col for col in df.columns if col.startswith('interaction_type_')]
X = df[features]
y = df['claimfiled']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)
```

## Web Interface
A user-friendly web interface is provided for making predictions:

```html
<h2 class="mb-4">Insurance Claim Prediction</h2>
<div class="alert alert-info">
  <h5>About this Prediction Tool</h5>
  <p>This tool predicts whether a customer is likely to file an insurance claim based on their interaction data.</p>
  <p><strong>Output:</strong> The prediction will indicate if the customer is likely or unlikely to file a claim based on the provided information.</p>
</div>
```

## API Endpoints
### `GET /`
- Returns the prediction interface (HTML page)

### `POST /predict`
- Accepts customer interaction data
- Returns prediction result (JSON)

**Request Body Example:**
```json
{
    "value": 200,
    "gender": "Male",
    "interaction_type": "purchase",
    "interaction_hour": 14
}
```

**Response Example:**
```json
{
    "prediction": 1
}
```

## Supported Interaction Types
- App Usage
- Call Center
- Chat Support
- Customer Support Call
- Email Open
- Policy Update
- Purchase
- Social Media Mention
- Survey Response
- Website Visit

## Data Format
**Unstructured Interaction Data Example:**
```json
{"CustomerID": 1, "interaction_type": "app_usage", "value": 5, "timestamp": "2024-12-09T10:00:00Z"},
{"CustomerID": 2, "interaction_type": "purchase", "value": 200, "timestamp": "2024-12-10T11:00:00Z"},
{"CustomerID": 3, "interaction_type": "survey_response", "value": 4, "timestamp": "2024-12-11T12:00:00Z"},
{"CustomerID": 4, "interaction_type": "email_open", "value": 3, "timestamp": "2024-12-12T13:00:00Z"},
{"CustomerID": 5, "interaction_type": "chat_support", "value": 2, "timestamp": "2024-12-13T14:00:00Z"}
```

## Running the Application

### Extract and Process Data
```bash
python scripts/extract_data.py
python scripts/process_unstructured.py
python scripts/combine_data.py
```

### Train the Model
```bash
python scripts/train_model.py
```

### Start the Flask Application
```bash
python scripts/flask_api.py
```

**Access the web interface at:** [http://localhost:5001](http://localhost:5001)

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- **Flask** for the web framework
- **scikit-learn** for machine learning capabilities
- **Apache Spark** for big data processing
- **Bootstrap** for the frontend interface

