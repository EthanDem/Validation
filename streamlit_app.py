import streamlit as st
import requests

backendUrl = "https://validator-backend-icecube1513.replit.app/request"


input = st.text_input("Enter query here")

payload = {
  "message": input
}

if st.button("Submit")

req = requests.post(backendUrl, json=payload)

st.write(req.content)
