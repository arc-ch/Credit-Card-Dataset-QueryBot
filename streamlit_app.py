import streamlit as st
from pandasai import SmartDataframe
from pandasai.responses.response_parser import ResponseParser
from langchain_community.llms import GooglePalm
from data import load_data

class CustomResponseParser(ResponseParser):
    def __init__(self, context) -> None:
        super().__init__(context)

    def format_dataframe(self, result):
        st.dataframe(result["value"])
        return

    def format_plot(self, result):
        st.image(result["value"])
        return

    def format_other(self, result):
        st.write(result["value"])
        return

st.write("# Chat with Credit Card Fraud Dataset 🦙")

df = load_data("./data")

with st.expander("🔎 Dataframe Preview"):
    st.write(df.tail(3))

query = st.text_area("🗣️ Chat with Dataframe")
container = st.container()

if query:
    # Initialize the Google PaLM API client
    api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    llm = GooglePalm(google_api_key=api_key, temperature=0.2)
    
    query_engine = SmartDataframe(
        df,
        config={
            "llm": llm,
            "response_parser": CustomResponseParser,
        }
    )

    answer = query_engine.chat(query)
    st.write(answer)  # Display the final answer
