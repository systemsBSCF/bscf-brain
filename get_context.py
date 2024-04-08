from openai import OpenAI
import streamlit as st
def get_context(JSON_data):
    # Initialize the OpenAI client with your API key
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    messages = [
        {"role": "system", "content": """
        You are tasked with interpreting JSON data to generate concise narratives in plain English.
        These narratives will be utilized as context within a chatbot application for BlueSky Capital Funding, 
        a company specializing in Merchant Cash Advance (MCA) loans. 
        Your generated context is crucial for assisting sales representatives in composing targeted emails to potential clients.
        Your response should exclusively contain the context derived from the provided JSON data. 
        Structure your output to first present the prospect's general information, followed by a narrative crafted from the JSON data. Aim for a medium-length output that is neither too brief nor overly extended.
          
         """},
        {"role": "user", "content": JSON_data}
            ]

    response = client.chat.completions.create(
                model= "gpt-4-1106-preview",
                messages=messages)
    
    return response.choices[0].message.content
