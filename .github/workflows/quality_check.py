import pandas as pd
import os

# Define the data file
data_file = "data.csv"

# Check if file exists
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
    print("✅ Data file exists. Quality check passed.")
else:
    print("❌ Data file not found. Quality check failed.")
    exit(1)  # Exit with error code
