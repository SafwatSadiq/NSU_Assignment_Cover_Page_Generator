from fpdf import FPDF
from fpdf.enums import XPos, YPos
import streamlit as st
import io

Header = "ASSIGNMENT"

# streamlit input box
col1, col2, col3 = st.columns(3)
with col1:
    Course = st.text_input('Course').strip().title()
with col2:
    Faculty = st.text_input('Faculty').strip().title()
with col3:
    Sec = st.text_input('Section').strip().title()
    
Name = st.text_input('Name').strip().title()

col4, col5 = st.columns(2)
with col4:
    Id = st.text_input('ID').strip().title()
with col5:
    Date = st.text_input('Date').strip().title()

def draw_border(pdf, x):
    """ Draws a border around the page with a specified margin."""
    pdf.set_draw_color(34, 126, 172)
    pdf.set_line_width(0.3)
    pdf.rect(x=x, y=x, w=pdf.w - 2 * x, h=pdf.h - 2 * x)
    
def add_text(pdf, x_1, y_1, x_2, y_2, text_1, text_2, font_size=20):
    pdf.set_font("Nimbus_Rom_No_9L", style="B", size=font_size)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(x_1, y_1)
    pdf.cell(0, 20, text=text_1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='L')
    pdf.set_font("Nimbus_Rom_No_9L", size=20)
    pdf.set_xy(x_2, y_2)
    pdf.cell(0, 20, text=text_2, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
    
    
# Page Setup
def generate_pdf():
    pdf = FPDF(format='A4') 
    pdf.add_page()
    draw_border(pdf, 6)
    draw_border(pdf, 6.7)

    # Adding New Fonts
    pdf.add_font("Bay_Tavern", "", "Fonts/Bay_Tavern/Bay Tavern S Regular.ttf")
    pdf.add_font("Nimbus_Rom_No_9L", "B", "Fonts/Nimbus_Rom_No_9L/NimbusRomNo9L-Med.ttf")
    pdf.add_font("Nimbus_Rom_No_9L", "", "Fonts/Nimbus_Rom_No_9L/NimbusRomNo9L-Reg.ttf")

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
    pdf.set_draw_color(0, 0, 0)
    pdf.rect(x=pdf.w/2 - pdf.get_string_width(Course) / 2, y=114.5,
            w=pdf.get_string_width(Course) + 2.2, h=10,
            round_corners=True, corner_radius=10, style="DF")
    pdf.set_xy(pdf.w/2 - pdf.get_string_width(Course) / 2, 115)
    pdf.cell(pdf.get_string_width(Course) + 2, 10, text=Course, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')

    # Submitted To Part
    add_text(pdf, 20, 140, 65, 140, "Submitted To: ", Faculty)
    # Submitted By Part
    add_text(pdf, 20, 180, 65, 180, "Submitted By: ", Name)
    # ID Part
    add_text(pdf, 20, 190, 32, 190, "ID: ", Id)
    # Sec Part
    add_text(pdf, 20, 200, 34, 200, "Sec: ", Sec)
    # Date Part
    add_text(pdf, 20, 210, 38, 210, "Date: ", Date)


    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output

submitted = st.button("Submit")
if submitted:
    if not Course or not Faculty or not Sec or not Name or not Id or not Date:
        st.error("Please fill in all fields.")
    else:
        st.download_button(
            label="Download PDF",
            data=generate_pdf(),
            file_name="NSU_Assignment_Cover_Page.pdf",
            mime="application/pdf"
        )