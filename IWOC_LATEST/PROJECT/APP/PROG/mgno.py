from fpdf import FPDF

def MGNO(request,files1):
    path11 = r'E:\IWOC\SOURCE\\'+ files1
    with open(path11) as file:
        lines = file.readlines()
        total_lines = len(lines)
        print(total_lines)
    with open(path11) as file:
        Seq = []
        Date1 = []
        Br = []
        Date2 = []
        Name1 = []
        Account_no = []
        Tp = []
        Facility = []
        Name2 = []
        Date3 = []
        AMTDisburse = []
        TTLDisburse = []
        MonthlyAMT = []
        TYPEDisburse = []
        Date4 = []
        Name3 = []
        Add1 = []
        Add2 = []
        Add3 = []
        Add4 = []
        Add5 = []
        TypeFACe = []
        TypeFACm = []
        Day = []
        Month = []
        Year = []
        TP2 = []
        line = file.readlines()
        for i in line:
            if i.startswith('1'):
                i = i.strip('\n')
                i = i.split('|')
                Seq.append(i[0])
                Date1.append(i[1])
                Br.append(i[2])
                Date2.append(i[3])
                Name1.append(i[4])
                Account_no.append(i[5])
                Tp.append(i[6])
                Facility.append(i[7])
                Name2.append(i[8])
                Date3.append(i[9])
                AMTDisburse.append(i[10])
                TTLDisburse.append(i[11])
                MonthlyAMT.append(i[12])
                TYPEDisburse.append(i[13])
                Date4.append(i[14])
                Name3.append(i[15])
                Add1.append(i[16])
                Add2.append(i[17])
                Add3.append(i[18])
                Add4.append(i[19])
                Add5.append(i[20])
                TypeFACe.append(i[21])
                TypeFACm.append(i[22])
                Day.append(i[23])
                Month.append(i[24])
                Year.append(i[25])
                TP2.append(i[26])
        # postcode0 = []
        # with open(path11) as file:
            # for i in range(0,total_lines-2):
                # print(i,'iii')
                # if i[4].startswith(('0','1','2','3','4','5','6','7','8','9')) and ',' not in line[4]  and len(line[4].strip()) > 4 and '/' not in line[4]:
                    # pst = line[4].split()
                    # postcode0.append(pst[0]) 
                # elif line[5].startswith(('0','1','2','3','4','5','6','7','8','9')) and ',' not in line[5] and len(line[5].strip()) > 4 and '/' not in line[5]:
                #     pst = line[5].split()
                #     postcode0.append(pst[0]) 
                # elif line[6].startswith(('0','1','2','3','4','5','6','7','8','9')) and ',' not in line[6] and len(line[6].strip()) > 4 and ',' not in line[6]:
                #     pst = line[6].split()
                #     postcode0.append(pst[0]) 
                # else:
                #     postcode0.append('00000') 
        # print(postcode0,'po')
        count = 1
        pdf = FPDF()
        # print(Add4)
        for i in range(0,total_lines-2):
            pdf.add_page()
            pdf.set_auto_page_break(auto=False)
            pdf.set_line_width(6)
            pdf.set_draw_color(r=0, g=0, b=0)
            pdf.line(4, 5, 200, 5)       #1st horizontal line
            pdf.line(5, 290,200,290)     #2nd horizontal line 
            pdf.line(4,6,4,290)          # 1st vertical line
            pdf.line(200,6,200,290)      # 2nd vertical line    

            pdf.image(r'E:\IWOC\APP SCRIPT\MGNO\CYCLE\mno\DATA\heading.png',15,9,80)
            pdf.image(r'E:\IWOC\APP SCRIPT\MGNO\CYCLE\mno\DATA\sidehaeding.png',142,9,50)
            pdf.ln(1)
            pdf.set_font('Arial','',7)
            pdf.cell(7)
            pdf.cell(10,48,txt = 'Date : ')
            pdf.cell(-3)
            # pdf.cell(10,48,txt = '20/12/2022')
            pdf.cell(10,48,txt = Date1[i])
            pdf.ln(1)
            pdf.set_font('Arial','',7)
            pdf.cell(7)
            pdf.cell(10,60,txt = Name2[i])
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,65,txt = Add1[i])
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,70,txt = Add2[i])
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,75,txt = Add3[i])
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,80,txt = Add4[i])
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,85,txt = Add5[i])

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,110,txt = 'Dear Sir/Madam')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,116,txt = 'NOTIFICATION OF DISBURSEMENT')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,122,txt = 'ACCOUNT NUMBER')
            pdf.cell(36)
            pdf.cell(10,122,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,122,txt = Account_no[i])

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,128,txt = 'FINANCING FACILITY')
            pdf.cell(36)
            pdf.cell(10,128,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,128,txt = Facility[i])

            pdf.set_line_width(0.05)
            pdf.line(18,89,190,89)

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,142,txt = 'We refer to the above and wish to advise that your')
            pdf.cell(46)
            # print(TypeFACe[i],len(TypeFACe[i]),'ccpp')
            if len(TypeFACe[i]) == 14:
                # print('-----------14')
                pdf.cell(10,142,txt = TypeFACe[i])
                pdf.cell(9)
                pdf.cell(10,142,txt = '("Financing Facility") account has been debited with the following details:-')

            if len(TypeFACe[i]) == 15:
                # print('-----------15')
                pdf.cell(10,142,txt = TypeFACe[i])
                pdf.cell(10)
                pdf.cell(10,142,txt = '("Financing Facility") account has been debited with the following details:-')

            if len(TypeFACe[i]) == 16:
                # print('-----------16')
                pdf.cell(10,142,txt = TypeFACe[i])
                pdf.cell(11)
                pdf.cell(10,142,txt = '("Financing Facility") account has been debited with the following details:-')

            if len(TypeFACe[i].strip()) == 17:
                # print('-----------17')
                pdf.cell(10,142,txt = TypeFACe[i])
                pdf.cell(12)
                pdf.cell(10,142,txt = '("Financing Facility") account has been debited with the following details:-')

            if len(TypeFACe[i]) == 18:
                # print('-----------18')
                pdf.cell(10,142,txt = TypeFACe[i])
                pdf.cell(13)
                pdf.cell(10,142,txt = '("Financing Facility") account has been debited with the following details:-')

            if len(TypeFACe[i]) == 19:
                # print('-----------19')
                pdf.cell(10,142,txt = TypeFACe[i])
                pdf.cell(14)
                pdf.cell(10,142,txt = '("Financing Facility") account has been debited with the following details:-')

            if len(TypeFACe[i]) == 20:
                # print('-----------20')
                pdf.cell(10,142,txt = TypeFACe[i])
                pdf.cell(20)
                pdf.cell(10,142,txt = '("Financing Facility") account has been debited with the following details:-')

            if len(TypeFACe[i]) == 21:
                # print('-----------21')
                pdf.cell(10,142,txt = TypeFACe[i])
                pdf.cell(23)
                pdf.cell(10,142,txt = '("Financing Facility") account has been debited with the following details:-')

            if len(TypeFACe[i]) == 22:
                # print('-----------22')
                pdf.cell(10,142,txt = TypeFACe[i])
                pdf.cell(19)
                pdf.cell(10,142,txt = '("Financing Facility") account has been debited with the following details:-')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,152,txt = 'Date of Disbursement')
            pdf.cell(36)
            pdf.cell(10,152,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,152,txt = Date2[i])

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,158,txt = 'Amount Disbursed ')
            pdf.cell(36)
            pdf.cell(10,158,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,158,txt = 'RM')
            pdf.cell(-5)
            pdf.cell(10,158,txt = AMTDisburse[i])

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,164,txt = 'Type of Disbursement')
            pdf.cell(36)
            pdf.cell(10,164,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,164,txt = TYPEDisburse[i])

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,170,txt = 'Total Disbursement to date')
            pdf.cell(36)
            pdf.cell(10,170,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,170,txt = 'RM')
            pdf.cell(-5)
            pdf.cell(10,170,txt = TTLDisburse[i])


            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,178,txt = 'As per our earlier Notice of Disbursement, you shall continue to pay the monthly payment of RM')
            pdf.cell(95)
            if len(MonthlyAMT[i]) == 6:
                pdf.cell(10,178,txt = MonthlyAMT[i])
                pdf.cell(-2)
                pdf.cell(10,178,txt = 'on the first day of each month until full settlement.')
            
            if len(MonthlyAMT[i]) == 8:
                pdf.cell(10,178,txt = MonthlyAMT[i])
                pdf.cell(1)
                pdf.cell(10,178,txt = 'on the first day of each month until full settlement.')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,186,txt = 'Payment can be made through our nationwide branches or alternatively at any of our participating payment channels listed on MBSB Bank website.')

            pdf.ln(2)
            pdf.cell(7)
            pdf.set_font('Arial','',6.8)
            pdf.cell(10,194,txt = 'Please ensure that the payment reaches us before the first day of the month, failing which late payment compensation ("Ta widh") of 1% p.a. on the amount in')

            pdf.ln(1)
            pdf.cell(7)
            pdf.set_font('Arial','',6.8)
            pdf.cell(10,200,txt = 'arrears (not compounded), calculated daily after the due date will be charged and debited into your financing account.')

            pdf.ln(2)
            pdf.cell(7)
            pdf.set_font('Arial','',6.8)
            pdf.cell(10,208,txt = 'Should you have further queries and/or require assistance in relation to your financing account, please contact our Customer Service Center at 03-2096 3000.')

            pdf.ln(2)
            pdf.cell(7)
            pdf.set_font('Arial','',7)
            pdf.cell(10,216,txt = 'Thank you.')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,222,txt = 'Your faithfully,')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,228,txt = 'MBSB BANK BERHAD (716122-P)')

            pdf.ln(1)
            pdf.cell(7)
            pdf.set_font('Arial','',6.8)
            pdf.cell(10,234,txt = 'Note: This is a computer-generated document. No signature is required.')

            pdf.set_line_width(0.05)
            pdf.line(18,160,190,160)


            pdf.ln(1)
            pdf.cell(7)
            pdf.set_font('Arial','',7)
            pdf.cell(10,246,txt = 'Tuan/Puan,')

            pdf.ln(1)
            pdf.cell(7)
            pdf.set_font('Arial','',7)
            pdf.cell(10,252,txt = 'NOTIS PEMBAYARAN')


            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,258,txt = 'NO. AKAUN')
            pdf.cell(36)
            pdf.cell(10,258,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,258,txt = Account_no[i])

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,264,txt = 'KEMUDAHAN PEMBIAYAAN')
            pdf.cell(36)
            pdf.cell(10,264,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,264,txt = TypeFACe[i])

            pdf.set_line_width(0.05)
            pdf.line(18,180,190,180)

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,276,txt = 'Kami merujuk perkara di atas dan ingin memaklumkan bahawa akaun')
            pdf.cell(67)
            if len(TypeFACe[i]) == 14:
                pdf.cell(10,276,txt = TypeFACe[i])
                pdf.cell(9)
                pdf.cell(10,276,txt = '("Kemudahan Pembiayaan") anda telah didebitkan dengan jumlah')
            if len(TypeFACe[i]) == 15:
                pdf.cell(10,276,txt = TypeFACe[i])
                pdf.cell(10)
                pdf.cell(10,276,txt = '("Kemudahan Pembiayaan") anda telah didebitkan dengan jumlah')
            if len(TypeFACe[i]) == 16:
                pdf.cell(10,276,txt = TypeFACe[i])
                pdf.cell(11)
                pdf.cell(10,276,txt = '("Kemudahan Pembiayaan") anda telah didebitkan dengan jumlah')
            if len(TypeFACe[i]) == 17:
                pdf.cell(10,276,txt = TypeFACe[i])
                pdf.cell(12)
                pdf.cell(10,276,txt = '("Kemudahan Pembiayaan") anda telah didebitkan dengan jumlah')
            if len(TypeFACe[i]) == 18:
                pdf.cell(10,276,txt = TypeFACe[i])
                pdf.cell(13)
                pdf.cell(10,276,txt = '("Kemudahan Pembiayaan") anda telah didebitkan dengan jumlah')
            if len(TypeFACe[i]) == 19:
                pdf.cell(10,276,txt = TypeFACe[i])
                pdf.cell(14)
                pdf.cell(10,276,txt = '("Kemudahan Pembiayaan") anda telah didebitkan dengan jumlah')
            if len(TypeFACe[i]) == 20:
                pdf.cell(10,276,txt = TypeFACe[i])
                pdf.cell(20)
                pdf.cell(10,276,txt = '("Kemudahan Pembiayaan") anda telah didebitkan dengan jumlah')
            if len(TypeFACe[i]) == 21:
                pdf.cell(10,276,txt = TypeFACe[i])
                pdf.cell(23)
                pdf.cell(10,276,txt = '("Kemudahan Pembiayaan") anda telah didebitkan dengan jumlah')
            if len(TypeFACe[i]) == 22:
                pdf.cell(10,276,txt = TypeFACe[i])
                pdf.cell(19)
                pdf.cell(10,276,txt = '("Kemudahan Pembiayaan") anda telah didebitkan dengan jumlah')
            
            


            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,282,txt = 'seperti butiran di bawah:-')


            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,290,txt = 'Tarikh Pembayaran')
            pdf.cell(36)
            pdf.cell(10,290,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,290,txt = Date3[i])

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,296,txt = 'Jumlah Pembayaran')
            pdf.cell(36)
            pdf.cell(10,296,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,296,txt = 'RM')
            pdf.cell(-5)
            pdf.cell(10,296,txt = AMTDisburse[i])

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,302,txt = 'Jenis Pembayaran')
            pdf.cell(36)
            pdf.cell(10,302,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,302,txt = TypeFACm[i])

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,308,txt = 'Jumlah Keseluruhan Pembayaran Terkini')
            pdf.cell(36)
            pdf.cell(10,308,txt = ':')
            pdf.cell(-7)
            pdf.cell(10,308,txt = 'RM')
            pdf.cell(-5)
            pdf.cell(10,308,txt = TTLDisburse[i])

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,318,txt = 'Merujuk kepada Notis Pembayaran kami yang terdahulu, bayaran bulanan anda kekal sebanyak RM 485.00 dan hendaklah dibayar pada hari pertama setiap')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,324,txt = 'bulan sehingga penyelesaian penuh.')



            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,334,txt = 'Bayaran boleh dibuat melalui cawangan kami di seluruh negara atau sebagai alternatif di mana-mana saluran pembayaran terpilih seperti yang tersenarai')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,340,txt = 'di laman web MBSB Bank.')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,350,txt = 'Sila pastikan pembayaran dibuat sebelum hari pertama setiap bulan dan sekiranya gagal, pampasan bayaran lewat ("Ta widh") sebanyak 1% setahun')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,356,txt = 'daripada jumlah tunggakan (tidak dikompaun), dikira setiap hari selepas tarikh akhir akan dikenakan dan didebitkan ke dalam akaun pembiayaan anda.')


            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,366,txt = 'Untuk sebarang pertanyaan atau bantuan berkaitan akaun pembiayaan anda, sila hubungi Pusat Khidmat Pelanggan kami di 03-2096 3000.')


            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,376,txt = 'Terima kasih.')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,382,txt = 'Yang benar,')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,388,txt = 'MBSB BANK BERHAD (716122-P)')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,394,txt = 'Nota : Dokumen ini adalah cetakan komputer. Tiada tandatangan diperlukan.')

            pdf.ln(1)
            pdf.cell(130)
            pdf.set_font('Arial','',6)
            pdf.cell(10,440,txt = '00000' +  str(count)  + '(1)MGNOFRLS_20221220.pdf')

            pdf.add_page()

            import pyqrcode
            import png
            from pyqrcode import QRCode
            s = 'ISL' +  str(Name2[i]) +  str(Add1[i]) +  str(Add2[i])  + str(Add3[i]) +  str(Add4[i]) + str(Add5[i]) +  str(Date1[i]) +  str(Account_no[i])
            url = pyqrcode.create(s)
            url.png(r'E:\IWOC\APP SCRIPT\MGNO\CYCLE\mno\DATA\mgno_b\\+%s.png' %(count), scale = 6)


            
            pdf.set_font('Courier','B',7.2)
            pdf.cell(80)
            pdf.cell(10,320,txt = 'PRIVATE  & CONFIDENTIAL')

            pdf.ln(1)
            pdf.cell(50)
            pdf.cell(10,400,txt = '(000-00000' + str(count) + ')')

            pdf.ln(1)
            pdf.cell(50)
            pdf.cell(10,406,txt = str(Name2[i]))

            pdf.ln(1)
            pdf.cell(50)
            pdf.cell(10,412,txt = str(Add1[i]))

            pdf.ln(1)
            pdf.cell(50)
            pdf.cell(10,418,txt = str(Add2[i]))

            pdf.ln(1)
            pdf.cell(50)
            pdf.cell(10,424,txt = str(Add3[i]))

            pdf.ln(1)
            pdf.cell(50)
            pdf.cell(10,430,txt = str(Add4[i]))

            pdf.image(r'E:\IWOC\APP SCRIPT\MGNO\CYCLE\mno\DATA\MBSB02.png',18,20,180)
            pdf.image(r'E:\IWOC\APP SCRIPT\MGNO\CYCLE\mno\DATA\MBSB01.png',150,164,40)
            pdf.image(r'E:\IWOC\APP SCRIPT\MGNO\CYCLE\mno\DATA\NearQR1.PNG',147,40,38)
            pdf.image(r'E:\IWOC\APP SCRIPT\MGNO\CYCLE\mno\DATA\mgno_b\\+%s.png' %(count),110,42,10)

            pdf.set_font('Arial','',6)
            pdf.cell(-18)
            pdf.rotate(180)
            pdf.cell(10,10,txt = '00000' +str(count) + '(1)ISLM_DORREM_20221220.pdf')
            count +=1

    pdf.output('E:\IWOC\APP SCRIPT\MGNO\CYCLE\mno\DATA\mgno1.pdf')

import PyPDF2

pdf_in = open(r'E:\IWOC\APP SCRIPT\MGNO\CYCLE\mno\DATA\mgno1.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    if pagenum % 2:
        page.rotateClockwise(180)
    pdf_writer.addPage(page)

pdf_out = open(r'E:\IWOC\OUTPUT\MGNO\MGNOPDF_1.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()    

