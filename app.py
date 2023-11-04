import streamlit as st
from pathlib import Path

# Design
st.set_page_config(page_title="Edgard Huanca Quispe",
                   page_icon="bar_chart:",
                   layout="wide")

# Hide hamburger menu
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Print .md file
result=st.experimental_get_query_params() #Get params of url
if len(result.keys())!=0:
    filename=result['file'][0]
    md=Path(filename).read_text()
else:
    md=Path('summary.md').read_text()

st.markdown(md, unsafe_allow_html=True) #Output
