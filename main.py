import streamlit as st
from modules import dfFunctions
from modules import printPDF
import pandas as pd
import os
import time
import uuid


PDFFILE = "pdflist.csv"

st.set_page_config(layout="wide")
st.header("Notebook Maker")

if not os.path.exists(PDFFILE):
    with open(PDFFILE, 'w') as newfile:
        newfile.write("topic,pages,uuid\n")

st.subheader("Topics to be included in PDF")

df = dfFunctions.get_pdf_list()

indexToDrop = None

if not df.empty:
    for i, row in df.iterrows():
        label = f"**{row['topic']}** - {row['pages']} page(s)"
        checkbox = st.checkbox(label, key=f"delete_{row['uuid']}")
        if checkbox:
            indexToDrop = row['uuid']
            break

    if indexToDrop is not None:
        df = df[df["uuid"] != indexToDrop]
        dfFunctions.writedftofile(df)
        st.success("Item Removed")
        time.sleep(1)
        st.rerun()

else:
    st.write("No topics added yet.")


with st.form(key="pdfForm"):
    pdfTopic = st.text_input("Enter Topic", key="pdfTopic",)
    pdfPages = st.text_input("Enter the number of pages for the topic",
                                 key="pdfPages")

    button = st.form_submit_button("Add Pages")

    if button:
        try:
            newRow = pd.DataFrame([{"topic": pdfTopic, "pages": int(pdfPages), "uuid":str(uuid.uuid4())}])
            newDf = pd.concat([df, newRow], ignore_index=True)
            dfFunctions.writedftofile(newDf)
            st.success("Topic and Pages added successfully")
            time.sleep(1)
            st.rerun()

        except ValueError:
            st.warning("Please enter a numerical digit for the number of pages")

with st.form(key="pdfPrint"):
    printButton = st.form_submit_button("Generate PDF")

    if printButton:
        printPDF.generatePDF()
        os.remove(PDFFILE)
        st.rerun()


