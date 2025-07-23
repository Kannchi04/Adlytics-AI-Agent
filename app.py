import streamlit as st
import pandas as pd
import plotly.express as px
import time
from agent_ai import get_schema, get_sql_query, run_query
import os

db_path = "C:\\Adlytics-AI\\my_database.db"
if not os.path.exists(db_path):
    st.error("❌ Database file not found.")
    st.stop()

schema = get_schema(db_path)


st.set_page_config(page_title="Adlytics AI", layout="wide", page_icon="📈")

st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>📈 Adlytics AI</h1>
    <p style='text-align: center; font-size: 18px;'>Your personal AI agent for e-commerce campaign analysis.</p>
    <hr style="border:1px solid #ccc;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])
with col1:
    question = st.text_input("🔍 Ask me a question about sales, ads, products...",
                           placeholder="E.g., 'Show me total sales by product'")

with col2:
    if question.strip():
        st.markdown("<p style='color: green;'>🟢 Ready to analyze</p>", unsafe_allow_html=True)


submit = st.button("🚀 Submit", type="primary")

if submit and question.strip():
    with st.spinner("🤖 Analyzing your campaign data..."):
        try:
            sql = get_sql_query(question, schema)
            result = run_query(db_path, sql)

            st.subheader("🧠 Insights:")
            st.code(sql, language="sql")

            if isinstance(result, list) and isinstance(result[0], str) and result[0].startswith("❌"):
                st.error(result[0])
                st.stop()

            result_df = pd.DataFrame(result)

            if result_df.empty:
                st.info("ℹ️ No data returned for this query.")
                st.stop()

            st.subheader("📊 Data Visualization")
            with st.expander("📄 View Raw Data"):
                st.dataframe(result_df)

            result_df.columns = [f"Column {i+1}" for i in range(len(result_df.columns))]  # Rename generic

            q_lower = question.lower()

            if len(result_df) == 1 and len(result_df.columns) == 1:
                value = result_df.iloc[0, 0]
                st.metric(label="Result", value=f"{value:,.2f}")

            elif any(col in q_lower for col in ['trend', 'over time', 'daily', 'weekly']) and len(result_df.columns) >= 2:
                fig = px.line(result_df, x=result_df.columns[0], y=result_df.columns[1])
                st.plotly_chart(fig, use_container_width=True)

            elif any(term in q_lower for term in ['compare', 'versus', 'vs', 'by']) and len(result_df.columns) >= 2:
                if len(result_df) > 8:
                    fig = px.bar(result_df, y=result_df.columns[0], x=result_df.columns[1], orientation='h')
                else:
                    fig = px.bar(result_df, x=result_df.columns[0], y=result_df.columns[1])
                st.plotly_chart(fig, use_container_width=True)

            elif any(term in q_lower for term in ['distribution', 'breakdown']) and len(result_df.columns) >= 1:
                if len(result_df.columns) == 1:
                    fig = px.histogram(result_df, x=result_df.columns[0])
                else:
                    fig = px.pie(result_df, names=result_df.columns[0], values=result_df.columns[1])
                st.plotly_chart(fig, use_container_width=True)

            elif len(result_df.columns) >= 2:
                if len(result_df) > 15:
                    fig = px.scatter(result_df, x=result_df.columns[0], y=result_df.columns[1])
                else:
                    fig = px.bar(result_df, x=result_df.columns[0], y=result_df.columns[1])
                st.plotly_chart(fig, use_container_width=True)

            else:
                st.warning("⚠️ Data format not recognized for automatic visualization")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.write("Please try rephrasing your question or check your data connection.")
