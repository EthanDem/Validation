import streamlit as st
import requests
import json
backendUrl = "https://validator-backend-icecube1513.replit.app/request"


input = st.text_input("Enter query here")

payload = {
  "message": input
}

if st.button("Submit"):

  req = requests.post(backendUrl, json=payload)
  
  response = req.content

  response_str = response.decode("utf-8")

  response_json = json.loads(response_str)

  message = response_json.get('message')

  st.write(message)

  
