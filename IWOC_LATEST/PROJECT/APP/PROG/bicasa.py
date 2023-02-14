from reportlab.pdfgen import canvas
import datetime
from fpdf import FPDF
import pandas as pd
from PyPDF2 import PdfFileMerger
from fpdf import FPDF
from os import path
from turtle import pen
from PyPDF2 import PdfFileWriter, PdfFileReader
import pandas as pd
from fpdf import FPDF
import docx
import pandas as pd
import os
from datetime import datetime
from datetime import date
def Folder_creation_non_email(kc1):
    # ------------------Capture date----------------
    kc1=str(kc1)
    today =date.today()
    d1 = today.strftime("%d-%b-%Y")
    d2=d1[0:2]
    d3=d1[3:6]
    d1=d2+d3+kc1
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
    # directory=d1
    parent_dir = "E:\IWOC\OUTPUT\BICASA\CYCLE/"
    directory = d1+"_"+start_time 
    path1 = os.path.join(parent_dir, directory) # date folder path
    os.mkdir(path1)
    # print("Directory '% s' created" % directory)

    directory = 'BIMB'
    parent_dir = path1
    path2 = os.path.join(path1, directory) # bkrcc folder path
    os.mkdir(path2)
    # print("Directory '% s' created" % directory)


    directory = 'PRINTING'
    parent_dir = path2
    path4 = os.path.join(path2, directory) # PRINTING folder path
    os.mkdir(path4)
    # print("Directory '% s' created" % directory)

    return path4


def Folder_creation_email(kc1):
    # ------------------Capture date----------------
    kc1=str(kc1)
    today =date.today()
    d1 = today.strftime("%d-%b-%Y")
    d2=d1[0:2]
    d3=d1[3:6]
    d1=d2+d3+kc1
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
    # directory=d1
    parent_dir = "E:\IWOC\OUTPUT\BICASA\CYCLE/"
    directory = d1+"_"+start_time 
    path1 = os.path.join(parent_dir, directory) # date folder path
    os.mkdir(path1)
    # print("Directory '% s' created" % directory)

    directory = 'BIMB'
    parent_dir = path1
    path2 = os.path.join(path1, directory) # bkrcc folder path
    os.mkdir(path2)
    # print("Directory '% s' created" % directory)

    directory = 'DIGITAL'
    parent_dir = path2
    path3 = os.path.join(path2, directory) # DIGITAL folder path
    os.mkdir(path3)
    # print("Directory '% s' created" % directory)

    return path3

