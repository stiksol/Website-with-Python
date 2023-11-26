from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

# get list of file paths
filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    # get filepath and invoice number like '10001'
    filename = Path(filepath).stem
    # invoice_number = filename[0] and date = filename[1]
    invoice_number, date = filename.split("-")

    # create a PDF File with invoice number as a title
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr {invoice_number}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=55, h=8, txt=columns[1], border=1)
    pdf.cell(w=35, h=8, txt=columns[2], border=1)
    pdf.cell(w=35, h=8, txt=columns[3], border=1)
    pdf.cell(w=35, h=8, txt=columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=55, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["total_price"]), border=1, ln=1)

    pdf.output(f"PDFs/{filename}.pdf")

