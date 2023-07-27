
import streamlit as st
from constants import *
import pandas as pd
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)

def show_titles_and_subtitles():
    st.title(TITLE)
    st.write(SUBTITLE_1)
    st.write(SUBTITLE_2)
    st.write(SUBTITLE_3)

def initialize_session_state():
    if 'key' not in st.session_state:
        st.session_state['key'] = 'value'
        st.session_state['consent'] = False
        st.session_state['submit'] = False
        st.session_state['No answer'] = ''
    
    if 'data' not in st.session_state:
        st.session_state['data'] = {
            'Professional Category': [],
            'Prior on the program\'s impact': [],
            'Percentage of expected impact': [],
            'Probability of expected impact': [],
            'Effects of the impact': [],
            'Motivation': []
        }

def safe_var(key):
    if key in st.session_state:
        return st.session_state[key]
    #return st.session_state['No answer']
        
# Insert consent
def add_consent():
    st.session_state['consent'] = True

def add_submission():
    st.session_state['submit'] = True 

    data = st.session_state['data']
    data['Professional Category'].append(safe_var('professional_category'))
    data['Prior on the program\'s impact'].append(safe_var('export_impact'))
    data['Effects of the impact'].append(safe_var('export_outcome'))
    data['Probability of expected impact'].append(safe_var('probability_of_expected_impact'))
    data['Percentage of expected impact'].append(safe_var('percentage_of_expected_impact'))
    data['Motivation'].append(safe_var('motivation_text'))
            
    st.session_state['data'] = data
    df = pd.DataFrame(data)
    df.to_csv('Results.csv', index=False)