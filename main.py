import streamlit_survey as ss
import streamlit as st
import numpy as np

survey = ss.StreamlitSurvey()

st.title("Survey for Informative Priors")

st.write("Survey draft realized with Streamlit based on the paper \"Bayesian Impact Evaluation with Informative Priors\" by Leonardo Iacovone, David McKenzie and Rachael Meager.")
st.write("""The scope of this survey is to record informative priors of different categories of actors: policymakers, experts and firms, in order to incorporate
them in Bayesian impact evaluation to learn more from expensive new programs tested on relatively small samples.
 """)

st.write("The research is held on a Colombian Government Program which aimed to increase export in small, medium firms.")

st.write("Specify your professional category:")
option = st.selectbox(
     'Select one of the options below:',
     ('Policymaker', 'Expert', 'Firm'))

st.write('You selected:', option)
array = np.arange(0, 101)

st.write("Express your beliefs regarding the impact of the consulting programm on export for the firms offered the treatment:")
st.radio("Select one the options below:", options=["Positive", "Negative", "No changes"], horizontal=False)

st.write("""Express your beliefs for the likely impact of the program for the firms that are
offered the full intervention, compared to firms offered just the diagnostic phase and trade:""")
survey.select_slider("Select one of the following options:", options= array )

st.radio("Select one of the following options", options = ["Diversify the range of products exported", "Diversify the destinations towards the products are exported", "All of the above"])

st.title("Survey for Informative Priors")
