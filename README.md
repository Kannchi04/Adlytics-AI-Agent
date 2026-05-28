# 📈 Adlytics AI Agent

Adlytics AI Agent is an AI-powered analytics assistant designed for e-commerce campaign analysis.
It enables users to ask natural language questions about advertising and sales data, automatically converts those queries into SQL using Google Gemini AI, executes them on a SQLite database, and generates interactive visual insights using Streamlit and Plotly.

---

## 🚀 Features

* 🤖 Natural Language to SQL conversion using Gemini AI
* 📊 Interactive dashboard built with Streamlit
* 🧠 AI-generated campaign insights
* 📈 Automatic chart generation (bar, line, scatter, pie, histogram)
* 🗄 SQLite database integration
* ⚡ Real-time ad performance analysis
* 📉 Sales trend and campaign breakdown visualization

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **SQLite**
* **Google Gemini API**
* **Pandas**
* **Plotly Express**

---

## 📂 Project Structure

```bash
Adlytics-AI-Agent/
│── app.py                 # Streamlit frontend dashboard
│── agent_ai.py            # AI agent for SQL generation
│── setup.py               # Database setup script
│── my_database.db         # SQLite database
│── requirements.txt
│── data/
│   ├── product_ad_sales.csv
│   ├── product_eligibility.csv
│   └── product_total_sales.csv
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Adlytics-AI-Agent.git
cd Adlytics-AI-Agent
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Gemini API Key

Replace the API key in `agent_ai.py`:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

### 4️⃣ Setup the Database

```bash
python setup.py
```

### 5️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

## Example Queries

* “Show total sales by item”
* “Which products generated the highest ad revenue?”
* “Compare ad spend vs ad sales”
* “Show weekly sales trends”
* “Breakdown sales distribution by category”

---

## 📊 Visualization Support

The application automatically selects visualizations based on query intent:

| Query Type           | Visualization   |
| -------------------- | --------------- |
| Trends / Time-series | Line Chart      |
| Comparisons          | Bar Chart       |
| Distributions        | Pie / Histogram |
| Multi-variable Data  | Scatter Plot    |

---

## How It Works

1. User enters a natural language business query.
2. Gemini AI converts the query into SQL.
3. SQL executes on the SQLite database.
4. Results are transformed into interactive visualizations.
5. Insights are displayed through the Streamlit dashboard.

---

## Future Improvements

* Multi-database support (PostgreSQL, MySQL)
* Conversational memory for follow-up questions
* Advanced KPI dashboards
* Export insights to PDF/Excel
* User authentication & role-based access
* Cloud deployment support

---

## 📸 Demo Preview

<img width="1814" height="830" alt="image" src="https://github.com/user-attachments/assets/476429ce-f5d0-4ff9-9e26-6310c22b622c" />

---

## 👩‍💻 Author

Developed by Kannchi Maithil
AI + Data Analytics Enthusiast 

---
