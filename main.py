from fpdf import FPDF
Header = "ASSIGNMENT"
Course = "CSE115"
# Faculty = input("Enter your faculty name: ").strip().title()
# Name = input("Enter your name: ").strip().title()
# Id = input("Enter your id: ").strip().title()
# Sec = input("Enter your sec: ").strip().title()
# Date = input("Enter your date: ").strip().title()
Name = "Safwat Sadiq"
Id = "2513454642"
Sec = "8"
Date = "2025-10-01"

def draw_border(FPDF, x):
    """ Draws a border around the page with a specified margin."""
    pdf.set_line_width(0.3)
    pdf.rect(x=x, y=x, w=pdf.w - 2 * x, h=pdf.h - 2 * x)
    
# Page Setup
pdf = FPDF(format='A4') 
pdf.add_page()
draw_border(pdf, 6)
draw_border(pdf, 6.7)

# Adding New Fonts
pdf.add_font("Bay_Tavern", "", "Fonts\\Bay_Tavern\\Bay Tavern S Regular.ttf", uni=True)
pdf.add_font("Nimbus_Rom_No_9L", "B", "Fonts\\Nimbus_Rom_No_9L\\NimbusRomNo9L-Med.ttf", uni=True)
pdf.add_font("Nimbus_Rom_No_9L", "", "Fonts\\Nimbus_Rom_No_9L\\NimbusRomNo9L-Reg.ttf", uni=True)

# Working With The NSU Logo
page_center = pdf.w / 2
image_width = 50
pdf.image("Data\\Logo2.png", x=page_center - (image_width / 2), y=20, w=image_width)

# Header Part
pdf.set_font("Bay_Tavern", size=50)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(0, 80)
pdf.cell(pdf.w, 50, txt=Header, ln=True, align='C')

# Course Part
pdf.set_font("Arial", style="B",  size=20)
pdf.set_text_color(255, 255, 255)
# pdf.set_text_color(0, 0, 0)
# pdf.rect(x=60, y=10, w=50, h=30, round_corners=True, corner_radius=5, style="DF")
pdf.set_xy(pdf.w/2 - pdf.get_string_width(Course) / 2, 115)
pdf.cell(pdf.get_string_width(Course) + 2, 10, txt=Course, ln=True, align='L', fill=True)

# Submitted To Part
pdf.set_font("Nimbus_Rom_No_9L", style="B", size=20)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, 140)
pdf.cell(0, 20, txt="Submitted To: ", ln=False, align='L')
pdf.set_font("Nimbus_Rom_No_9L", size=20)
pdf.set_xy(65, 140)
pdf.cell(0, 20, txt=Name, ln=True, align='L')

# Submitted By Part
pdf.set_font("Nimbus_Rom_No_9L", style="B", size=20)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, 180)
pdf.cell(0, 20, txt="Submitted By: ", ln=False, align='L')
pdf.set_font("Nimbus_Rom_No_9L", size=20)
pdf.set_xy(65, 180)
pdf.cell(0, 20, txt=Name, ln=True, align='L')

# ID Part
pdf.set_font("Nimbus_Rom_No_9L", style="B", size=20)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, 190)
pdf.cell(0, 20, txt="ID: ", ln=False, align='L')
pdf.set_font("Nimbus_Rom_No_9L", size=20)
pdf.set_xy(32, 190)
pdf.cell(0, 20, txt=Id, ln=True, align='L')

# Sec Part
pdf.set_font("Nimbus_Rom_No_9L", style="B", size=20)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, 200)
pdf.cell(0, 20, txt="Sec: ", ln=False, align='L')
pdf.set_font("Nimbus_Rom_No_9L", size=20)
pdf.set_xy(34, 200)
pdf.cell(0, 20, txt=Sec, ln=True, align='L')

# Date Part
pdf.set_font("Nimbus_Rom_No_9L", style="B", size=20)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, 210)
pdf.cell(0, 20, txt="Date: ", ln=False, align='L')
pdf.set_font("Nimbus_Rom_No_9L", size=20)
pdf.set_xy(38, 210)
pdf.cell(0, 20, txt=Date, ln=True, align='L')


pdf.output("Output\\output.pdf")