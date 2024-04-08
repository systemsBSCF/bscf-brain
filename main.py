import json
from openai import OpenAI
import streamlit as st
from fetch_data import fetch_data_from_backend
from get_context import get_context

prospect_id = st.query_params["prospect_id"]

data = fetch_data_from_backend(prospect_id)
# convert the varibable `data` to string from JSON
data1 = json.dumps(data)
data2 = get_context(data1)

system_message = f"you are a helpful bot that help Users with their queries given the context of a prospact. the context opr the prospact is: {data2}"

st.title("ChatGPT-like clone")
# Initialize the OpenAI client with your API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Check if the necessary keys are in the session state, otherwise initialize them
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_message}]

# Function to display chat messages
def display_messages():
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Retrieve prospect ID and sales rep ID from the URL parameters

# Display prospect ID and sales rep ID
st.write(f"Prospect ID: {prospect_id}")
# st.write(f"Sales Rep ID: {sales_rep_id}")

# Display chat history
display_messages()

# Chat input for user messages
prompt = st.chat_input("What is up?")

# Process the user input
if prompt:
    # Append the user's message to the chat history
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # Prepare the chat history for the OpenAI API call
    api_messages = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state["messages"]
    ]

    # Call the OpenAI API to get a response and stream it back
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=api_messages,
            stream=True
        )
        response = st.write_stream(stream)

    # Update the session state with the assistant's response for history
    st.session_state["messages"].append({"role": "assistant", "content": response})
