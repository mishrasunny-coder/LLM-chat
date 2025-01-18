import streamlit as st 
from llama_index.core.llms import ChatMessage 
import logging
import time
from llama_index.llms.ollama import Ollama

logging.basicConfig(level=logging.INFO)