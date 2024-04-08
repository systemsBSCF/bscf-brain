from openai import OpenAI
import streamlit as st
def get_context(JSON_data):
    # Initialize the OpenAI client with your API key
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    messages = [
        {"role": "system", "content": """
         You are a function designed to process JSON data as input and produce a narrative in plain English based on that data. 
         This narrative serves as context within a chatbot application developed for BlueSky Capital Funding, 
         a Merchant Cash Advance (MCA) loan company. The context you generate will be integrated into the chatbot's system messages. 
         The primary goal of this chatbot application is to assist sales representatives in crafting effective emails to prospective clients.
          
         """},
        {"role": "user", "content": JSON_data}
            ]

    response = client.chat.completions.create(
                model= "gpt-4-1106-preview",
                messages=messages)
    
    return response.choices[0].message.content
