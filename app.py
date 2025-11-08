import streamlit as st
import random

st.set_page_config(page_title="Daily Quote Generator", layout="centered")
st.title("📜 Quote Generator")

# List of quotes
QUOTES = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Sometimes later becomes never. Do it now.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it."
]

# Show a random quote every time
if st.button("Give me a quote"):
    st.markdown(f"> {random.choice(QUOTES)}")
