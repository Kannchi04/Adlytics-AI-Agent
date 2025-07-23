import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key="AIzaSyBkVqMJSQeJJaJnkSYQWfMdfFGSGQDT5SI")

def get_schema(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    schema = []
    for (table_name,) in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
        schema.append(f"Table: {table_name}")
        for column in cursor.execute(f"PRAGMA table_info({table_name});"):
            schema.append(f"  {column[1]} ({column[2]})")
        schema.append("")
    conn.close()
    return "\n".join(schema)

def get_sql_query(question, schema):
    prompt = f"""
You are a senior SQL analyst.

You are working with a SQLite database that contains three tables:

1. ad_performance – This table tracks ad-related performance metrics:
   - `item_id`: Unique ID for the item
   - `clicks`: Number of ad clicks
   - `impressions`: Number of times the ad was shown
   - `ad_spend`: Total money spent on ads
   - `ad_sales`: Sales directly from ads (ad-driven revenue)

2. total_sales – This table tracks actual sales figures regardless of ad spend:
   - `item_id`: Unique ID for the item
   - `total_sales`: Total revenue generated (not limited to ad performance)

3. products – This table contains product catalog information:
   - `item_id`: Unique ID for the item
   - `product_name`: Name of the product
   - `category`: Category of the product
   - `price`: Retail price

📌 Guidelines for column usage:
- Use **`ad_performance.ad_sales`** only when the question is specifically about **sales from ads**.
- Use **`total_sales.total_sales`** when the question is about **overall revenue or total sales**.
- Use **`products`** when product names, categories, or prices are needed for context or filtering.

🛑 Important: There is NO table called `products`. Do NOT use or reference `products`, `product_name`, `category`, or `price`.

📌 If the user question uses the word **"product"**, return the `item_id` instead (assume product = item).

Write a syntactically correct SQL query to answer this user question:
"{question}"

💡 Only return the SQL query — no markdown, no explanations, no triple backticks.
"""

    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    response = model.generate_content(prompt)
    sql_query = response.text.strip()

    if "```" in sql_query:
        sql_query = sql_query.split("```")[-2].strip()
    if sql_query.lower().startswith("sql"):
        sql_query = sql_query[3:].strip()

    return sql_query


def run_query(db_path, sql):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        return [f"❌ Error: {str(e)}"]
    finally:
        conn.close()

def main():
    db_path = "C:\\Adlytics-AI\\my_database.db"
    if not os.path.exists(db_path):
        print("❌ Database file not found.")
        return

    print("✅ Model and database are ready.")
    print("🤖 You can now ask questions about your data.")
    print("💡 Type 'exit' to quit.\n")

    schema = get_schema(db_path)

    while True:
        question = input("❓ Your question: ").strip()
        if question.lower() == "exit":
            break

        sql = get_sql_query(question, schema)
        print("\n📜 SQL Generated:\n", sql)

        result = run_query(db_path, sql)
        print("\n📊 Result:\n", result)
        print("-" * 50)

if __name__ == "__main__":
    main()
