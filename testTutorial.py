from fpdf import FPDF

name = "Roilhi"
pdf = FPDF()

pdf.add_page()
pdf.set_font('Arial', 'B',16)
pdf.cell(40,10, 'Hello World!')
pdf.set_font('Arial','',14)
pdf.cell(40,20, f'Hello, my name is {name}!')
pdf.output('tuto.pdf', 'F')