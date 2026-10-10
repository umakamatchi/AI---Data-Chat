import json

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

from mydb import execute_query, get_schema

load_dotenv()


class QueryResult(BaseModel):
    sql: str
    question: str


@st.cache_resource
def get_client():
    return genai.Client()


@st.cache_data(show_spinner=False)
def load_schema():
    return get_schema("superstore")


def generate_sql(client, question, schema):
    prompt = f"""Write a read-only SQL query based on the question below.
Question: {question}
Use this superstore table schema:
{schema}
Return only a SELECT query. Do not modify data or database structure."""
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=QueryResult,
        ),
    )
    payload = json.loads(response.text)
    sql = payload["sql"].strip()
    if not sql.lower().startswith(("select", "with")):
        raise ValueError("Generated SQL was not a read-only SELECT query.")
    return sql


st.set_page_config(page_title="Superstore Data Chat", page_icon="📊")
st.title("Superstore Data Chat")
st.caption("Ask questions about your superstore data in plain English.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sql"):
            st.code(message["sql"], language="sql")
        if message.get("data") is not None:
            st.dataframe(message["data"], use_container_width=True)

question = st.chat_input("Ask about your superstore data")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Generating and running your query..."):
                schema = load_schema()
                sql = generate_sql(get_client(), question, schema)
                result = execute_query(sql)
            st.code(sql, language="sql")
            st.dataframe(result, use_container_width=True)
            st.session_state.messages.append(
                {"role": "assistant", "content": "Here are the results:", "sql": sql, "data": result}
            )
        except Exception as exc:
            st.error(f"Could not answer that question: {exc}")
            st.session_state.messages.append(
                {"role": "assistant", "content": f"Could not answer that question: {exc}"}
            )
