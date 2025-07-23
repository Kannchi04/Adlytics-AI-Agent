import pandas as pd
import sqlite3
import os

# Define your CSV file paths and target SQL table names
files_and_tables = {
    r"C:\Adlytics-AI\data\product_ad_sales.csv": "ad_performance",
    r"C:\Adlytics-AI\data\product_eligibility.csv": "eligibility",
    r"C:\Adlytics-AI\data\product_total_sales.csv": "total_sales"
}


# SQLite database filename
db_file = "my_database.db"

# Optional: Delete existing DB for a clean start
if os.path.exists(db_file):
    os.remove(db_file)
    print(f"🧹 Old database '{db_file}' removed for clean start.")

# Connect to SQLite using context manager
with sqlite3.connect(db_file) as conn:
    for file_path, table_name in files_and_tables.items():
        try:
            # Load CSV
            df = pd.read_csv(file_path)

            # Write to SQLite
            df.to_sql(table_name, conn, if_exists="replace", index=False)

            # Confirm success
            print(f"✅ Loaded '{file_path}' into table '{table_name}'")
            print(f"   📄 Columns: {df.columns.tolist()}")
            print(f"   🔍 Sample data:\n{df.head(2)}\n")

        except Exception as e:
            print(f"❌ Failed to load '{file_path}' into table '{table_name}': {e}")

print("✅ All tables loaded successfully.")
