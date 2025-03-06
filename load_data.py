import snowflake.connector
import pandas as pd
import os

# Get credentials from environment variables
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT
)

# Create a cursor object
cur = conn.cursor()

# Create a test table (if not exists)
cur.execute("""
    CREATE TABLE IF NOT EXISTS demo_table (
        id INT,
        name STRING
    )
""")

# Insert sample data
cur.execute("INSERT INTO demo_table (id, name) VALUES (1, 'GitHub Actions')")

# Fetch and print data
cur.execute("SELECT * FROM demo_table")
for row in cur.fetchall():
    print(row)

# Close the connection
cur.close()
conn.close()
