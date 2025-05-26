import os

from fpdf import FPDF
import pandas as pd

PDFFILE = "pdflist.csv"

def generatePDF(pdfFile = PDFFILE):
    pdf = FPDF(orientation="P", unit="mm", format="a4")
    pdf.set_auto_page_break(auto=False, margin=0)

    df = pd.read_csv(pdfFile)

    for index, row in df.iterrows():
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["topic"], align="L", ln=1)

        for y in range(21, 297, 12):
            pdf.line(x1=10, y1=y, x2=200, y2=y)

        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["topic"], align="R", ln=1)

        for i in range(row["pages"] - 1):
            pdf.add_page()
            pdf.set_font(family="Times", style="I", size=10)
            pdf.set_text_color(180, 180, 180)

            for y in range(21, 297, 12):
                pdf.line(x1=10, y1=y, x2=200, y2=y)

            pdf.ln(277)
            pdf.cell(w=0, h=12, txt=row["topic"], align="R", ln=1)

    pdf.output("output.pdf")
    os.startfile("output.pdf")
