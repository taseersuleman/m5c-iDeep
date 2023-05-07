import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

selected2 = option_menu(None, ["Home", "Predictor", "Dataset", "Citations"],
                        icons=['house', 'search', 'list-task', 'book'],
                        menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

if selected2 == "Home":
    st.header("m5C-iDeep")
    #st.subheader("The DHU-Pred is a web-server for the prediction of Dihydrouridine in transfer RNA (tRNA) "
     #            "modifications.")
    st.write("5-Methylcytosine (m5c) is a chemical modification that happens after transcription, which is the process of turning a DNA blueprint into an RNA molecule. It is done by adding a methyl group to the cytosine base. This modification is one of the most common post transcriptional modifications (PTM) that used to occur in RNA. The conventional laboratory methods do not provide quick reliable identification of m5c sites. However, the availability of sequence data has made it feasible to develop computationally intelligent models that optimize the identification process for accuracy and robustness. The current study focused on the development of in-silico methods based on deep learning models. The encoded data was subsequently passed on to deep learning models such as long short-term memory (LSTM), gated recurrent unit (GRU), and bi-directional LSTM (Bi-LSTM). After that, the models3 were subjected to a rigorous evaluation process that included both independent set testing and 10-fold cross validation. The results revealed that LSTM-based model, m5c-iDeep, outperformed revealing 99.9% accuracy while comparing with existing m5c predictors. M5c-iDeep was also deployed on a web-based server to make it available to the researchers."
             )
    #image = Image.open('pseudo.PNG')
    #st.image(image, width=400)

elif selected2 == "Predictor":
    #st.subheader("Predictor Page")
    import predictor

    exec(open('predictor.py').read())


elif selected2 == "Dataset":
    #st.subheader("Data Set")
    st.info("iRNA 5mc Dataset")
    with open("iRNA-5mc.rar", "rb") as file:
        btn = st.download_button(
            label="Download file",
            data=file,
            file_name="iRNA-5mc.rar",
            mime=""
        )
    st.info("m5c-Pred-XS")
    with open("m5c-pred-XS.rar", "rb") as file:
        btn = st.download_button(
            label="Download file",
            data=file,
            file_name="m5c-pred-XS.rar",
            mime=""
        )
