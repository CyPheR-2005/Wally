import streamlit as st
import datetime
import ollama
import pandas as pd
import json
import os

# Initialize Ollama client
client = ollama.Client()

# File paths
CHAT_HISTORY_FILE = "chat_history.json"
EXCEL_FILE = "shopping_data.xlsx"

# Set page configuration
st.set_page_config(page_title="RetailX Assistant", page_icon="🛒", layout="centered")
st.title("🛒 RetailX Shopping Assistant")
st.subheader("Your personalized shopping assistant powered by Ollama")

# Load or initialize shopping data from Excel
def load_shopping_data():
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
        return df.set_index('item').to_dict(orient='index')
    else:
        # default data if file not found
        data = {
            "toothpaste": {"last_bought": "2024-06-01", "days_interval": 30},
            "rice": {"last_bought": "2024-06-20", "days_interval": 60},
            "milk": {"last_bought": "2025-07-11", "days_interval": 2},
            "shampoo": {"last_bought": "2025-06-15", "days_interval": 45}
        }
        pd.DataFrame([
            {"item": k, **v} for k, v in data.items()
        ]).to_excel(EXCEL_FILE, index=False)
        return data

shopping_data = load_shopping_data()

# Load chat history from file
if os.path.exists(CHAT_HISTORY_FILE):
    with open(CHAT_HISTORY_FILE, 'r') as f:
        st.session_state['history'] = json.load(f)
else:
    st.session_state['history'] = []

# Function to check if user needs to restock
def get_restock_reminders():
    today = datetime.date.today()
    reminders = []
    for item, details in shopping_data.items():
        last = datetime.datetime.strptime(str(details['last_bought']), "%Y-%m-%d").date()
        delta_days = (today - last).days
        if delta_days >= int(details['days_interval']):
            reminders.append(f"🛒 You may need to buy **{item}**. Last bought {delta_days} days ago.")
    return reminders

# Display restock reminders
with st.expander("📌 View Restock Suggestions"):
    reminders = get_restock_reminders()
    if reminders:
        for r in reminders:
            st.markdown(r)
    else:
        st.success("✅ No items need restocking right now!")

# User query input
user_input = st.chat_input("Ask RetailX something (e.g., 'What should I buy this week?')")

# Add shopping context system message (inject only once at start)
if len(st.session_state['history']) == 0:
    system_message = {
        "role": "system",
        "content": "You are RetailX, a smart shopping assistant. Only respond with answers related to shopping, product reminders, grocery planning, or personal purchase advice. Do not go off-topic."
    }
    st.session_state['history'].append(system_message)

# Process input
if user_input:
    st.session_state['history'].append({"role": "user", "content": user_input})

    response = client.chat(
        model="llama2",
        messages=st.session_state['history']
    )

    reply = response["message"]["content"]
    st.session_state['history'].append({"role": "assistant", "content": reply})

    # Save chat history after each response
    with open(CHAT_HISTORY_FILE, 'w') as f:
        json.dump(st.session_state['history'], f, indent=2)

# Display chat history
for message in st.session_state['history']:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(message["content"])
