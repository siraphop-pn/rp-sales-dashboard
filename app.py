import streamlit as st
import streamlit.components.v1 as components
import json
import os

st.set_page_config(layout="wide", page_title="RP Sales Dashboard")

# Load pre-processed data
with open("data.json", "r", encoding="utf-8") as f:
    raw_data = f.read()

# Load UI Template
with open("template.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Inject data into the template
start_marker = "const rawData = ["
end_marker = "];"
start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker, start_idx) + 2

if start_idx != -1 and end_idx != -1:
    injected_html = html_content[:start_idx] + "const rawData = " + raw_data + ";" + html_content[end_idx:]
    # Fix for streamlit component display
    components.html(injected_html, height=1000, scrolling=True)
else:
    st.error("Could not find data injection point in template.html")

