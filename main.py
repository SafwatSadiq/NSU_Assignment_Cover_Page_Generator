from fpdf import FPDF
from fpdf.enums import XPos, YPos

Header = "ASSIGNMENT"
Course = input("Enter your course name: ").strip().title()
Faculty = input("Enter your faculty name: ").strip().title()
Name = input("Enter your name: ").strip().title()
Id = input("Enter your id: ").strip().title()
Sec = input("Enter your sec: ").strip().title()
Date = input("Enter your date: ").strip().title()

def draw_border(FPDF, x):
    """ Draws a border around the page with a specified margin."""
    pdf.set_draw_color(34, 126, 172)
    pdf.set_line_width(0.3)
    pdf.rect(x=x, y=x, w=pdf.w - 2 * x, h=pdf.h - 2 * x)
    
# Page Setup
pdf = FPDF(format='A4') 
pdf.add_page()
draw_border(pdf, 6)
draw_border(pdf, 6.7)

# Adding New Fonts
pdf.add_font("Bay_Tavern", "", "Fonts\\Bay_Tavern\\Bay Tavern S Regular.ttf")
pdf.add_font("Nimbus_Rom_No_9L", "B", "Fonts\\Nimbus_Rom_No_9L\\NimbusRomNo9L-Med.ttf")
pdf.add_font("Nimbus_Rom_No_9L", "", "Fonts\\Nimbus_Rom_No_9L\\NimbusRomNo9L-Reg.ttf")

# Working With The NSU Logo
page_center = pdf.w / 2
image_width = 50
pdf.image("Data\\Logo2.png", x=page_center - (image_width / 2), y=20, w=image_width)

# Header Part
pdf.set_font("Bay_Tavern", size=50)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(0, 80)
pdf.cell(pdf.w + 2, 50, text=Header, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

# Course Part
pdf.set_font("helvetica", style="B",  size=20)
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(34, 126, 172)
pdf.rect(x=pdf.w/2 - pdf.get_string_width(Course) / 2, y=114.5,
         w=pdf.get_string_width(Course) + 2.2, h=10,
         round_corners=True, corner_radius=10, style="DF")
pdf.set_xy(pdf.w/2 - pdf.get_string_width(Course) / 2, 115)
pdf.cell(pdf.get_string_width(Course) + 2, 10, text=Course, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')

# Submitted To Part
pdf.set_font("Nimbus_Rom_No_9L", style="B", size=20)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, 140)
pdf.cell(0, 20, text="Submitted To: ", new_x=XPos.RIGHT, new_y=YPos.TOP, align='L')
pdf.set_font("Nimbus_Rom_No_9L", size=20)
pdf.set_xy(65, 140)
pdf.cell(0, 20, text=Faculty, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')

# Submitted By Part
pdf.set_font("Nimbus_Rom_No_9L", style="B", size=20)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, 180)
pdf.cell(0, 20, text="Submitted By: ", new_x=XPos.RIGHT, new_y=YPos.TOP, align='L')
pdf.set_font("Nimbus_Rom_No_9L", size=20)
pdf.set_xy(65, 180)
pdf.cell(0, 20, text=Name, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')

# ID Part
pdf.set_font("Nimbus_Rom_No_9L", style="B", size=20)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, 190)
pdf.cell(0, 20, text="ID: ", new_x=XPos.RIGHT, new_y=YPos.TOP, align='L')
pdf.set_font("Nimbus_Rom_No_9L", size=20)
pdf.set_xy(32, 190)
pdf.cell(0, 20, text=Id, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')

# Sec Part
pdf.set_font("Nimbus_Rom_No_9L", style="B", size=20)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, 200)
pdf.cell(0, 20, text="Sec: ", new_x=XPos.RIGHT, new_y=YPos.TOP, align='L')
pdf.set_font("Nimbus_Rom_No_9L", size=20)
pdf.set_xy(34, 200)
pdf.cell(0, 20, text=Sec, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')

# Date Part
pdf.set_font("Nimbus_Rom_No_9L", style="B", size=20)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(20, 210)
pdf.cell(0, 20, text="Date: ", new_x=XPos.RIGHT, new_y=YPos.TOP, align='L')
pdf.set_font("Nimbus_Rom_No_9L", size=20)
pdf.set_xy(38, 210)
pdf.cell(0, 20, text=Date, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')


pdf.output("Output\\output.pdf")