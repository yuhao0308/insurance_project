import os
import pandas as pd
from sqlalchemy import create_engine

# Database connection details
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

# Create the database URL
db_url = f"postgresql://{db_config['user']}:{db_config['password']}@" \
    f"{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Query the data
query = """
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
"""
df = pd.read_sql_query(query, engine)

# Ensure the output directory exists
output_dir = './data'
os.makedirs(output_dir, exist_ok=True)

# Save the data to a CSV file
df.to_csv(os.path.join(output_dir, 'structured_data.csv'), index=False)
