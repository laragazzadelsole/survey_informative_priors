import streamlit_survey as ss
import streamlit as st

survey = ss.StreamlitSurvey()

#[theme]
#primaryColor="#F63366"
#backgroundColor="#FFFFFF"
#secondaryBackgroundColor="#F0F2F6"
#textColor="#262730"
#font="sans serif"


st.title("Survey for Informative Priors")
st.write("Survey draft realized with Python's Streamlit package based on the paper \"Bayesian Impact Evaluation with Informative Priors\" by Leonardo Iacovone, David McKenzie and Rachael Meager.")
st.write("""The scope of this survey is to record informative priors of different categories of actors: policymakers, experts and firms, in order to incorporate
them in Bayesian impact evaluation to learn more from expensive new programs tested on relatively small samples.""")
st.write("The research is held on a Colombian Government Program which aimed to increase export in small, medium and large firms.")

#fix the session state
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

#insert consent
placeholder = st.empty()
with placeholder.container():
    with st.expander("Consent", expanded=True):
        st.markdown("""
        By submitting the form below you agree to your data being used for research. 
        """)
        agree = st.checkbox("I understand and consent.")
        if agree:
            st.markdown("You have consented. Select \"Next\" to start the survey.")
if st.button('Next'):
    st.write("Specify your professional category:")
    option = st.selectbox(
        'Select one of the options below:',
        ('Policymaker', 'Expert', 'Firm'))

    st.write("Express your beliefs regarding the impact of the consulting programm on export for the firms offered the treatment compared to firms offered just the diagnostic phase and trade:")
    export_impact = st.radio("Select one of the options below:", options=["Positive", "Negative", "No changes"], horizontal=False, key = 'export_impact')


    if export_impact == "Positive":
        st.write("""Choose what percentage on average do you think the export is going to increase in the treated firms:""")
        positive_slider = st.slider("Select the percentage sliding on the bar below:", 0, 100, format = '%d', key = 'positive_slider')
        st.write("""Choose with what probability on average do you think the export is going to increase in the treated firms:""")
        prob_slider = st.slider("Select the probability sliding on the bar below:", 0, 100, key = 'prob_slider')
        st.write("Please shortly summarize the reasons for your previous answer:")
        positive_text = st.text_input("Write your answer below:", key = 'positive_text' )
        st.radio("Select one of the following options", options = ["Diversify the range of products exported", "Diversify the destinations of exportation", "All of the above"])
    if export_impact == "Negative":
        st.write("""Choose what percentage on average do you think the export is going to decrease in the treated firms:""")
        negative_slider = st.slider("Select the percentage sliding on the bar below:", 0, -100, format = '%d', key = 'negative_slider')
        st.write("""Choose with what probability on average do you think the export is going to decrease in the treated firms:""")
        prob_slider_neg = st.slider("Select the probability sliding on the bar below:", 0, 100, key = 'prob_slider_neg')
        st.write("Please shortly summarize the reasons for your previous answer:")
        negative_text = st.text_input("Write your answer below:", key = 'negative_text')
    else: 
        st.write("""Choose with what probability on average do you think the export is not going to change in the treated firms:""")
        prob_slider_neutral = st.slider("Select the probability sliding on the bar below:", 0, 100, key = 'prob_slider_neutral')
        st.write("Please shortly summarize the reasons for your previous answer:")
        text = st.text_input("Write your answer below:", key = 'text')



    st.success("You completed the form successfully!")