def BICASA(request,files1):
    move_files = []
    move_files.append(files1)
    kc1 = 1
    kk1 = Folder_creation_email(kc1)
    kc2 = 11
    kk2 = Folder_creation_non_email(kc2) 

 #----------------------- data captured from word file-----------------
    doc = docx.Document(r'E:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Copy of DD7405F.docx')
    all_docs = doc.paragraphs

    email_id = []
    Account_no = []

    for i in all_docs:
        a = i.text
        if '@' in a:
            email_id.append(a[20:52])
            Account_no.append(a[8:19])
    # print(Account_no,'))))))))')
        
    df1 = pd.DataFrame()
    df1['account_no'] = Account_no
    df1['email_id'] = email_id

    path11=r'E:\IWOC\SOURCE\\'+ files1
    #---------------email data ends here-----
    with open(path11) as file:
        k=file.readlines()
        total_lines=len(k)
        total_accounts=0
        for i in k:
            i=i.strip()
            if 'ACCOUNT NO  ' in i:
                total_accounts=total_accounts+1
                file.readline()
                # print(i)
        print('Total Accounts',total_accounts)
        print('Total Lines',total_lines)

    a1=[]
    client_name=[]
    statement_date=[]
    add1=[]
    add2=[]
    add3=[]
    add4=[]
    account_no=[]
    branch=[]
    date_list=[]
    bal_bf =[]
    desc=[]
    debit = []
    total_debit=[]
    total_date_list = []
    len_list = []
    credit=[]
    total_credit=[]

    monthly_average=[]
    total_bal = []
    bal = []
    with open(path11) as file:
        for i in file:
            if 'ACCOUNT NO  ' in i:
                account_no.append(i[109:120].strip())
    

        for i in range(0,total_lines):
            line=file.readline()
            line=line.strip()
            if line.startswith('.'):
                l2=file.readline()
                a1.append(l2[90:103])
                l3=file.readline()
                l3=l3.strip()
                client_name.append(l3[0:40])
                l4=file.readline()
                l4=l4.strip()
                statement_date.append(l4[112:130])
                l5=file.readline()
                l5=l5.strip()
                add1.append(l5[0:10])
                l5=file.readline()
                l5=l5.strip()
                add2.append(l5[0:15])
                l6=file.readline()
                l6=l6.strip()
                add3.append(l6[0:15])
                l7=file.readline()
                add4.append(l7[0:15])
                # account_no.append(l7[109:120])
                l8=file.readline()
                l9=file.readline()
                l9=l9[89:115]
                l9=l9.strip()
                branch.append(l9)
    #-----------------------Total debit, credit----------------------------------------
    #------In source file we have keyword DATE DESCRIPTION which is start of transation, 
    # -----Here , we have captured start location of this keyword -----------------------------------
    print(len(account_no),'****************************************')
    with open(path11) as file:
            c=-1
            date_start_line_number=[]
            total_debit=[]
            for line in file:
                c=c+1
                line=line.strip()
                if line.startswith('DATE    DESCRIPTION  '):
                    date_start_line_number.append(c)
            date_start_line_number.append(total_lines)
    with open(path11) as file:
            lines=file.readlines()
            file.seek(0)
            line=file.readline()
            num=0
            start_date_list=[]
            for line in file:
                line=line.strip()
                num+=1
                if '/' in line:
                    if line.startswith(('1','2','3','4','5','6','7','8','9','0')):
                        start_date_list.append(num)                


    with open(path11) as file:
            lines=file.readlines()
            msg_total_debit=[]
            msg_total_credit=[]
            monthly_avg=[]
            total_desc0=[]
            total_desc1=[]
            total_desc2=[]
            total_desc3=[]
            total_desc4=[]
            a=0
            b=date_start_line_number[1]
            print(b,'date_start_line_number')
            c=2
            lenght=len(date_start_line_number)
            flag='False'
            while c<=lenght:
                flag1='False'
                flag2='False'
                flag3='False'
                for i in range(a,b):
                    line=lines[i].strip()
                    if 'PROFIT PAID' in line:
                        line1=lines[i+1].strip()
                        line1=line1.strip()
                        line2=lines[i+2].strip()
                        line2=line2.strip()
                        line3=lines[i+3].strip()
                        line3=line3.strip()
                        if 'TOTAL DEBIT' in line1:
                            msg_total_debit.append(line1[25:50])     
                            flag1='True'  
                        if 'TOTAL CREDIT' in line2:
                            msg_total_credit.append(line2[25:50])     
                            flag2='True'  
                        if 'MONTHLY AVERAGE' in line3:
                            flag3='True'  

                if flag1=='False':
                    pass
                    msg_total_debit.append('Test')              
                if flag1=='False':
                    pass
                    msg_total_credit.append('Test')

                if flag1=='False':
                    monthly_avg.append('Test')              
                if c==lenght:
                    break
                a=b
                b=date_start_line_number[c]
                c=c+1

    #-----------------------------------------------------------------------------------
    with open(path11) as file:
            line=file.readline()
            copy = False
            date_list=[]
            desc0=[]
            desc1 = []
            desc2 = []
            desc3 = []
            desc4 = []
            bal_bf = []
                    
            debit = []
            for i in range(0,len(date_start_line_number)-1):
                
                a=date_start_line_number[i]
                b=date_start_line_number[i+1]
                date_line=lines[a]
                date_line=date_line.strip()
                for j in range(a,b):
                    line1 = lines[j]
                    line1 = line1.strip()
                    if j<b-1:
                        line2 = lines[j+1]
                        line2 = line2.strip()
                    if j<b-2:
                        line3 = lines[j+2]
                        line3 = line3.strip()
                    if j<b-3:
                        line4 = lines[j+3]
                        line4 = line4.strip()
                    if '/' in line1 and line1.startswith(('1','2','3','4','5','6','7','8','9','0')):
                        desc0.append(line1[8:20].strip())
                        dl=line1[0:8].strip()
                        date_list.append(dl)
                        db=line1[67:72].strip()
                        debit.append(db)
                        ba=line1[109:119].strip()
                        bal.append(ba)
                        cr=line1[90:100].strip()
                        credit.append(cr)
                        if '/' in line2 :
                            desc1.append('desc_TEST')
                            desc2.append('desc_TEST')
                            desc3.append('desc_TEST')
                            continue
                        else:
                            if line2.startswith('TOTAL'):
                                desc1.append('desc_TEST')
                            else:
                                desc1.append(line2[0:8])
                        if '/' in line3 or 'T0TAL' in line3:
                            desc2.append('desc_TEST')
                            desc3.append('desc_TEST')
                            continue
                        else:
                            if line3.startswith('TOTAL'):
                                desc2.append('desc_TEST')
                            else:
                                desc2.append(line3[0:8])
                            
                        if '/' in line4 or 'T0TAL' in line4:
                            desc3.append('desc_TEST')
                            continue
                        else:
                            if line4.startswith('TOTAL') or line4.startswith('MONTHLY'):
                                desc3.append('desc_TEST')
                            else:
                                desc3.append(line4[0:10])
                    else:
                        continue
                total_debit.append(debit)
                debit = []
                total_credit.append(credit)
                credit=[]
                total_date_list.append(date_list)
                date_list = []
                total_desc0.append(desc0)
                desc0=[]          
                total_desc1.append(desc1)
                desc1=[]          
                total_desc2.append(desc2)
                desc2=[]          
                total_desc3.append(desc3)
                desc3=[]   
                total_bal.append(bal)
                bal = []       
            for i in range(0,len(date_start_line_number)-1):
                aa=date_start_line_number[i]+2
                l1=lines[aa]
                l1 = l1.strip()
                if l1.startswith('BAL B/F'):
                    # print(l1,'L!----------------------------------')
                    linee=l1[80:120]
                    linee=linee.strip()
                    bal_bf.append(linee)
                else:
                    bal_bf.append('TEST')
            total_date_list.append(date_list)
            total_desc0.append(desc0)
            total_desc1.append(desc1)
            total_desc2.append(desc2)
            total_desc3.append(desc3)
            total_debit.append(debit)
            total_bal.append(bal)
            total_credit.append(credit)
            total_date_list.pop()
            total_bal.pop()
            total_debit.pop()
            total_desc0.pop()
            total_desc1.pop()
            total_desc2.pop()
            total_desc3.pop()
            total_credit.pop()
            for i in total_date_list:
                len_list.append(len(i))
            max_List1=max(len_list)
            for item in total_date_list:               
                while len(item) < max_List1:   
                    item.append('Test')
            for item in total_debit:               
                while len(item) < max_List1:   
                    item.append('Test')
            for item in total_bal:               
                while len(item) < max_List1:   
                    item.append('Test')
            for item in total_credit:               
                while len(item) < max_List1:   
                    item.append('Test')

            print('Most Transactions of one client are --', max_List1)
            # print(total_desc0,len(total_desc0),'desc0')
            # print('--------------------------------------')
            # print(total_desc1,len(total_desc1),'desc1')
            # print('--------------------------------------')
            # print(total_desc2,len(total_desc2),'desc2')
            # print(total_desc3,len(total_desc3),'desc3')
            # print(total_date_list,'d',len(total_date_list))
            # print('--------------------------------------')
            # print(total_debit,len(total_debit),'debit')
            # print('--------------------------------------')
            # print('--------------------------------------')
            # print(total_bal,len(total_bal),'total_bf')
            # print(total_credit,len(total_credit),'credit')
    # print(bal,'bal')
    df2 = pd.DataFrame()
    df2['account_no'] = account_no               # df2 text file

    result  = pd.merge(df1,df2,how = 'inner', on = ['account_no'])
    email = result['email_id']

    email_account_no = list(result['account_no'])
    Total_email_accounts=len(email_account_no)
    Total_non_email_account=total_accounts-Total_email_accounts
    print('Total Accounts email BICASA-->',Total_email_accounts)
    print('Total Accounts without email BICASA-->',Total_non_email_account)
    pdf = FPDF()



    
    #-----------------------------function with nonemailids------------------------------
    c=1
    c = c + 1
    # for i in range(0,len(bal_bf)):
    #     if bal_bf[i] != 'TEST':
    #         print(bal_bf[i],'******************************8')
    for i in range(0,total_accounts):
        if account_no[i] not in email_account_no: 
            pdf.add_page()
            pdf.image('E:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Left_logo.jpg',10,15,60)
            pdf.image('E:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Right_logo.jpg',160,15,33)
            pdf.set_auto_page_break(auto=False)

            pdf.set_font('Arial', '', 9)
            pdf.cell(4)
            pdf.cell(10,70,txt = 'TUAN SULAIMAN AKHLAKEN BIN SADIQ SEGARAG.')

            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,72,txt = 'A')

            pdf.set_font('Arial','B',9)
            pdf.cell(90)
            pdf.cell(30,70,txt = 'TARIKH PENYATA')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,74,txt = 'Unit A-11-12')

            pdf.set_font('Arial','I',9)
            pdf.cell(90)
            pdf.cell(30,74,txt = 'STATEMENT DATE')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,76,txt = 'Hermington Condo,')

            pdf.set_font('Arial','B',9)
            pdf.cell(90)
            pdf.cell(30,78,txt = 'HALAMAN')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,78,txt = 'No. 3, Jalan Indrahana 3,')

            pdf.set_font('Arial','I',9)
            pdf.cell(90)
            pdf.cell(30,82,txt = 'Page')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,80,txt = 'Taman Indrahana')

            pdf.set_font('Arial','B',9)
            pdf.cell(90)
            pdf.cell(10,86,txt = 'NOMBOR AKAUN')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,82,txt = 'Jalan Kuchai Lama')

            pdf.set_font('Arial','I',9)
            pdf.cell(90)
            pdf.cell(10,90,txt = 'ACCOUNT NO  ')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,84,txt = '58200 Kuala Lumpur')

            pdf.set_font('Arial','B',9)
            pdf.cell(90)
            pdf.cell(10,94,txt = 'CAWANGAN')

            pdf.set_font('Arial','I',9)
            pdf.cell(-10)
            pdf.cell(10,102,txt = 'BRANCH ')

            #-----------------------------------------INSERTING VALUES OF NAME,ADDRESS,ACC,BRANCH ON 2 PAGE-----------

            pdf.set_font('Arial', 'B', 9)
            pdf.cell(50)
            pdf.cell(10,55,txt = '30/09/25')

            pdf.ln(2)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(160)
            pdf.cell(10,66,txt = 'Page 2 of 3')

            pdf.ln(2)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(152)
            pdf.cell(10,78,txt = str(account_no[i]))

            pdf.ln(2)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(142)
            pdf.cell(10,90,txt = 'MENARA BANK ISLAM')

            #-----------------------INSERTING ACCOUNT STATEMENT AND SAVING ACCOUNT ON 2 PAGE----------------------
            pdf.ln(1)
            pdf.set_font('Arial','B',9)
            pdf.cell(4)
            pdf.cell(10,100,txt = 'PENYATA AKAUN / ')

            pdf.set_font('Arial','BI',9)
            pdf.cell(20)
            pdf.cell(10,100,txt = 'ACCOUNT STATEMENT ')

            pdf.ln(1)
            pdf.set_font('Arial','',9)
            pdf.cell(4)
            pdf.cell(10,106,txt = 'AKAUN SIMPANAN / ')

            pdf.set_font('Arial','',9)
            pdf.cell(20)
            pdf.cell(10,106,txt = ' SAVINGS ACCOUNT')

            pdf.ln(1)
            pdf.set_font('Arial','',8)
            pdf.cell(4)
            pdf.cell(10,112,txt = '(Dilindungi oleh PIDM setakat RM250,000 bagi setiap pendeposit. /')

            pdf.set_font('Arial','I',8)
            pdf.ln(1)
            pdf.cell(5)
            pdf.cell(10,118,txt = 'Protected by PIDM up to RM250,000 for each depositor.)')

                #-----------------------------------INSERTING 2ND PAGE TABLE-------------------------------------

            if 'TEST' in bal_bf[i]:
                pdf.ln(1)
                pdf.set_fill_color(r=211,g=211,b=211)
                pdf.set_line_width(0.01)
                pdf.rect(x = 15 , y = 100 , w = 180 , h = 15, style = 'DF')

                pdf.set_line_width(0.5)
                pdf.line(40,100, 40, 115)                      # first  | line
                pdf.line(110,100, 110, 115)                    # second | line
                pdf.line(140,100, 140, 115)                    # third | line
                pdf.line(170,100,170,115)                      # fourth | line

                #-------------------------------------INSERTING 2ND PAGE TABLE COLUMN NAMES---------------------------------

                pdf.ln(1)
                pdf.set_font('Arial', 'B', 9)
                pdf.cell(10)
                pdf.cell(30,134,txt = 'TARIKH')
                pdf.cell(6)
                pdf.cell(30,134,txt = 'KETERANGAN')
                pdf.cell(30)
                pdf.cell(30,134,txt = 'DEBIT')
                pdf.cell(4)
                pdf.cell(25,134,txt = 'KREDIT')
                pdf.cell(1)
                pdf.cell(25,134,txt = 'BAKI')


                pdf.ln(4)

                pdf.set_font('Arial', 'I', 9)
                pdf.cell(10)
                pdf.cell(30,136,txt = 'DATE')
                pdf.cell(6)
                pdf.cell(30,136,txt = 'DESCRIPTION')
                pdf.cell(30)
                pdf.cell(25,136,txt = 'DEBIT')
                pdf.cell(8)
                pdf.cell(25,136,txt = 'CREDIT')
                pdf.cell(1)
                pdf.cell(25,136,txt = 'BALANCE')

                pdf.ln(4)

                pdf.set_font('Arial', 'B', 9)
                pdf.cell(10)
                pdf.cell(30,138,txt = '')
                pdf.cell(6)
                pdf.cell(30,138,txt = '')
                pdf.cell(35)
                pdf.cell(25,138,txt = 'RM')
                pdf.cell(5)
                pdf.cell(25,138,txt = 'RM')
                pdf.cell(1)
                pdf.cell(25,138,txt = 'RM')

            #     #--------------------------------------------INSERTING 1ST TABLE DATA OF 1ST PAGE-----------------
                h = 147
                p2=h
                cc=1
                dd=115

                m1=h
                m2=h
                flag11=False
                line_flag = 'a'
                for j in range(0,10):
                    if total_date_list[i][j] != 'Test':
                        pdf.set_line_width(0.01)

                        pdf.ln(1)
                        pdf.cell(10)
                        pdf.cell(10,h,txt = str(total_date_list[i][j]))

                        pdf.cell(10)
                        pdf.cell(10,h,txt = str(total_desc0[i][j]))

                        pdf.cell(80)
                        pdf.cell(10,h,txt = str(total_debit[i][j]))
                        pdf.cell(20)
                        pdf.cell(10,h,txt = str(total_credit[i][j]))

                        pdf.cell(8)
                        pdf.cell(10,h,txt = str(total_bal[i][j]))    
                        if total_desc1[i][j]!='desc_TEST':
                            pdf.ln(1)
                            pdf.cell(30)
                            h=h+4
                            pdf.set_font('Arial','B',8)
                            pdf.cell(20,h,txt =  str(total_desc1[i][j]))
                            cc=cc+1  
                            line_flag = 'a1'
                        if total_desc2[i][j]!='desc_TEST':                                                
                            pdf.ln(1)                                              
                            pdf.cell(30)
                            h=h+4                                          # 31,33,35,37,39,41
                            pdf.cell(10,h,txt =  str(total_desc2[i][j]))   #  27,29,31,33,35                         
                            cc=cc+1  
                            line_flag = 'a2'
                        if total_desc3[i][j]!='desc_TEST':
                            pdf.ln(1)        
                            pdf.cell(30)
                            h=h+2
                            pdf.cell(10,h,txt =  str(total_desc3[i][j]))   
                            cc=cc+1  
                            line_flag = 'a3'
                        pdf.ln(2)
                        if total_desc1[i][j]=='desc_TEST':
                            p1=h-25-j*2+2*j
                        else:
                            if line_flag == 'a1':
                                p1=h-27.5-j*0.1
                                print(p1,'a1p111111111111111111111')
                                pdf.line(15,p1,195,p1)
                            elif line_flag == 'a2':
                                p1=h-27-j*2
                                print(p1,'a2p111111111111111111111')
                                pdf.line(15,p1,195,p1)
                            elif line_flag == 'a3':
                                p1=h-27-j*2
                                print(p1,'a3p111111111111111111111')
                                pdf.line(15,p1,195,p1)
                            # else:
                            #     p1=hh-29-j
                            #     pdf.line(15,p1,195,p1)
                                


                        # print(p1,h,cc,'-----------')
                        pdf.line(15,dd-cc+1.6, 15,p1)                       # 1st vertical line
                        pdf.line(40,dd-cc+1.6, 40,p1)                       # 2nd vertical line
                        pdf.line(110,dd-cc+1.6, 110,p1)                       # 1st vertical line
                        pdf.line(140,dd-cc+1.6, 140,p1)                       # 2nd vertical line
                        pdf.line(170,dd-cc+1.6, 170,p1)                       # 1st vertical line
                        pdf.line(195,dd-cc+1.6, 195,p1)                       # 2nd vertical line


                        dd=p1
                        if line_flag == 'a1':
                            h = h + 4
                        elif line_flag == 'a2':
                            h = h + 6
                        elif line_flag == 'a3':
                            h = h + 6
                        m1=h

                        if j == 9:
                            pdf.add_page()
                            pdf.set_auto_page_break(auto=False)
                        cc=1
                m1=h

                if j==9:
                    h = 10  
                    dd=22             
                    for j in range(10,max_List1):
                        if total_date_list[i][j] != 'Test':
                            pdf.set_line_width(0.01)

                            pdf.ln(1)
                            pdf.cell(10)
                            pdf.cell(10,h,txt = str(total_date_list[i][j]))

                            pdf.cell(10)
                            pdf.cell(10,h,txt = str(total_desc0[i][j]))

                            pdf.cell(80)
                            pdf.cell(10,h,txt = str(total_debit[i][j]))
                            pdf.cell(20)
                            pdf.cell(10,h,txt = str(total_credit[i][j]))

                            pdf.cell(8)
                            pdf.cell(10,h,txt = str(total_bal[i][j]))    
                            if total_desc1[i][j]!='desc_TEST':
                                pdf.ln(1)
                                pdf.cell(30)
                                h=h+4
                                pdf.set_font('Arial','',8)
                                pdf.cell(20,h,txt =  str(total_desc1[i][j]))
                                cc=cc+1  
                            if total_desc2[i][j]!='desc_TEST':                                                
                                pdf.ln(1)                                              
                                pdf.cell(30)
                                h=h+4                                          # 31,33,35,37,39,41
                                pdf.cell(10,h,txt =  str(total_desc2[i][j]))   #  27,29,31,33,35                         
                                cc=cc+1  

                            if total_desc3[i][j]!='desc_TEST':
                                pdf.ln(1)        
                                pdf.cell(30)
                                h=h+4
                                pdf.cell(10,h,txt =  str(total_desc3[i][j]))   
                                cc=cc+1  
                            pdf.ln(2)
                            p1=h-j*2+27
                            pdf.line(15,p1,195,p1)
                            pdf.line(15,dd-cc-5, 15,p1)                       # 1st vertical line
                            pdf.line(40,dd-cc-5, 40,p1)                       # 2nd vertical line
                            pdf.line(110,dd-cc-5, 110,p1)                       # 1st vertical line
                            pdf.line(140,dd-cc-5, 140,p1)                       # 2nd vertical line
                            pdf.line(170,dd-cc-5, 170,p1)                       # 1st vertical line
                            pdf.line(195,dd-cc-5, 195,p1)                       # 2nd vertical line
                            dd=p1
                            h=h+6
                            m2=h
                            flag11=True
        
                    

                m2=h
                # print(m1,m2,'00000000')
                if msg_total_debit[i] != 'Test' and m1>100 and m2<100 and flag11==False: # adds msg for transactions <9
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m1-45,15,m1-10)                             # 1st vertical line of total table  
                    pdf.line(195,m1-45,195,m1-10)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m1+20,txt = 'TOTAL DEBIT')

                    pdf.cell(30)
                    pdf.cell(20,m1+20,txt = str(msg_total_debit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m1+25,txt = 'TOTAL CREDIT')
                    
                    pdf.cell(30)
                    pdf.cell(20,m1+25,txt = str(msg_total_credit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m1+30,txt = 'MONTHLY AVERAGE')
                    
                    # pdf.cell(30)
                    # pdf.cell(40,h+30,txt = str(monthly_avg[i][j]))

                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m1-12 , w = 180 , h = 4, style = 'DF')      
                    pdf.ln(1)
                    pdf.set_font('Arial','',7.2)
                    pdf.cell(4)
                    pdf.cell(10,m1+66,txt ='Sekiranya anda mendapati sebarang perbezaan, sila maklumkan kepada pihak Bank di dalam tempoh 14 hari daripada tarikh penyata ini. Jika tiada perbezaan')   
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+69 , txt = 'penyata ini akan dianggap betul. ')
                    pdf.set_font('Arial','I',7.1)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+73,txt= 'If you note any discrepancies, please advise the Bank within 14 days from the date of this statement, otherwise this account statement is considered to be correct. ')
                    pdf.set_font('Arial','',7.2)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+77,txt = 'Untuk pertanyaan, ajukan kepada / For enquiries, please channel to: ')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+81,txt = 'Jabatan Khidmat Pelanggan (Customer Care Department), Tingkat 17, Menara Bank Islam, No 22, Jalan Perak, 50450 Kuala Lumpur')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+85,txt = 'Tel: 03-26 900 900 / Faks: 03-2782 1337. Emel / Email: contactcenter@bankislam.com.my')

                if msg_total_debit[i] == 'Test' and m1>100 and m2<100 and flag11==False:
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m1-50,15,m1-26)                             # 1st vertical line of total table  
                    pdf.line(195,m1-50,195,m1-26)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m1+10,txt = 'NO MESSAGE')


                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m1-30 , w = 180 , h = 4, style = 'DF')      

                if msg_total_debit[i] == 'Test' and m2<100 and flag11==True:
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m2+20,15,m2-5)                             # 1st vertical line of total table  
                    pdf.line(195,m2+20,195,m2-5)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m2+10,txt = 'NO MESSAGE')


                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m2+20 , w = 180 , h = 4, style = 'DF')      

                if msg_total_debit[i] != 'Test' and m2<100 and flag11==True: # adds msg for transactions >9
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m2-5,15,m2+20)                             # 1st vertical line of total table  
                    pdf.line(195,m2-5,195,m2+20)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m2,txt = 'TOTAL DEBIT')

                    pdf.cell(30)
                    pdf.cell(20,m2,txt = str(msg_total_debit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m2+5,txt = 'TOTAL CREDIT')
                    
                    pdf.cell(30)
                    pdf.cell(20,m2+5,txt = str(msg_total_credit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m2+10,txt = 'MONTHLY AVERAGE')
                    
                    # pdf.cell(30)
                    # pdf.cell(40,h+30,txt = str(monthly_avg[i][j]))

                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m2+20 , w = 180 , h = 4, style = 'DF')      
                    pdf.ln(1)
                    pdf.set_font('Arial','',7.2)
                    pdf.cell(4)
                    pdf.cell(10,m2+60,txt ='Sekiranya anda mendapati sebarang perbezaan, sila maklumkan kepada pihak Bank di dalam tempoh 14 hari daripada tarikh penyata ini. Jika tiada perbezaan')   
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+64 , txt = 'penyata ini akan dianggap betul. ')
                    pdf.set_font('Arial','I',7.1)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+68.8,txt= 'If you note any discrepancies, please advise the Bank within 14 days from the date of this statement, otherwise this account statement is considered to be correct. ')
                    pdf.set_font('Arial','',7.2)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+73.8,txt = 'Untuk pertanyaan, ajukan kepada / For enquiries, please channel to: ')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+78.8,txt = 'Jabatan Khidmat Pelanggan (Customer Care Department), Tingkat 17, Menara Bank Islam, No 22, Jalan Perak, 50450 Kuala Lumpur')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+84,txt = 'Tel: 03-26 900 900 / Faks: 03-2782 1337. Emel / Email: contactcenter@bankislam.com.my')



            if 'TEST' not in bal_bf[i]:
                pdf.ln(1)
                pdf.set_fill_color(r=211,g=211,b=211)
                pdf.set_line_width(0.01)
                pdf.rect(x = 15 , y = 100 , w = 180 , h = 15, style = 'DF')

                pdf.set_line_width(0.5)
                pdf.line(40,100, 40, 115)                      # first  | line
                pdf.line(110,100, 110, 115)                    # second | line
                pdf.line(140,100, 140, 115)                    # third | line
                pdf.line(170,100,170,115)                      # fourth | line

                #-------------------------------------INSERTING 2ND PAGE TABLE COLUMN NAMES---------------------------------

                pdf.ln(1)
                pdf.set_font('Arial', 'B', 9)
                pdf.cell(10)
                pdf.cell(30,134,txt = 'TARIKH')
                pdf.cell(6)
                pdf.cell(30,134,txt = 'KETERANGAN')
                pdf.cell(30)
                pdf.cell(30,134,txt = 'DEBIT')
                pdf.cell(4)
                pdf.cell(25,134,txt = 'KREDIT')
                pdf.cell(1)
                pdf.cell(25,134,txt = 'BAKI')


                pdf.ln(4)

                pdf.set_font('Arial', 'I', 9)
                pdf.cell(10)
                pdf.cell(30,136,txt = 'DATE')
                pdf.cell(6)
                pdf.cell(30,136,txt = 'DESCRIPTION')
                pdf.cell(30)
                pdf.cell(25,136,txt = 'DEBIT')
                pdf.cell(8)
                pdf.cell(25,136,txt = 'CREDIT')
                pdf.cell(1)
                pdf.cell(25,136,txt = 'BALANCE')

                pdf.ln(4)

                pdf.set_font('Arial', '', 9)
                pdf.cell(10)
                pdf.cell(30,138,txt = '')
                pdf.cell(6)
                pdf.cell(30,138,txt = '')
                pdf.cell(35)
                pdf.cell(25,138,txt = 'RM')
                pdf.cell(5)
                pdf.cell(25,138,txt = 'RM')
                pdf.cell(1)
                pdf.cell(25,138,txt = 'RM')

            #     #--------------------------------------------INSERTING 1ST TABLE DATA OF 1ST PAGE-----------------
                h = 147
                p2=h
                cc=1
                dd=115

                m1=h
                m2=h
                flag11=False
                for j in range(0,10):
                    if total_date_list[i][j] != 'Test':
                        pdf.set_line_width(0.01)

                        pdf.ln(1)
                        pdf.cell(10)
                        pdf.cell(10,h,txt = str(total_date_list[i][j]))

                        pdf.cell(10)
                        pdf.cell(10,h,txt = str(total_desc0[i][j]))

                        pdf.cell(80)
                        pdf.cell(10,h,txt = str(total_debit[i][j]))
                        pdf.cell(20)
                        pdf.cell(10,h,txt = str(total_credit[i][j]))

                        pdf.cell(8)
                        pdf.cell(10,h,txt = str(total_bal[i][j]))    
                        if total_desc1[i][j]!='desc_TEST':
                            pdf.ln(1)
                            pdf.cell(30)
                            h=h+4
                            pdf.set_font('Arial','B',8)
                            pdf.cell(20,h,txt =  str(total_desc1[i][j]))
                            cc=cc+1  
                        if total_desc2[i][j]!='desc_TEST':                                                
                            pdf.ln(1)                                              
                            pdf.cell(30)
                            h=h+4                                          # 31,33,35,37,39,41
                            pdf.cell(10,h,txt =  str(total_desc2[i][j]))   #  27,29,31,33,35                         
                            cc=cc+1  

                        if total_desc3[i][j]!='desc_TEST':
                            pdf.ln(1)        
                            pdf.cell(30)
                            h=h+2
                            pdf.cell(10,h,txt =  str(total_desc3[i][j]))   
                            cc=cc+1  
                        
                        pdf.ln(2)
                        p1=h-27-j*2
                        pdf.line(15,p1,195,p1)
                        # print(p1,h,cc,'-----------')
                        pdf.line(15,dd-cc+1.6, 15,p1)                       # 1st vertical line
                        pdf.line(40,dd-cc+1.6, 40,p1)                       # 2nd vertical line
                        pdf.line(110,dd-cc+1.6, 110,p1)                       # 1st vertical line
                        pdf.line(140,dd-cc+1.6, 140,p1)                       # 2nd vertical line
                        pdf.line(170,dd-cc+1.6, 170,p1)                       # 1st vertical line
                        pdf.line(195,dd-cc+1.6, 195,p1)                       # 2nd vertical line

                        dd=p1
                        h=h+6
                        m1=h
                        if j == 9:
                            pdf.add_page()
                            pdf.set_auto_page_break(auto=False)
                        cc=1
                m1=h

                if j==9:
                    h = 10  
                    dd=22             
                    for j in range(10,max_List1):
                        if total_date_list[i][j] != 'Test':
                            pdf.set_line_width(0.01)

                            pdf.ln(1)
                            pdf.cell(10)
                            pdf.cell(10,h,txt = str(total_date_list[i][j]))

                            pdf.cell(10)
                            pdf.cell(10,h,txt = str(total_desc0[i][j]))

                            pdf.cell(80)
                            pdf.cell(10,h,txt = str(total_debit[i][j]))
                            pdf.cell(20)
                            pdf.cell(10,h,txt = str(total_credit[i][j]))

                            pdf.cell(8)
                            pdf.cell(10,h,txt = str(total_bal[i][j]))    
                            if total_desc1[i][j]!='desc_TEST':
                                pdf.ln(1)
                                pdf.cell(30)
                                h=h+4
                                pdf.set_font('Arial','',8)
                                pdf.cell(20,h,txt =  str(total_desc1[i][j]))
                                cc=cc+1  
                            if total_desc2[i][j]!='desc_TEST':                                                
                                pdf.ln(1)                                              
                                pdf.cell(30)
                                h=h+4                                          # 31,33,35,37,39,41
                                pdf.cell(10,h,txt =  str(total_desc2[i][j]))   #  27,29,31,33,35                         
                                cc=cc+1  

                            if total_desc3[i][j]!='desc_TEST':
                                pdf.ln(1)        
                                pdf.cell(30)
                                h=h+4
                                pdf.cell(10,h,txt =  str(total_desc3[i][j]))   
                                cc=cc+1  
                            pdf.ln(2)
                            p1=h-j*2+27
                            pdf.line(15,p1,195,p1)
                            pdf.line(15,dd-cc-5, 15,p1)                       # 1st vertical line
                            pdf.line(40,dd-cc-5, 40,p1)                       # 2nd vertical line
                            pdf.line(110,dd-cc-5, 110,p1)                       # 1st vertical line
                            pdf.line(140,dd-cc-5, 140,p1)                       # 2nd vertical line
                            pdf.line(170,dd-cc-5, 170,p1)                       # 1st vertical line
                            pdf.line(195,dd-cc-5, 195,p1)                       # 2nd vertical line
                            dd=p1
                            h=h+6
                            m2=h
                            flag11=True
        
                    

                m2=h
                # print(m1,m2,'00000000')
                if msg_total_debit[i] != 'Test' and m1>100 and m2<100 and flag11==False: # adds msg for transactions <9
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m1-45,15,m1-10)                             # 1st vertical line of total table  
                    pdf.line(195,m1-45,195,m1-10)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m1+20,txt = 'TOTAL DEBIT')

                    pdf.cell(30)
                    pdf.cell(20,m1+20,txt = str(msg_total_debit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m1+25,txt = 'TOTAL CREDIT')
                    
                    pdf.cell(30)
                    pdf.cell(20,m1+25,txt = str(msg_total_credit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m1+30,txt = 'MONTHLY AVERAGE')
                    
                    # pdf.cell(30)
                    # pdf.cell(40,h+30,txt = str(monthly_avg[i][j]))

                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m1-12 , w = 180 , h = 4, style = 'DF')      
                    pdf.ln(1)
                    pdf.set_font('Arial','',7.2)
                    pdf.cell(4)
                    pdf.cell(10,m1+66,txt ='Sekiranya anda mendapati sebarang perbezaan, sila maklumkan kepada pihak Bank di dalam tempoh 14 hari daripada tarikh penyata ini. Jika tiada perbezaan')   
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+69 , txt = 'penyata ini akan dianggap betul. ')
                    pdf.set_font('Arial','I',7.1)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+73,txt= 'If you note any discrepancies, please advise the Bank within 14 days from the date of this statement, otherwise this account statement is considered to be correct. ')
                    pdf.set_font('Arial','',7.2)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+77,txt = 'Untuk pertanyaan, ajukan kepada / For enquiries, please channel to: ')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+81,txt = 'Jabatan Khidmat Pelanggan (Customer Care Department), Tingkat 17, Menara Bank Islam, No 22, Jalan Perak, 50450 Kuala Lumpur')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+85,txt = 'Tel: 03-26 900 900 / Faks: 03-2782 1337. Emel / Email: contactcenter@bankislam.com.my')

                if msg_total_debit[i] == 'Test' and m1>100 and m2<100 and flag11==False:
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m1-50,15,m1-26)                             # 1st vertical line of total table  
                    pdf.line(195,m1-50,195,m1-26)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m1+10,txt = 'NO MESSAGE')


                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m1-30 , w = 180 , h = 4, style = 'DF')      

                if msg_total_debit[i] == 'Test' and m2<100 and flag11==True:
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m2+20,15,m2-5)                             # 1st vertical line of total table  
                    pdf.line(195,m2+20,195,m2-5)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m2+10,txt = 'NO MESSAGE')


                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m2+20 , w = 180 , h = 4, style = 'DF')      

                if msg_total_debit[i] != 'Test' and m2<100 and flag11==True: # adds msg for transactions >9
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m2-5,15,m2+20)                             # 1st vertical line of total table  
                    pdf.line(195,m2-5,195,m2+20)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m2,txt = 'TOTAL DEBIT')

                    pdf.cell(30)
                    pdf.cell(20,m2,txt = str(msg_total_debit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m2+5,txt = 'TOTAL CREDIT')
                    
                    pdf.cell(30)
                    pdf.cell(20,m2+5,txt = str(msg_total_credit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m2+10,txt = 'MONTHLY AVERAGE')
                    
                    # pdf.cell(30)
                    # pdf.cell(40,h+30,txt = str(monthly_avg[i][j]))

                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m2+20 , w = 180 , h = 4, style = 'DF')      
                    pdf.ln(1)
                    pdf.set_font('Arial','',7.2)
                    pdf.cell(4)
                    pdf.cell(10,m2+60,txt ='Sekiranya anda mendapati sebarang perbezaan, sila maklumkan kepada pihak Bank di dalam tempoh 14 hari daripada tarikh penyata ini. Jika tiada perbezaan')   
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+64 , txt = 'penyata ini akan dianggap betul. ')
                    pdf.set_font('Arial','I',7.1)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+68.8,txt= 'If you note any discrepancies, please advise the Bank within 14 days from the date of this statement, otherwise this account statement is considered to be correct. ')
                    pdf.set_font('Arial','',7.2)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+73.8,txt = 'Untuk pertanyaan, ajukan kepada / For enquiries, please channel to: ')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+78.8,txt = 'Jabatan Khidmat Pelanggan (Customer Care Department), Tingkat 17, Menara Bank Islam, No 22, Jalan Perak, 50450 Kuala Lumpur')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+84,txt = 'Tel: 03-26 900 900 / Faks: 03-2782 1337. Emel / Email: contactcenter@bankislam.com.my')




    
                    



    


    
    #---------------------------filenames -----------------------------
    kc1 = 1
    pdf_merger = PdfFileMerger()
    date1 = datetime.now()
    d = date1.strftime('%d')
    m = date1.strftime('%m')
    y = date1.strftime('%y')
    y = y[2:4]

    if m == '01':
        month = 'JAN'
    if m == '02':
        month = 'FEB'
    if m == '03':
        month = 'MAR'
    if m == '04':
        month = 'APR'
    if m == '05':
        month = 'MAY'
    if m == '06':
        month = 'JUN'
    if m == '07':
        month = 'JUL'
    if m == '08':
        month = 'AUG'
    if m == '09':
        month = 'SEP'
    if m == '10':
        month = 'OCT'
    if m == '11':
        month = 'NOV'
    if m == '12':
        month = 'DEC'

    filename = os.path.abspath(r"%s\C-%s%s%s_0000%s.pdf"%(kk2,d,month,y,kc1))
    f = filename    
    print(Total_email_accounts,'NON EMAIL ACCOUNTS PDF CREATED')
    pdf.output(f)    
    kc1 +=  1  

