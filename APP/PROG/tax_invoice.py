from fpdf import FPDF
import pandas as pd
from datetime import datetime
from PIL import Image
from barcode import EAN13,Code39
from barcode.writer import ImageWriter
import pandas as pd
from datetime import datetime,date,timedelta
import os
import PyPDF2
def rotate_func(kk):
    pdf_in = open(r"%s\tax_invoce11.pdf"%kk, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        if pagenum % 2:
            page.rotateClockwise(180)
        pdf_writer.addPage(page)

    pdf_out = open(r"%s\tax_invoce.pdf"%kk, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()  

    import os
    os.remove(r"%s\tax_invoce11.pdf"%kk)


def TAX_INV(request,files1):
    move_files = []
    move_files.append(files1)
    p = 1
    cppp = 1
    def Folder_creation(cppp):
        # ------------------Capture date----------------
        cppp=str(cppp)
        today=date.today()
        d1 = today.strftime("%d-%b-%Y")
        # print(d1,'ddddddddddddddddddddddddddddddddd')
        d2=d1[0:2]
        d3=d1[3:6]
        d1=d2+d3+cppp
        # ------------------Capture time----------------
        now = datetime.now()        
        start_time = now.strftime("%H:%M:%S")
        s1=start_time[0:2]
        s2=start_time[3:5]
        s3=start_time[6:8]
        start_time=s1+s2+s3

        # ---------------create first date folder------------
        # import os
        # directory = d
        # print('Helloooooooooooooooooooooooooooooooo')
        directory=d1
        parent_dir = "E:\IWOC\OUTPUT\Bank Simpanan Nasional\CYCLE\\"
        directory = d1+"_"+start_time 
        path1 = os.path.join(parent_dir, directory) # date folder path
        os.mkdir(path1)
        # print("Directory '% s' created" % directory)

        directory = 'tax'
        parent_dir = path1
        path2 = os.path.join(path1, directory) # bkrcc folder path
        os.mkdir(path2)
        # print("Directory '% s' created" % directory)

        directory = 'PRINTING'
        parent_dir = path2
        path3 = os.path.join(path2, directory) # DIGITAL folder path
        os.mkdir(path3)
        # print("Directory '% s' created" % directory)

        # directory = 'PRINTING'
        # parent_dir = path2
        # path4 = os.path.join(path2, directory) # PRINTING folder path
        # os.mkdir(path4)
        # print("Directory '% s' created" % directory)

        return path3

    path11 = r'E:\IWOC\SOURCE\\'+ files1
    data=pd.read_excel(path11)
    # print(data.columns)
    number_of_rows = len(data)
    df=pd.DataFrame()
    df['INVOICE_NUMBER'] = data['INVOICE_NUMBER']
    df['PRINT DATE'] = data['PRINT DATE']
    df['ILOM_OLD_SEQUENCE'] = data['ILOM_OLD_SEQUENCE']
    df['LNAME'] =  data['LNAME']
    df['ADDR1']=data['ADDR1']
    df['ADDR2']=data['ADDR2']
    df['ADDR3']=data['ADDR3']
    df['ADDR4']=data['ADDR4']
    df['POSTCD']=data['POSTCD']
    df['CITY']=data['CITY']
    df['STATECD']=data['STATECD']
    df['SYSDATE_GENERATE'] = data['SYSDATE_GENERATE']
    df['MEMO_ITEM'] = data['MEMO_ITEM']
    df['MEMO_AMOUNT'] = data['MEMO_AMOUNT'].astype(str)
    df['GST_TAX'] = data['GST_TAX']
    df['TOTAL_AMOUNT_INCLUDED_GST'] = data['TOTAL_AMOUNT_INCLUDED_GST']
    # print(df)
    memo_amt = []
    memo_amt_final = []
    memo_amt = data['MEMO_AMOUNT'].to_list()
    for i in memo_amt:
        i = str(i)
        k = i.split(".")
        k0 = k[0]
        k1 = k[-1]
        if len(k1) == 1:
            k1 = k[-1] + '0'
        k2 = k0 + '.' + k1
        memo_amt_final.append(k2)
    
    gst_tax = []
    gst_tax_final = []
    gst_tax = data['GST_TAX'].to_list()
    for i in gst_tax:
        i = str(i)
        k = i.split(".")
        k0 = k[0]
        k1 = k[-1]
        if len(k1) == 1:
            k1 = k[-1] + '0'
        k2 = k0 + '.' + k1
        gst_tax_final.append(k2)
    
    total_amt_inc_tax = []
    total_amt_inc_tax_final = []
    total_amt_inc_tax = data['TOTAL_AMOUNT_INCLUDED_GST'].to_list()
    for i in total_amt_inc_tax:
        i = str(i)
        k = i.split(".")
        k0 = k[0]
        k1 = k[-1]
        if len(k1) == 1:
            k1 = k[-1] + '0'
        k2 = k0 + '.' + k1
        total_amt_inc_tax_final.append(k2)


    df['PRINT DATE'] = df['PRINT DATE'].dt.strftime('%d/%m/%Y')
    sysdate = df['SYSDATE_GENERATE'].to_list()
    sysd = []
    for i in sysdate:
        sysd.append(i.strftime('%d/%m/%Y'))


    dates = df['SYSDATE_GENERATE'].to_list()
    date1 = []
    for i in dates:
        date1.append(i.strftime('%d%m%y'))
    # print(date1,'sysysysysy')

    time1 = datetime.now() 
    start_time=time1.strftime("%H:%M:%S")
    date1 = time1.strftime("%d/%b/%Y")

    file=open(r"E:\\IWOC\\LOG_FILES\\tax-invoice.txt","a")
    file.write("INTERCITY  MPC (M) Sdn. Bhd.\n")
    file.write("FIRST REMINDER\n")
    file.write("=============================================================\n")
    file.write("Program ID           : FIRST REMINDER.PDS\n")
    file.write("Paper Type           :\n")
    


    def barcode(acc_no,count):
        now = datetime.now() 
        date0 = now.strftime("%m%d%y")
        barcode_no = '0905' +  str(date0) +  str(acc_no) 
        # print("date :",date) 
        # print(acc_no,'barcode_nobarcode_nobarcode_no')
        

        number = barcode_no
        my_code = Code39(number, writer=ImageWriter())
        new_code  = 'b' + str(count)
        my_code.save(r"E:\IWOC\barcode_for_tax\%s" %(new_code))

        from PIL import Image

        img = Image.open(r"E:\IWOC\barcode_for_tax\%s.png" %(new_code))
        imgCropped = img.crop(box=(4,10,1080,200))
        imgCropped.save(r"E:\IWOC\barcode_for_tax\%s.png" %(new_code))

    count = 1
    pdf = FPDF()
    for i in range(0,number_of_rows):
        barcode(df['ILOM_OLD_SEQUENCE'][i],count)
        now = datetime.now() 
        date1 = now.strftime("%m%d%y")
        barcode_no1 = '0905' +  str(date1) +  str(df['ILOM_OLD_SEQUENCE'][i])
        # print(barcode_no1)
        # print(date1)
        # print(str(df['ILOM_OLD_SEQUENCE'][i]))
        pdf.add_page()
        pdf.set_auto_page_break(auto=False)
        pdf.set_line_width(6)
        pdf.set_draw_color(r=0, g=0, b=0)
        pdf.line(x1=5, y1=4, x2=205, y2=4)         #1st horizontal line
        pdf.line(x1=5, y1=292, x2=205, y2=292)     #2nd horizontal line 
        pdf.line(5,6,5,290)                         # 1st vertical line
        pdf.line(205,6,205,290)                     # 2nd vertical line    

        pdf.image(r'E:\IWOC\APP SCRIPT\TAX_INVOICE\CYCLE\TAX_INVOICE\DATA\conv_header2.jpg',20,20,30)

        pdf.ln(1)
        pdf.set_font('Arial','B',9)
        pdf.cell(10)
        pdf.cell(10,80,txt ='Tax Invoice No:')

        pdf.cell(14)
        pdf.set_font('Arial','',9)
        pdf.cell(10,80,txt = str(df['INVOICE_NUMBER'][i]))

        pdf.cell(100)
        pdf.set_font('Arial','B',9)
        pdf.cell(10,80,txt = 'Date:  ')

        pdf.cell(-1)
        pdf.set_font('Arial','',9)
        a = str(df['PRINT DATE'][i]) 
        a = a.split()
        a = a[0]
        pdf.cell(10,80,txt = str(a))

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','',9)
        pdf.cell(10,84,txt = 'BANK SIMPANAN NASIONAL')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','',9)
        pdf.cell(10,88,txt = 'Wisma BSN')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','',9)
        pdf.cell(10,92,txt = '117, Jalan Ampang')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','',9)
        pdf.cell(10,96,txt = '50450 Kuala Lumpur')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',9)
        pdf.cell(10,101,txt = 'GST ID No:  ')

        pdf.cell(7)
        pdf.set_font('Arial','B',9)
        pdf.cell(10,101,txt = ' 001673723904')


        pdf.ln(1)
        pdf.cell(80)
        pdf.set_font('Arial','B',10)
        pdf.cell(10,110,txt = 'TAX INVOICE')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',9)
        pdf.cell(10,125,txt = str(df['ILOM_OLD_SEQUENCE'][i]))

        h = 140
        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','',9)
        pdf.cell(10,h,txt = str(df['LNAME'][i]))

        if pd.notna(df['ADDR1'][i]):
            h = h + 5
            pdf.ln(1)
            pdf.cell(10)
            pdf.set_font('Arial','',9)
            pdf.cell(10,h,txt = df['ADDR1'][i])

        if pd.notna(df['ADDR2'][i]):
            h = h + 5
            pdf.ln(1)
            pdf.cell(10)
            pdf.set_font('Arial','',9)
            pdf.cell(10,h,txt = str(df['ADDR2'][i]))

        if pd.notna(df['ADDR3'][i]):
            h = h + 5
            pdf.ln(1)
            pdf.cell(10)
            pdf.set_font('Arial','',9)
            pdf.cell(10,h,txt = str(df['ADDR3'][i]))

        if pd.notna(df['ADDR4'][i]):
            h = h + 5    
            pdf.ln(1)
            pdf.cell(10)
            pdf.set_font('Arial','',9)
            pdf.cell(10,h,txt = str(df['ADDR4'][i]))

        if pd.notna(df['POSTCD'][i]):
            h = h + 5
            pdf.ln(1)
            pdf.cell(10)
            pdf.set_font('Arial','',9)
            pdf.cell(10,h,txt = str(df['POSTCD'][i]))
            pdf.cell(1)
            pdf.cell(10,h,txt = str(df['CITY'][i]))

        if pd.notna(df['STATECD'][i]):
            h = h + 5
            pdf.ln(1)
            pdf.cell(10)
            pdf.set_font('Arial','',9)
            pdf.cell(10,h,txt = str(df['STATECD'][i]) )

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',9)
        pdf.cell(10,200,txt = 'No.')

        pdf.cell(-1)
        pdf.cell(10,200,txt = 'Date')

        pdf.cell(12)
        pdf.cell(10,200,txt = 'Description ')

        pdf.cell(38)
        pdf.cell(10,200,txt = 'Tax Rate')

        pdf.cell(12)
        pdf.cell(10,200,txt = 'Amount')

        pdf.cell(10)
        pdf.cell(10,200,txt = 'GST Amount')

        pdf.cell(13)
        pdf.cell(10,200,txt = 'Total Incl GST')

        pdf.ln(1)
        pdf.cell(96)
        pdf.cell(10,205,txt = '(%)')

        pdf.cell(10)
        pdf.cell(10,205,txt = '(RM)')

        pdf.cell(16)
        pdf.cell(10,205,txt = '(RM)')

        pdf.cell(14)
        pdf.cell(10,205,txt = '(RM)')

        pdf.ln(1)
        pdf.set_line_width(0.1)
        pdf.line(20,134,190,134)

        pdf.cell(10)
        pdf.set_font('Arial','',9)
        pdf.cell(10,230,txt = '1')

        pdf.cell(-3)
        # pdf.set_font('Arial','',9)
        # a = str(df['SYSDATE_GENERATE'][i])
        # a = a.split()
        # a = a[0]
        pdf.cell(10,230,txt = str(sysd[i]))

        pdf.cell(14)
        pdf.set_font('Arial','',9)
        pdf.cell(10,230,txt = str(df['MEMO_ITEM'][i]))

        pdf.cell(42)
        pdf.cell(10,230,txt = '6.00')

        pdf.cell(12)
        pdf.cell(10,230,txt = str(memo_amt_final[i]))

        pdf.cell(16)
        pdf.cell(10,230,txt = str(gst_tax_final[i]))
        
        pdf.cell(14)
        pdf.cell(10,230,txt = str(total_amt_inc_tax_final[i]))

        pdf.ln(1)
        pdf.set_line_width(0.1)
        pdf.line(20,150,190,150)


        pdf.ln(1)
        pdf.set_font('Arial','B',9)
        pdf.cell(88)
        pdf.cell(10,260,txt = 'TOTAL :')

        pdf.cell(16)
        pdf.cell(10,260,txt = str(memo_amt_final[i]))

        pdf.cell(16)
        pdf.cell(10,260,txt = str(gst_tax_final[i]))

        pdf.cell(14)
        pdf.cell(10,260,txt = str(total_amt_inc_tax_final[i]))

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','',9)
        pdf.cell(10,450,txt = 'AGENSI KAUNSELING DAN PENGURUSAN KREDIT TELAH DITUBUHKAN OLEH BANK NEGARA')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,455,txt = 'MALAYSIA UNTUK MENYEDIAKAN PERKHIDMATAN PENGURUSAN KEWANGAN, KAUNSELING KREDIT,')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,460,txt = 'PENDIDIKAN KEWANGAN DAN PENSTRUKTURAN SEMULA PINJAMAN SECARA PERCUMA KEPADA')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,465,txt = 'INDIVIDU. UNTUK MEMBUAT PERTANYAAN, SILA HUBUNGI TALIAN 1-800-88-2575')


        pdf.cell(30)
        pdf.cell(10,490,txt = 'This tax invoice is system generated. No signature is required.')

        pdf.ln(1)
        pdf.cell(120)
        pdf.set_font('Arial','',6)
        pdf.cell(10,498,txt= 'TaxInv 1404-1904_200422.csv-00000' + str(count))

        # pdf.set_line_width(4)
        # pdf.set_draw_color(r=128, g=128, b=128)
        # pdf.line(x1=10, y1=287, x2=200, y2=287) 
        

        # pdf.ln(1)
        # pdf.cell(150)
        # pdf.set_font('Arial','',6)
        # pdf.set_text_color(r = 255,g=255,b=255)
        # pdf.cell(10,506,txt= 'www.mybsn.com.my')
        pdf.image(r'E:\IWOC\APP SCRIPT\TAX_INVOICE\CYCLE\TAX_INVOICE\DATA\newurl.png',8,286.5,194)

        
        pdf.add_page()
        pdf.image(r'E:\IWOC\APP SCRIPT\TAX_INVOICE\CYCLE\TAX_INVOICE\DATA\BSN_Reminder-01.jpg',-10,-10,230)

        # pdf.set_font('Arial','',7)
        # pdf.cell(10,280,txt = '00' + str(c))
        # c += 1
        pdf.ln(1)
        pdf.image(r'E:\IWOC\APP SCRIPT\TAX_INVOICE\CYCLE\TAX_INVOICE\DATA\BSN_Reminder-02.jpg', 12,154,180)

        pdf.ln(1)
        new_code  = 'b' + str(count)
        pdf.image(r'E:\IWOC\barcode_for_tax\%s.png'%(new_code),30,203,70)
        
    
        pdf.cell(22)
        pdf.cell(10,412,txt = str(barcode_no1))
        

        pdf.set_font('times','',7)
        pdf.cell(-34)
        pdf.cell(10,286,txt = '00' + str(count))


        # pdf.set_font('times','',7)
        # pdf.cell(-5)
        # pdf.cell(10,412,txt ='(000)')

        
        # pdf.set_font('times','',7)
        # pdf.cell(-5)
        # pdf.cell(10,412,txt =' -P02 - 01')
        
        h = 430 
        if pd.notna(df['LNAME'][i]):
            pdf.ln(1)
            pdf.set_font('Arial','B',10)
            pdf.cell(22)
            pdf.cell(10,h,txt = str(df['LNAME'][i]))

        if pd.notna(df['ADDR1'][i]):
            h = h + 6
            pdf.ln(1)
            pdf.cell(22)
            pdf.cell(10,h,txt = str(df['ADDR1'][i]))

        if pd.notna(df['ADDR2'][i]):
            h = h  + 6
            pdf.ln(1)
            pdf.cell(22)
            pdf.cell(10,h,txt = str(df['ADDR2'][i]))

        if pd.notna(df['ADDR3'][i]):
            h = h  + 6
            pdf.ln(1)
            pdf.cell(22)
            pdf.cell(10,h,txt = str(df['ADDR3'][i]))

        if pd.notna(df['ADDR4'][i]):
            h = h  + 6
            pdf.ln(1)
            pdf.cell(22)
            pdf.cell(10,h,txt = str(df['ADDR4'][i]))
        
        if pd.notna(df['POSTCD'][i]):
            h = h  + 6
            pdf.ln(1)
            pdf.cell(22)
            pdf.cell(10,h,txt = str(df['POSTCD'][i]))
            pdf.cell(2) 
            pdf.cell(10,h,txt = str(df['CITY'][i]))

        if pd.notna(df['STATECD'][i]):
            h = h  + 6
            pdf.ln(1)
            pdf.cell(22)
            pdf.cell(10,h,txt = str(df['STATECD'][i]))
        count = int(count)
        count += 1
    
    kk=Folder_creation(cppp)
    bk = kk
    # print(kk,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        
    pdf.output(r"%s\tax_invoce11.pdf"%kk)
    if i == number_of_rows-1:
        rotate_func(bk)
    lesson =(r"%s\tax_invoce11.pdf"%kk)
    file_name = os.path.split(lesson)
    ffname = file_name[-1]
    # print(ffname,'saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaam')
    cppp += 1


    file.write("File Name (PDF)      :")
    file.write(str(ffname))
    file.write("\n")
    file.write("Data Name (TXT)      :")
    file.write(str(files1))
    file.write("\n")
    file.write("Total Accounts       :        ")
    file.write(str(number_of_rows))
    file.write("\n")
    file.write("Total Pages          :        ")
    file.write(str(number_of_rows))
    file.write("\n")
    file.write("Total Impression     :        ")
    file.write(str(number_of_rows*2))
    file.write("\n")

    file.write("First Record         : ")
    file.write(str(df['ILOM_OLD_SEQUENCE'][0]))
    file.write("\n")
    file.write("Last Record          : ")
    last_record=df['ILOM_OLD_SEQUENCE'].iat[-1]
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
    
    
    # pdf.output(r'E:\IWOC\APP SCRIPT\TAX_INVOICE\CYCLE\TAX_INVOICE\DATA\tax.pdf') 
    time1 = datetime.now()
    end_time=time1.strftime("%H:%M:%S")
    file.write("    ")
    file.write(str(end_time) )
    file.write('\n\n\n\n')
    file.close()

 

    # path20 = r'E:\IWOC\SOURCE' 
    # target = r'E:\IWOC\TEMP' 

    # for i in move_files:

    #     src_path = os.path.join(path20, i)
    #     dst_path = os.path.join(target, i)
    #     os.rename(src_path, dst_path)
    # print('Files Moved................')
