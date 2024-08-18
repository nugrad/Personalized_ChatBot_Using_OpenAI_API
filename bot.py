import streamlit as st
import openai
import json
from secretkey import secret_key

# Load personal details
with open('my.json', 'r') as file:
    personal_info = json.load(file)

# Set up OpenAI API key
openai.api_key = secret_key

def get_chatbot_response(user_input):
    prompt = (f"You are a chatbot that knows everything about Hamza Jafri. "
              f"Here are some details: {json.dumps(personal_info, indent=2)}\n"
              f"User input: {user_input}\n"
              "Chatbot response:")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message['content'].strip()

# Streamlit app
st.title("Personalized Chatbot")

# Text input for user message
user_input = st.text_input("You: ")

if st.button("Submit"):
    if user_input:
        response = get_chatbot_response(user_input)
        st.text_area("Chatbot:", value=response, height=200)
    else:
        st.warning("Please enter a message.")