######################################################################################################
    #-----------------------------function with emailids--------------------------
######################################################################################################
    c=1
    c = c + 1
    for i in range(0,Total_email_accounts):
        if account_no[i] in email_account_no: 
            pdf = FPDF()
            pdf.add_page()
            pdf.image('E:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Left_logo.jpg',10,15,60)
            pdf.image('E:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Right_logo.jpg',160,15,33)
            pdf.set_auto_page_break(auto=False)

            pdf.set_font('Arial', '', 9)
            pdf.cell(4)
            pdf.cell(10,70,txt = 'TUAN SULAIMAN AKHLAKEN BIN SADIQ SEGARAG.')

            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,72,txt = 'A')

            pdf.set_font('Arial','B',9)
            pdf.cell(90)
            pdf.cell(30,70,txt = 'TARIKH PENYATA')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,74,txt = 'Unit A-11-12')

            pdf.set_font('Arial','I',9)
            pdf.cell(90)
            pdf.cell(30,74,txt = 'STATEMENT DATE')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,76,txt = 'Hermington Condo,')

            pdf.set_font('Arial','B',9)
            pdf.cell(90)
            pdf.cell(30,78,txt = 'HALAMAN')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,78,txt = 'No. 3, Jalan Indrahana 3,')

            pdf.set_font('Arial','I',9)
            pdf.cell(90)
            pdf.cell(30,82,txt = 'Page')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,80,txt = 'Taman Indrahana')

            pdf.set_font('Arial','B',9)
            pdf.cell(90)
            pdf.cell(10,86,txt = 'NOMBOR AKAUN')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,82,txt = 'Jalan Kuchai Lama')

            pdf.set_font('Arial','I',9)
            pdf.cell(90)
            pdf.cell(10,90,txt = 'ACCOUNT NO  ')

            pdf.set_font('Arial','',9)
            pdf.ln(2)
            pdf.cell(4)
            pdf.cell(10,84,txt = '58200 Kuala Lumpur')

            pdf.set_font('Arial','B',9)
            pdf.cell(90)
            pdf.cell(10,94,txt = 'CAWANGAN')

            pdf.set_font('Arial','I',9)
            pdf.cell(-10)
            pdf.cell(10,102,txt = 'BRANCH ')

            #-----------------------------------------INSERTING VALUES OF NAME,ADDRESS,ACC,BRANCH ON 2 PAGE-----------

            pdf.set_font('Arial', 'B', 9)
            pdf.cell(50)
            pdf.cell(10,55,txt = '30/09/25')

            pdf.ln(2)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(160)
            pdf.cell(10,66,txt = 'Page 2 of 3')

            pdf.ln(2)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(152)
            pdf.cell(10,78,txt = str(account_no[i]))

            pdf.ln(2)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(142)
            pdf.cell(10,90,txt = 'MENARA BANK ISLAM')

            #-----------------------INSERTING ACCOUNT STATEMENT AND SAVING ACCOUNT ON 2 PAGE----------------------
            pdf.ln(1)
            pdf.set_font('Arial','B',9)
            pdf.cell(4)
            pdf.cell(10,100,txt = 'PENYATA AKAUN / ')

            pdf.set_font('Arial','BI',9)
            pdf.cell(20)
            pdf.cell(10,100,txt = 'ACCOUNT STATEMENT ')

            pdf.ln(1)
            pdf.set_font('Arial','',9)
            pdf.cell(4)
            pdf.cell(10,106,txt = 'AKAUN SIMPANAN / ')

            pdf.set_font('Arial','',9)
            pdf.cell(20)
            pdf.cell(10,106,txt = ' SAVINGS ACCOUNT')

            pdf.ln(1)
            pdf.set_font('Arial','',8)
            pdf.cell(4)
            pdf.cell(10,112,txt = '(Dilindungi oleh PIDM setakat RM250,000 bagi setiap pendeposit. /')

            pdf.set_font('Arial','I',8)
            pdf.ln(1)
            pdf.cell(5)
            pdf.cell(10,118,txt = 'Protected by PIDM up to RM250,000 for each depositor.)')

                #-----------------------------------INSERTING 2ND PAGE TABLE-------------------------------------

            if 'TEST' in bal_bf[i]:
                pdf.ln(1)
                pdf.set_fill_color(r=211,g=211,b=211)
                pdf.set_line_width(0.01)
                pdf.rect(x = 15 , y = 100 , w = 180 , h = 15, style = 'DF')

                pdf.set_line_width(0.5)
                pdf.line(40,100, 40, 115)                      # first  | line
                pdf.line(110,100, 110, 115)                    # second | line
                pdf.line(140,100, 140, 115)                    # third | line
                pdf.line(170,100,170,115)                      # fourth | line

                #-------------------------------------INSERTING 2ND PAGE TABLE COLUMN NAMES---------------------------------

                pdf.ln(1)
                pdf.set_font('Arial', 'B', 9)
                pdf.cell(10)
                pdf.cell(30,134,txt = 'TARIKH')
                pdf.cell(6)
                pdf.cell(30,134,txt = 'KETERANGAN')
                pdf.cell(30)
                pdf.cell(30,134,txt = 'DEBIT')
                pdf.cell(4)
                pdf.cell(25,134,txt = 'KREDIT')
                pdf.cell(1)
                pdf.cell(25,134,txt = 'BAKI')


                pdf.ln(4)

                pdf.set_font('Arial', 'I', 9)
                pdf.cell(10)
                pdf.cell(30,136,txt = 'DATE')
                pdf.cell(6)
                pdf.cell(30,136,txt = 'DESCRIPTION')
                pdf.cell(30)
                pdf.cell(25,136,txt = 'DEBIT')
                pdf.cell(8)
                pdf.cell(25,136,txt = 'CREDIT')
                pdf.cell(1)
                pdf.cell(25,136,txt = 'BALANCE')

                pdf.ln(4)

                pdf.set_font('Arial', 'B', 9)
                pdf.cell(10)
                pdf.cell(30,138,txt = '')
                pdf.cell(6)
                pdf.cell(30,138,txt = '')
                pdf.cell(35)
                pdf.cell(25,138,txt = 'RM')
                pdf.cell(5)
                pdf.cell(25,138,txt = 'RM')
                pdf.cell(1)
                pdf.cell(25,138,txt = 'RM')

            #     #--------------------------------------------INSERTING 1ST TABLE DATA OF 1ST PAGE-----------------
                h = 147
                p2=h
                cc=1
                dd=115

                m1=h
                m2=h
                flag11=False
                for j in range(0,10):
                    if total_date_list[i][j] != 'Test':
                        pdf.set_line_width(0.01)

                        pdf.ln(1)
                        pdf.cell(10)
                        pdf.cell(10,h,txt = str(total_date_list[i][j]))

                        pdf.cell(10)
                        pdf.cell(10,h,txt = str(total_desc0[i][j]))

                        pdf.cell(80)
                        pdf.cell(10,h,txt = str(total_debit[i][j]))
                        pdf.cell(20)
                        pdf.cell(10,h,txt = str(total_credit[i][j]))

                        pdf.cell(8)
                        pdf.cell(10,h,txt = str(total_bal[i][j]))    
                        if total_desc1[i][j]!='desc_TEST':
                            pdf.ln(1)
                            pdf.cell(30)
                            h=h+4
                            pdf.set_font('Arial','B',8)
                            pdf.cell(20,h,txt =  str(total_desc1[i][j]))
                            cc=cc+1  
                        if total_desc2[i][j]!='desc_TEST':                                                
                            pdf.ln(1)                                              
                            pdf.cell(30)
                            h=h+4                                          # 31,33,35,37,39,41
                            pdf.cell(10,h,txt =  str(total_desc2[i][j]))   #  27,29,31,33,35                         
                            cc=cc+1  

                        if total_desc3[i][j]!='desc_TEST':
                            pdf.ln(1)        
                            pdf.cell(30)
                            h=h+2
                            pdf.cell(10,h,txt =  str(total_desc3[i][j]))   
                            cc=cc+1  
                        
                        pdf.ln(2)
                        if total_desc1[i][j]=='desc_TEST':
                            p1=h-25-j*2+2*j
                        else:
                            p1=h-27-j*2
                        # p1=h-27-j*2
                        pdf.line(15,p1,195,p1)
                        # print(p1,h,cc,'-----------')
                        pdf.line(15,dd-cc+1.6, 15,p1)                       # 1st vertical line
                        pdf.line(40,dd-cc+1.6, 40,p1)                       # 2nd vertical line
                        pdf.line(110,dd-cc+1.6, 110,p1)                       # 1st vertical line
                        pdf.line(140,dd-cc+1.6, 140,p1)                       # 2nd vertical line
                        pdf.line(170,dd-cc+1.6, 170,p1)                       # 1st vertical line
                        pdf.line(195,dd-cc+1.6, 195,p1)                       # 2nd vertical line

                        dd=p1
                        h=h+6
                        m1=h
                        if j == 9:
                            pdf.add_page()
                            pdf.set_auto_page_break(auto=False)
                        cc=1
                m1=h

                if j==9:
                    h = 10  
                    dd=22             
                    for j in range(10,max_List1):
                        if total_date_list[i][j] != 'Test':
                            pdf.set_line_width(0.01)

                            pdf.ln(1)
                            pdf.cell(10)
                            pdf.cell(10,h,txt = str(total_date_list[i][j]))

                            pdf.cell(10)
                            pdf.cell(10,h,txt = str(total_desc0[i][j]))

                            pdf.cell(80)
                            pdf.cell(10,h,txt = str(total_debit[i][j]))
                            pdf.cell(20)
                            pdf.cell(10,h,txt = str(total_credit[i][j]))

                            pdf.cell(8)
                            pdf.cell(10,h,txt = str(total_bal[i][j]))    
                            if total_desc1[i][j]!='desc_TEST':
                                pdf.ln(1)
                                pdf.cell(30)
                                h=h+4
                                pdf.set_font('Arial','',8)
                                pdf.cell(20,h,txt =  str(total_desc1[i][j]))
                                cc=cc+1  
                            if total_desc2[i][j]!='desc_TEST':                                                
                                pdf.ln(1)                                              
                                pdf.cell(30)
                                h=h+4                                          # 31,33,35,37,39,41
                                pdf.cell(10,h,txt =  str(total_desc2[i][j]))   #  27,29,31,33,35                         
                                cc=cc+1  

                            if total_desc3[i][j] =='desc_TEST':
                                pdf.ln(1)        
                                pdf.cell(30)
                                h=h+4
                                pdf.cell(10,h,txt =  str(total_desc3[i][j]))   
                                cc=cc+1  
                            pdf.ln(2)
                            # if total_desc1[i][j] !='desc_TEST':
                            #     p1=h-25-j*2+2*j
                            # else:
                            #     p1=h-25-j*2
                            p1=h-j*2+31
                            pdf.line(15,p1,195,p1)                             # horizontal line
                            pdf.line(15,dd-cc-5, 15,p1)                       # 1st vertical line
                            pdf.line(40,dd-cc-5, 40,p1)                       # 2nd vertical line
                            pdf.line(110,dd-cc-5, 110,p1)                       # 3st vertical line
                            pdf.line(140,dd-cc-5, 140,p1)                       # 4nd vertical line
                            pdf.line(170,dd-cc-5, 170,p1)                       # 5st vertical line
                            pdf.line(195,dd-cc-5, 195,p1)                       # 6nd vertical line
                            dd=p1
                            h=h+6
                            m2=h
                            flag11=True
        
                    

                m2=h
                # print(m1,m2,'00000000')
                if msg_total_debit[i] != 'Test' and m1>100 and m2<100 and flag11==False: # adds msg for transactions <9
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m1-45,15,m1-10)                             # 1st vertical line of total table  
                    pdf.line(195,m1-45,195,m1-10)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m1+20,txt = 'TOTAL DEBIT')

                    pdf.cell(30)
                    pdf.cell(20,m1+20,txt = str(msg_total_debit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m1+25,txt = 'TOTAL CREDIT')
                    
                    pdf.cell(30)
                    pdf.cell(20,m1+25,txt = str(msg_total_credit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m1+30,txt = 'MONTHLY AVERAGE')
                    
                    # pdf.cell(30)
                    # pdf.cell(40,h+30,txt = str(monthly_avg[i][j]))

                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m1-12 , w = 180 , h = 4, style = 'DF')      
                    pdf.ln(1)
                    pdf.set_font('Arial','',7.2)
                    pdf.cell(4)
                    pdf.cell(10,m1+66,txt ='Sekiranya anda mendapati sebarang perbezaan, sila maklumkan kepada pihak Bank di dalam tempoh 14 hari daripada tarikh penyata ini. Jika tiada perbezaan')   
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+69 , txt = 'penyata ini akan dianggap betul. ')
                    pdf.set_font('Arial','I',7.1)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+73,txt= 'If you note any discrepancies, please advise the Bank within 14 days from the date of this statement, otherwise this account statement is considered to be correct. ')
                    pdf.set_font('Arial','',7.2)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+77,txt = 'Untuk pertanyaan, ajukan kepada / For enquiries, please channel to: ')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+81,txt = 'Jabatan Khidmat Pelanggan (Customer Care Department), Tingkat 17, Menara Bank Islam, No 22, Jalan Perak, 50450 Kuala Lumpur')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m1+85,txt = 'Tel: 03-26 900 900 / Faks: 03-2782 1337. Emel / Email: contactcenter@bankislam.com.my')

                if msg_total_debit[i] == 'Test' and m1>100 and m2<100 and flag11==False:
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m1-50,15,m1-26)                             # 1st vertical line of total table  
                    pdf.line(195,m1-50,195,m1-26)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m1+10,txt = 'NO MESSAGE')


                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m1-30 , w = 180 , h = 4, style = 'DF')      

                if msg_total_debit[i] == 'Test' and m2<100 and flag11==True:
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m2+20,15,m2-5)                             # 1st vertical line of total table  
                    pdf.line(195,m2+20,195,m2-5)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m2+10,txt = 'NO MESSAGE')


                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m2+20 , w = 180 , h = 4, style = 'DF')      

                if msg_total_debit[i] != 'Test' and m2<100 and flag11==True: # adds msg for transactions >9
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m2-5,15,m2+20)                             # 1st vertical line of total table  
                    pdf.line(195,m2-5,195,m2+20)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m2,txt = 'TOTAL DEBIT')

                    pdf.cell(30)
                    pdf.cell(20,m2,txt = str(msg_total_debit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m2+5,txt = 'TOTAL CREDIT')
                    
                    pdf.cell(30)
                    pdf.cell(20,m2+5,txt = str(msg_total_credit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m2+10,txt = 'MONTHLY AVERAGE')
                    
                    # pdf.cell(30)
                    # pdf.cell(40,h+30,txt = str(monthly_avg[i][j]))

                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m2+20 , w = 180 , h = 4, style = 'DF')      
                    pdf.ln(1)
                    pdf.set_font('Arial','',7.2)
                    pdf.cell(4)
                    pdf.cell(10,m2+60,txt ='Sekiranya anda mendapati sebarang perbezaan, sila maklumkan kepada pihak Bank di dalam tempoh 14 hari daripada tarikh penyata ini. Jika tiada perbezaan')   
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+64 , txt = 'penyata ini akan dianggap betul. ')
                    pdf.set_font('Arial','I',7.1)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+68.8,txt= 'If you note any discrepancies, please advise the Bank within 14 days from the date of this statement, otherwise this account statement is considered to be correct. ')
                    pdf.set_font('Arial','',7.2)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+73.8,txt = 'Untuk pertanyaan, ajukan kepada / For enquiries, please channel to: ')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+78.8,txt = 'Jabatan Khidmat Pelanggan (Customer Care Department), Tingkat 17, Menara Bank Islam, No 22, Jalan Perak, 50450 Kuala Lumpur')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m2+84,txt = 'Tel: 03-26 900 900 / Faks: 03-2782 1337. Emel / Email: contactcenter@bankislam.com.my')



            if 'TEST' not in bal_bf[i]:
                pdf.ln(1)
                pdf.set_fill_color(r=211,g=211,b=211)
                pdf.set_line_width(0.01)
                pdf.rect(x = 15 , y = 100 , w = 180 , h = 15, style = 'DF')

                pdf.set_line_width(0.5)
                pdf.line(40,100, 40, 115)                      # first  | line
                pdf.line(110,100, 110, 115)                    # second | line
                pdf.line(140,100, 140, 115)                    # third | line
                pdf.line(170,100,170,115)                      # fourth | line

                #-------------------------------------INSERTING 2ND PAGE TABLE COLUMN NAMES---------------------------------

                pdf.ln(1)
                pdf.set_font('Arial', 'B', 9)
                pdf.cell(10)
                pdf.cell(30,134,txt = 'TARIKH')
                pdf.cell(6)
                pdf.cell(30,134,txt = 'KETERANGAN')
                pdf.cell(30)
                pdf.cell(30,134,txt = 'DEBIT')
                pdf.cell(4)
                pdf.cell(25,134,txt = 'KREDIT')
                pdf.cell(1)
                pdf.cell(25,134,txt = 'BAKI')


                pdf.ln(4)

                pdf.set_font('Arial', 'I', 9)
                pdf.cell(10)
                pdf.cell(30,136,txt = 'DATE')
                pdf.cell(6)
                pdf.cell(30,136,txt = 'DESCRIPTION')
                pdf.cell(30)
                pdf.cell(25,136,txt = 'DEBIT')
                pdf.cell(8)
                pdf.cell(25,136,txt = 'CREDIT')
                pdf.cell(1)
                pdf.cell(25,136,txt = 'BALANCE')

                pdf.ln(4)

                pdf.set_font('Arial', '', 9)
                pdf.cell(10)
                pdf.cell(30,138,txt = '')
                pdf.cell(6)
                pdf.cell(30,138,txt = '')
                pdf.cell(35)
                pdf.cell(25,138,txt = 'RM')
                pdf.cell(5)
                pdf.cell(25,138,txt = 'RM')
                pdf.cell(1)
                pdf.cell(25,138,txt = 'RM')

            #     #--------------------------------------------INSERTING 1ST TABLE DATA OF 1ST PAGE-----------------
                h = 150
                p2=h
                cc=1
                dd=114
                pdf.set_line_width(0.01)
                pdf.ln(1)
                pdf.cell(10)
                pdf.cell(10,145,txt = "BAL B/F")
                pdf.cell(120)
                pdf.cell(10,145,txt = str(bal_bf[i]))
                pdf.line(15,119,195,119)
                pdf.ln(2)

                a=1
                flag12=False
                m4=h
                m3=h
                for j in range(0,10):
                    if total_date_list[i][j] != 'Test':                  
                        pdf.cell(10)
                        pdf.cell(10,h,txt = str(total_date_list[i][j]))

                        pdf.cell(10)
                        pdf.cell(10,h,txt = str(total_desc0[i][j]))

                        pdf.cell(80)
                        pdf.cell(10,h,txt = str(total_debit[i][j]))
                        pdf.cell(20)
                        pdf.cell(10,h,txt = str(total_credit[i][j]))

                        pdf.cell(8)
                        pdf.cell(10,h,txt = str(total_bal[i][j]))    
                        if total_desc1[i][j]!='desc_TEST':
                            pdf.ln(1)
                            pdf.cell(30)
                            h=h+4
                            pdf.set_font('Arial','B',8)
                            pdf.cell(20,h,txt =  str(total_desc1[i][j]))
                            cc=cc+1  
                        if total_desc2[i][j]!='desc_TEST':                                                
                            pdf.ln(1)                                              
                            pdf.cell(30)
                            h=h+4                                          # 31,33,35,37,39,41
                            pdf.cell(10,h,txt =  str(total_desc2[i][j]))   #  27,29,31,33,35                         
                            cc=cc+1  

                        if total_desc3[i][j]!='desc_TEST':
                            pdf.ln(1)        
                            pdf.cell(30)
                            h=h+4
                            pdf.cell(10,h,txt =  str(total_desc3[i][j]))   
                            cc=cc+1  
                        pdf.ln(2.5)

                        if cc==1:
                            h=h+6   
                            p1=h-31-j*2          #100,98,96,94,92,90
                            pdf.line(15,p1,195,p1)
                            h=h+3
                            # print(cc,h,'#########')
                        if cc==2:
                            h=h+3
                            p1=h-30-j*2          #100,98,96,94,92,90
                            h=h+3
                            
                            pdf.line(15,p1,195,p1)
                            # print(cc,h,'**********')
                        if cc==3:
                            h=h+5
                            p1=h-33-j*2          #100,98,96,94,92,90
                            pdf.line(15,p1,195,p1)
                            # print(cc,h,'111111111')
                        if cc==4:
                            p1=h-28.5-j*2          #100,98,96,94,92,90
                            pdf.line(15,p1,195,p1)                        # print(cc,h,'22222222')
                            h=h+2.5
                        pdf.line(15,dd-cc+1.6, 15,p1)                        # 1st vertical line
                        pdf.line(40,dd-cc+1.6, 40,p1)                        # 2nd vertical line
                        pdf.line(110,dd-cc+1.6, 110,p1)                       # 3rd vertical line
                        pdf.line(140,dd-cc+1.6, 140,p1)                       # 4th vertical line
                        pdf.line(170,dd-cc+1.6, 170,p1)                       # 5th vertical line
                        pdf.line(195,dd-cc+1.6, 195,p1)                       # 6th vertical line
                        dd=p1
                        m3=h
                    
                        if j == 9:
                            pdf.add_page()
                            pdf.set_auto_page_break(auto=False)

                        cc=1    

                    # print(h,'kkkk')
                if j==9:
                    h = 10  
                    dd=22   
                    for j in range(10,max_List1):
                        if total_date_list[i][j] != 'Test':
                            pdf.set_line_width(0.01)

                            pdf.ln(1)
                            pdf.cell(10)
                            pdf.cell(10,h,txt = str(total_date_list[i][j]))

                            pdf.cell(10)
                            pdf.cell(10,h,txt = str(total_desc0[i][j]))

                            pdf.cell(80)
                            pdf.cell(10,h,txt = str(total_debit[i][j]))
                            pdf.cell(20)
                            pdf.cell(10,h,txt = str(total_credit[i][j]))

                            pdf.cell(8)
                            pdf.cell(10,h,txt = str(total_bal[i][j]))    
                            if total_desc1[i][j]!='desc_TEST':
                                pdf.ln(1)
                                pdf.cell(30)
                                h=h+4
                                pdf.set_font('Arial','',8)
                                pdf.cell(20,h,txt =  str(total_desc1[i][j]))
                                cc=cc+1  
                            if total_desc2[i][j]!='desc_TEST':                                                
                                pdf.ln(1)                                              
                                pdf.cell(30)
                                h=h+4                                          # 31,33,35,37,39,41
                                pdf.cell(10,h,txt =  str(total_desc2[i][j]))   #  27,29,31,33,35                         
                                cc=cc+1  

                            if total_desc3[i][j]!='desc_TEST':
                                pdf.ln(1)        
                                pdf.cell(30)
                                h=h+2
                                pdf.cell(10,h,txt =  str(total_desc3[i][j]))   
                                cc=cc+1  
                            pdf.ln(2)
                            p1=h-j*2+32
                            pdf.line(15,p1,195,p1)
                            pdf.line(15,dd-cc+1.6, 15,p1)                       # 1st vertical line
                            pdf.line(40,dd-cc+1.6, 40,p1)                       # 2nd vertical line
                            pdf.line(110,dd-cc+1.6, 110,p1)                       # 1st vertical line
                            pdf.line(140,dd-cc+1.6, 140,p1)                       # 2nd vertical line
                            pdf.line(170,dd-cc+1.6, 170,p1)                       # 1st vertical line
                            pdf.line(195,dd-cc+1.6, 195,p1)                       # 2nd vertical line
                            dd=p1
                            h=h+6
                            flag12==True 
                    m4=h    
                            
                if msg_total_debit[i] != 'Test' and flag12==False and m3>100 and m4<100:
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m3-20,15,m3-60)                             # 1st vertical line of total table  
                    pdf.line(195,m3-20,195,m3-60)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m3,txt = 'TOTAL DEBIT')

                    pdf.cell(30)
                    pdf.cell(20,m3,txt = str(msg_total_debit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m3+8,txt = 'TOTAL CREDIT')
                    
                    pdf.cell(30)
                    pdf.cell(20,m3+8,txt = str(msg_total_credit[i]))

                    pdf.ln(1)
                    pdf.cell(20)
                    pdf.cell(10,m3+12,txt = 'MONTHLY AVERAGE')
                    
                    # pdf.cell(30)
                    # pdf.cell(40,h+25,txt = str(monthly_avg[i][j]))

                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m3-20 , w = 180 , h = 4, style = 'DF')      
                    pdf.ln(1)
                    pdf.set_font('Arial','',7.2)
                    pdf.cell(4)
                    pdf.cell(10,m3+45,txt ='Sekiranya anda mendapati sebarang perbezaan, sila maklumkan kepada pihak Bank di dalam tempoh 14 hari daripada tarikh penyata ini. Jika tiada perbezaan')   
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m3+50 , txt = 'penyata ini akan dianggap betul. ')
                    pdf.set_font('Arial','I',7.1)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m3+55,txt= 'If you note any discrepancies, please advise the Bank within 14 days from the date of this statement, otherwise this account statement is considered to be correct. ')
                    pdf.set_font('Arial','',7.2)
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m3+60,txt = 'Untuk pertanyaan, ajukan kepada / For enquiries, please channel to: ')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m3+65,txt = 'Jabatan Khidmat Pelanggan (Customer Care Department), Tingkat 17, Menara Bank Islam, No 22, Jalan Perak, 50450 Kuala Lumpur')
                    pdf.ln(1)
                    pdf.cell(4)
                    pdf.cell(10,m3+70,txt = 'Tel: 03-26 900 900 / Faks: 03-2782 1337. Emel / Email: contactcenter@bankislam.com.my')

                if msg_total_debit[i] == 'Test' and flag12==False and m3>100 and m4<100:
                    # print('I am inside Bal Bf with message')
                    pdf.ln(1)
                    pdf.set_line_width(0.01)  
                    pdf.line(15,m3-20,15,m3-60)                             # 1st vertical line of total table  
                    pdf.line(195,m3-20,195,m3-60)                           # 2nd vertical line of total tabel

                    pdf.set_font('Arial','B',8)
                    pdf.cell(20)
                    pdf.cell(10,m3,txt = 'NO MESSAGE')

                    pdf.set_fill_color(r=0,g=0,b=0)
                    pdf.set_line_width(0.01)
                    pdf.rect(x = 15 , y = m3-20 , w = 180 , h = 4, style = 'DF')      
                    pdf.ln(1)

    
            

        kc1 = 1
        pdf_merger = PdfFileMerger()
        date1 = datetime.now()
        d = date1.strftime('%d')
        m = date1.strftime('%m')
        y = date1.strftime('%y')
        y = y[2:4]

        if m == '01':
            month = 'JAN'
        if m == '02':
            month = 'FEB'
        if m == '03':
            month = 'MAR'
        if m == '04':
            month = 'APR'
        if m == '05':
            month = 'MAY'
        if m == '06':
            month = 'JUN'
        if m == '07':
            month = 'JUL'
        if m == '08':
            month = 'AUG'
        if m == '09':
            month = 'SEP'
        if m == '10':
            month = 'OCT'
        if m == '11':
            month = 'NOV'
        if m == '12':
            month = 'DEC'


        filename = os.path.abspath(r"%s\C-%s%s%s_0000%s.pdf"%(kk1,d,month,y,kc2))
        f = filename    
        print(Total_email_accounts,'EMAIL ACCOUNTS PDF CREATED')
        print(i,'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        pdf.output(f)    
        kc2 +=  1  

    
    path20 = r'E:\IWOC\SOURCE' 
    target = r'E:\IWOC\TEMP' 

    for i in move_files:
        src_path = os.path.join(path20, i)
        dst_path = os.path.join(target, i)
        os.rename(src_path, dst_path)
    print('Files Moved................')




                
    
