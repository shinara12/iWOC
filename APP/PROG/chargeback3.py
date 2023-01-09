import pandas as pd
import PyPDF2
from fpdf import FPDF
from datetime import datetime

def CHARGEBACK3(request,files1):
    move_files = []
    move_files.append(files1)
    path11=r'E:\IWOC\SOURCE\\'+ files1
    # path11 = r'C:\Users\Lenovo\Desktop\demo\ASBI-191022.txt'
    with open(path11) as file:
        Total_lines=len(file.readlines())
        print('Total Lines ',Total_lines)
        file.seek(0)
        Account_no=[]
        Account_no1=[]
        Commencement_date=[]
        Drawdown_date=[]
        Monthly_inst_amt=[]
        profit_due=[]
        Name=[]
        add1=[]
        add2=[]
        add3=[]
        add4=[]
        add5=[]
        hno = []    # add new rahul

        for i in file:
            line=i.strip()
            Account_no.append(line[0:12])
            Account_no1.append(line[1:5])
            Name.append(line[22:44].strip())
            Monthly_inst_amt.append(line[110:119])
            profit_due.append(line[166:171])
            Commencement_date.append(line[12:22])
            Drawdown_date.append(line[118:128])
            add1.append(line[248:280].strip())
            add2.append(line[288:325].strip())
            add3.append(line[328:350].strip())
            hno.append(line[208:236].strip())

    mylist =[]
    list =[]
    list1 = []

    with open(r"E:\IWOC\SOURCE\OML-191022.txt") as f:
        for line in f:
            if line.startswith(r"!1!"):
                line = line.strip()
                line = line[3:]
                line = line[0:-2].split("\\")
                list.append(line)
                line = str(line)
            if line.startswith(r"!2!"):
                line = line.strip()
                line = line[3:]
                line = line[0:-2].split("\\")
                list.append(line)
            if '!3!' in line:
                list1.append(line[0:20])
    total_desc_lines = len(list)

    time1 = datetime.now() 
    start_time=time1.strftime("%H:%M:%S")
    date1 = time1.strftime("%d/%b/%Y")

    file=open(r"E:\\IWOC\\LOG_FILES\\chargeback3.txt","a")
    file.write("Pro Office Solutions Sdn. Bhd.\n")
    file.write("FIRST REMINDER\n")
    file.write("=============================================================\n")
    file.write("Program ID           : FIRST REMINDER.PDS\n")
    file.write("Paper Type           :\n")
    file.write("File Name (PDF)      : R1 31102022_011122.srt.PDF\n")
    file.write("Data Name (TXT)      : R1 31102022_011122.srt\n")
    file.write("Total Accounts       :        ")
    file.write(str(Total_lines))
    file.write("\n")
    file.write("Total Pages          :        ")
    file.write(str(Total_lines))
    file.write("\n")
    file.write("Total Impression     :        ")
    file.write(str(Total_lines*2))
    file.write("\n")

    file.write("First Record         : ")
    file.write(str(Account_no[0]))
    file.write("\n")
    file.write("Last Record          : ")
    last_record=str(Account_no[-1])
    file.write(str(last_record))
    file.write("\n")
    file.write("=============================================================\n")
    file.write("CUSTOMER NAME        : BSN                                   \n")
    file.write("=============================================================\n")
    file.write("Date & Time processed: ")


    file.write(str(date1))
    file.write("    ")
    file.write(str(start_time))
    file.write("    " )
    
    pdf = FPDF()
    for i in range(0,Total_lines):
        pdf.add_page()
        pdf.image(r'E:\IWOC\APP SCRIPT\CHARGEBACK3\CYCLE\CHARGEBACK3\DATA\MiB-02.jpg',30,15,50)
        pdf.set_auto_page_break(auto=False)
        pdf.set_line_width(4)
        pdf.set_draw_color(r=0, g=0, b=0)
        pdf.line(x1=5, y1=4, x2=205, y2=4)         #1st horizontal line
        pdf.line(x1=5, y1=292, x2=205, y2=292)     #2nd horizontal line 
        pdf.line(5,6,5,290)                         # 1st vertical line
        pdf.line(205,6,205,290)                     # 2nd vertical line    

        pdf.ln(1)
        pdf.set_font('Arial','',8)
        pdf.cell(10)
        pdf.cell(10,50,txt = 'Tarikh   :'  )
        pdf.cell(10)
        pdf.cell(10,50,txt = Commencement_date[i])
        pdf.cell(110)
        pdf.cell(10,50,txt = 'Sulit & Persendirian')
        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,56,txt = 'Date     :')
        pdf.cell(130)
        pdf.cell(10,56,txt = 'Private & Confidential')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,70,txt = 'Tuan/Puan,')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,76,txt = 'Sir/Madam,')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',9)
        pdf.cell(10,88,txt = 'NOTIS PENGELURAN PENUH PEMBIAYAAN DAN PERMULAAN BAYARAN ANSURAN BULANAN')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','BI',9)
        pdf.cell(10,94,txt = 'NOTICE ON FULL DISBURSEMENT OF FACILITY AND COMMENCEMENT OF MONHLY INSTALLMENT')

        pdf.ln(1)
        pdf.set_font('Arial','B',8)
        pdf.cell(10)
        pdf.cell(10,104,txt = 'No.Akaun :')
        
        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','BI',8)
        pdf.cell(10,110,txt = 'Account No:')

        pdf.cell(50)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,110,txt = Account_no[i])
        # pdf.cell(10,110,txt = '4-01011-03538-5')

        pdf.ln(1)
        # pdf.cell(10)
        # pdf.cell(10,122,txt = 'Keuntungan Progresif Yang Perlu Dibayar')

        pdf.ln(1)
        # pdf.cell(10)
        # pdf.set_font('Arial','BI',8)
        # pdf.cell(10,128,txt = 'Progressive Profit Due')

        # pdf.cell(50)
        # pdf.set_font('Arial','B',8)
        # pdf.cell(10,128,txt = 'RM')

        # pdf.cell(10)
        # pdf.cell(10,128,txt = profit_due[i])

        pdf.set_font('Arial','B',8)
        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,122,txt = 'Jumlah Bayaran Ansuran')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','BI',)
        pdf.cell(10,128,txt = 'Monthly Installment Amoumt')

        pdf.cell(50)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,128,txt = 'RM')

        pdf.cell(10)
        pdf.cell(10,128,txt = Monthly_inst_amt[i])


        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,140 ,txt = 'Tarikh Ansuran Bermula')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,148,txt = 'Commencement Date')

        pdf.cell(50)
        pdf.cell(10,148,txt = Drawdown_date[i])

        pdf.ln(1)
        # pdf.cell(10)
        # pdf.set_font('Arial','B',8)
        # pdf.cell(10,176,txt = 'Tarikh Pengeluran Penuh')
        
        pdf.ln(1)
        # pdf.cell(10)
        # pdf.set_font('Arial','BI',8)
        # pdf.cell(10,182,txt = 'Final Drawdown rate')

        # pdf.cell(50)
        # pdf.set_font('Arial','B',8)
        # pdf.cell(10,182,txt = Commencement_date[i])

        pdf.set_line_width(0.2)
        pdf.line(20,105,195,105)

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','',8)

        
        pdf.image(r'E:\IWOC\APP SCRIPT\CHARGEBACK3\CYCLE\CHARGEBACK3\DATA\MiB-03.jpg', 20, 260 , 15)        

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,170,txt = 'Kami ingin memaklumkan bahawa pengeluaran penuh untuk akaun pembiayaan anda telah dibuat pada')

    # date to be mentioned here 
       
        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,176,txt = 'Please be informed that the bank has fully disbursed your financing account on ^FullRelDte^')

        
        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,182,txt = 'Pembayaran untuk ansuran bulanan anda bermula seperti dinyatakan di atas.')
       
        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,188,txt = 'Kindly effect your instalment payment effective from the above date.')
        

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,192,txt = 'Penyata pembiayaan akan dihantar kepada anda sekali setahun untuk tujuan rekod. Sebagai alternatif,.')
       
        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,198,txt = 'anda boleh menyemak maklumat terperinci di Maybank2U. Bagi akaun pembayaran melalui Arahan.')


        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,204,txt = 'Bayaran dan tarikh pembayaran adalah pada.')
        

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,210,txt = 'Kindly settle all progressive interest due before the commencement date of the instalment amount in order ')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,216,txt = 'to avoid penalty interest being imposed.')


        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,222,txt = 'Penyata pembiayaan akan dihantar kepada anda sekali setahun untuk tujuan rekod. Sebagai alternatif')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,228,txt = 'anda boleh menyemak maklumat terperinci di Maybank2U. Untuk akaun pembayaran melalui Arahan Tetap')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,234,txt = ' tarikh pembayaran adalah pada 1 haribulan pada setiap bulan.')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,240,txt = 'The facility statement will be sent to you once a year for record purposes. Alternatively, you may check the')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,246,txt = 'details via Maybank2U. For accounts with Standing Instruction arrangement, the payment due date will be')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,252,txt = ' on the 1st day of each month.')

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,258,txt = 'Sila hubungi cawangan Bank, di mana akaun kemudahan pembiayaan anda diselenggarakan, jika anda')


        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,264,txt = 'memerlukan penjelasan lanjut')


        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,270,txt = 'Do contact our branch, where your banking facility account is maintained, if you need further clarification')

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,276,txt = 'Sila maklumkan kepada Pihak Bank dengan SEGERA sekiranya terdapat apa-apa perubahan alamat dan')

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10) 
        pdf.cell(10,282,txt = ' nombor telefon.')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,288,txt = 'Kindly notify the Bank IMMEDIATELY if there is any change of address and telephone number')

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,294,txt = 'Terima kasih kerana menggunakan perkhidmatan perbankan kami')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,300,txt = 'Thank you for banking with us')


        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,306,txt = 'Yang benar,')

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,312,txt = 'bagi pihak!3! Maybank')


        pdf.ln(8)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,316,txt = 'Ini adalah cetakan komputer, tandatangan tidak diperlukan.,')

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,322,txt = 'This is a computer generated, no signature is required.')

        pdf.add_page()
        pdf.image(r'E:\IWOC\APP SCRIPT\CHARGEBACK3\CYCLE\CHARGEBACK3\DATA\MiB-01.jpg',5, 10,200)
        pdf.ln(1)
        pdf.set_font('Arial','B',10)
        pdf.cell(40)
        pdf.cell(10,420,txt = Name[i])

        pdf.ln(1)
        pdf.cell(40)
        pdf.cell(10,426,txt = add1[i])

        pdf.ln(1)
        pdf.cell(40)
        pdf.cell(10,432,txt = hno[i])

        pdf.ln(1)
        pdf.cell(40)
        pdf.cell(10,438,txt = add2[i])

        pdf.ln(1)
        pdf.cell(40)
        pdf.cell(10,444,txt = add3[i])

    pdf.output(r'E:\IWOC\APP SCRIPT\CHARGEBACK3\CYCLE\CHARGEBACK3\DATA\MBB00_OML.pdf')
    time1 = datetime.now()
    end_time=time1.strftime("%H:%M:%S")
    file.write("    ")
    file.write(str(end_time) )
    file.write('\n\n\n\n')
    file.close()
    
    import PyPDF2

    pdf_in = open(r'E:\IWOC\APP SCRIPT\CHARGEBACK3\CYCLE\CHARGEBACK3\DATA\MBB00_OML.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        if pagenum % 2:
            page.rotateClockwise(180)
        pdf_writer.addPage(page)

    pdf_out = open(r'E:\IWOC\OUTPUT\CHARGE BACK\ALL\MBB00_OML.pdf', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()    

    count = pd.Series(Account_no1).value_counts()
    df = pd.DataFrame({'BRCD':count.index, 'TOTACC':count.values})
    df['TOTPGS'] = df['TOTACC']
    df = df.sort_values(['BRCD'])

    import os
    base_filename = r'E:\IWOC\OUTPUT\CHARGE BACK\ALL\maybank_Acc_oml.txt'
    with open(os.path.join(base_filename),'w') as outfile:
        df.to_string(outfile,index=False)

    filename = 'E:\IWOC\SOURCE\dbMbbCBack.txt'
    brc = []
    br_name = []
    Cos_ctr = []
    BRCD = []

    with open(filename) as file:
        for line in file:
            brc.append(line[1:5])
            br_name.append(line[6:25])
            Cos_ctr.append(line[-9:-3])

    for i in br_name:
        i = i.strip()
        BRCD.append(i)

    df1 = pd.DataFrame()
    df1['BRCD'] = brc
    df1['COSCTR'] = Cos_ctr
    df1['BRANCH_NAME'] = BRCD
    print('--------')

    final_ouptut = pd.merge(df,df1,on=['BRCD'])

    import os
    base_filename = r'E:\IWOC\OUTPUT\CHARGE BACK\ALL\mapping_file_oml.txt'
    with open(os.path.join(base_filename),'w') as outfile:
        final_ouptut.to_string(outfile,index=False)


    path20 = r'E:\IWOC\SOURCE' 
    target = r'E:\IWOC\TEMP' 

    for i in move_files:
        src_path = os.path.join(path20, i)
        dst_path = os.path.join(target, i)
        os.rename(src_path, dst_path)
    print('Files Moved................')