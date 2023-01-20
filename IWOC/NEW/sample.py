from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=False)
pdf.set_line_width(6)
pdf.set_draw_color(r=0, g=0, b=0)
pdf.line(x1=5, y1=4, x2=205, y2=4)         #1st horizontal line
pdf.line(x1=5, y1=292, x2=205, y2=292)     #2nd horizontal line 
pdf.line(5,6,5,290)                         # 1st vertical line
pdf.line(205,6,205,290)                     # 2nd vertical line    

pdf.set_font('Times','B',8.5)
pdf.cell(45)
pdf.cell(10,10,txt = 'PSAMPLE DSJ DSIN DSIDSN DSDNS DBSDSDJS')
pdf.ln(1)
pdf.cell(66)
pdf.cell(10,14,txt = 'BANK SIMPANAN NASIONAL (BSN)')

pdf.output('sample.pdf')