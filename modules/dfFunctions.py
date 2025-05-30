import pandas as pd

PDFFILE = "pdflist.csv"

def writedftofile(df, pdffile=PDFFILE):
    df.to_csv(pdffile,index=False)


def get_pdf_list():
    try:
        df = pd.read_csv(PDFFILE)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=["topic", "pages"])
    return df
