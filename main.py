import streamlit as st
from modules import dfFunctions
from modules import printPDF
import pandas as pd
import os

PDFFILE = "pdflist.csv"

st.set_page_config(layout="wide")
st.header("PDF Maker")

if not os.path.exists(PDFFILE):
    with open(PDFFILE, 'w') as newfile:
        newfile.write("topic,pages\n")

st.subheader("Topics to be included in PDF")

df = dfFunctions.get_pdf_list()
if not df.empty:
    for i, row in df.iterrows():
        st.write(f"**{row['topic']}** - {row['pages']} page(s)")

else:
    st.write("No topics added yet.")


with st.form(key="pdfForm"):
    pdfTopic = st.text_input("Enter Topic", key="pdfTopic")
    pdfPages = st.text_input("Enter the number of pages for the topic",
                                 key="pdfPages")

    button = st.form_submit_button("Add Pages")

    if button:
        newRow = pd.DataFrame([{"topic": pdfTopic, "pages": int(pdfPages)}])
        newDf = pd.concat([df, newRow], ignore_index=True)
        dfFunctions.writedftofile(newDf)

with st.form(key="pdfPrint"):
    printButton = st.form_submit_button("Generate PDF")

    if printButton:
        printPDF.generatePDF()


