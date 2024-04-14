from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.set_font('arial', 'B', 20)
pdf.text(10,10,'hi')
pdf.text(10,20,'hi')
pdf.line(10,12.5,60,12.5)
pdf.output('new.pdf')