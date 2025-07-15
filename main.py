from fpdf import FPDF

def draw_border(FPDF, x):
    pdf.set_line_width(0.3)
    pdf.rect(x=x, y=x, w=pdf.w - 2 * x, h=pdf.h - 2 * x)
    

pdf = FPDF(format='A4')
pdf.add_page()

draw_border(pdf, 6)
draw_border(pdf, 6.7)

page_center = pdf.w / 2
image_width = 60
pdf.image("Data\\Logo.png", x=page_center - (image_width / 2), y=20, w=image_width)

pdf.set_font("Bay Tavern", size=24)
pdf.set_text_color(0, 0, 0)
Header = "ASSIGNMENT"
pdf.cell(0, 10, txt=Header, ln=True, align='C')


pdf.output("Output\\output.pdf")