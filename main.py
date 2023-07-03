import streamlit_survey as ss
import streamlit as st
import numpy as np

survey = ss.StreamlitSurvey()

st.title("Survey for Informative Priors")
st.write("Survey draft realized with Streamlit based on the paper \"Bayesian Impact Evaluation with Informative Priors\" by Leonardo Iacovone, David McKenzie and Rachael Meager.")
st.write("""The scope of this survey is to record informative priors of different categories of actors: policymakers, experts and firms, in order to incorporate
them in Bayesian impact evaluation to learn more from expensive new programs tested on relatively small samples.""")
st.write("The research is held on a Colombian Government Program which aimed to increase export in small, medium firms.")


st.write("Specify your professional category:")
option = st.selectbox(
    'Select one of the options below:',
    ('Policymaker', 'Expert', 'Firm'))
st.write('You selected:', option)

st.write("Express your beliefs regarding the impact of the consulting programm on export for the firms offered the treatment compared to firms offered just the diagnostic phase and trade:")
export_impact = st.radio("Select one the options below:", options=["Positive", "Negative", "No changes"], horizontal=False)

if export_impact == "Positive":
    st.write("""Choose what percentage on average do you think the export is going to increase in the treated firms:""")
    positive_slider = st.slider("Select the percentage sliding on the bar below:", 0, 100, format = '%d')
    st.write("Please shortly summarize the reasons for your previous answer:")
    positive_text = st.text_input("Write your answer below:", key = 'positive_text' )
elif export_impact == "Negative":
    st.write("""Choose what percentage on average do you think the export is going to decrease in the treated firms:""")
    negative_slider = st.slider("Select the percentage sliding on the bar below:", 0, -100, format = '%d')
    st.write("Please shortly summarize the reasons for your previous answer:")
    negative_text = st.text_input("Write your answer below:", key = 'negative_text')
else: 
    st.write("Please shortly summarize the reasons for your previous answer:")
    text = st.text_input("Write your answer below:", key = 'text')

st.radio("Select one of the following options", options = ["Diversify the range of products exported", "Diversify the destinations of exportation", "All of the above"])

st.success("You completed the form successfully!")
