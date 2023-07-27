import streamlit_survey as ss
import streamlit as st
import pandas as pd
from utils import *
from components import *
#from shillelagh.backends.apsw.db import connect

#survey = ss.StreamlitSurvey()




#connection = connect(":memory:",
#                     adapter_kwargs = {
 #                           "gsheetsapi": { 
  #                          "service_account_info":  st.secrets["gcp_service_account"] 
  #                                  }
   #                                     }
    #                    )


# streamlit_app.py


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


# Initialize session state
initialize_session_state()

# Show introductory texts
show_titles_and_subtitles()

df = pd.DataFrame()

consent_form()

if st.session_state['consent']:
    # Professional Category Checkbox
    st.selectbox('Specify your professional category:', ('Policymaker', 'Expert', 'Firm'), key="professional_category")
    
    st.radio(EXPORT_IMPACT_DESCRIPTION, options=["Positive", "Negative", "No changes"], horizontal=False, key = 'export_impact')

    percentage_of_expected_impact(st.session_state.export_impact)
    probability_of_expected_impact(st.session_state.export_impact)
    motivation()

    if st.session_state.export_impact == "Positive":
        st.radio("Select one of the following options", options = ["Diversify the range of products exported", "Diversify the destinations of exportation", "All of the above"], key = 'export_outcome')

    submit = st.button("Submit", on_click = add_submission)

    if st.session_state['submit']:
        st.success("You completed the form successfully!")

