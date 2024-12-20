import pandas as pd

# Load datasets
structured_df = pd.read_csv('./data/structured_data.csv')
unstructured_df = pd.read_csv('./data/unstructured_data.csv')

# Print columns for debugging
# print("Columns in structured_df:", structured_df.columns.tolist())
# print("Columns in unstructured_df:", unstructured_df.columns.tolist())

# Normalize column names to lowercase for consistency
structured_df.columns = structured_df.columns.str.lower()
unstructured_df.columns = unstructured_df.columns.str.lower()

# Print normalized columns
# print("Normalized columns in structured_df:", structured_df.columns.tolist())
# print("Normalized columns in unstructured_df:",
#       unstructured_df.columns.tolist())

# Handle date columns
structured_df['claimdate'] = pd.to_datetime(
    structured_df['claimdate'], errors='coerce')
structured_df['settlementdate'] = pd.to_datetime(
    structured_df['settlementdate'], errors='coerce')
unstructured_df['timestamp'] = pd.to_datetime(
    unstructured_df['timestamp'], errors='coerce')

# Create target variable: Has the customer filed a claim?
structured_df['claimfiled'] = structured_df['claimdate'].notnull().astype(int)

# Combine datasets on 'customerid'
combined_df = pd.merge(
    structured_df,
    unstructured_df,
    on='customerid',
    how='inner'
)

# Save combined dataset
combined_df.to_csv('./data/combined_data.csv', index=False)
# print("Combined data saved to './data/combined_data.csv'.")
