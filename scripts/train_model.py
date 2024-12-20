import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

# Load combined data
df = pd.read_csv('./data/combined_data.csv')

# Normalize column names to lowercase for consistency
df.columns = df.columns.str.lower()

# Preprocess data
df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
df['interaction_hour'] = pd.to_datetime(df['timestamp']).dt.hour

# One-hot encode 'interaction_type'
df = pd.get_dummies(df, columns=['interaction_type'])

# Define features and target
features = ['value', 'gender', 'interaction_hour'] + \
    [col for col in df.columns if col.startswith('interaction_type_')]
X = df[features]
y = df['claimfiled']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Ensure models directory exists
os.makedirs('./models', exist_ok=True)

# Save the model
with open('./models/ml_model.pkl', 'wb') as f:
    pickle.dump(model, f)
