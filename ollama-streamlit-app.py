import streamlit as st 
from llama_index.core.llms import ChatMessage 
import logging
import time
from llama_index.llms.ollama import Ollama

logging.basicConfig(level=logging.INFO)

if 'messages' not in st.session_state:
    st.session_state.messages = []

def stream_chat(model, messages):
    try:
        llm = Ollama(model=model, request_timeout=120.0)
        resp = llm.stream_chat(messages)
        response = ""
        response_placeholder = st.empty()
        for r in resp:
            response += r.delta
            response_placeholder.write(response)
        logging.info(f"Model: {model}, Messages: {messages}, Response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error During Streaming: {str(e)}")
        return e