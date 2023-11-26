from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

page_number = 0
for index, row in df.iterrows():
    for page in range(row["Pages"]):
        pdf.add_page()
        page_number += 1
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        # where ln - breakline,
        # height should be the same like font size
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)

        for i in range(20, 278, 10):
            pdf.line(10, i, 200, i)

        # Set the footer
        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=14, txt=str(page_number), align="R")

pdf.output("output.pdf")
