from PyPDF2 import PdfMerger, PdfFileMerger
from os import path
from APP.models import History,DetailActivity
import datetime
from datetime import datetime
from datetime import date
from urllib import request
import os
import pandas as pd
from datetime import date
from fpdf import FPDF
import pandas as pd
from PyPDF2 import PdfFileMerger
from fpdf import FPDF
from os import path
from turtle import pen
from PyPDF2 import PdfFileWriter, PdfFileReader
import pandas as pd
from fpdf import FPDF
import pandas as pd
from datetime import datetime


def BKRCC(request,files1):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =+++++++++++++++++++++++++++++++++++++++++++++++++++++++++", current_time)

    move_files = []
    move_files.append(files1)
    def Folder_creation(cppp):
        # ------------------Capture date----------------
        cppp=str(cppp)
        today=date.today()
        d1 = today.strftime("%d-%b-%Y")
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
        directory=d1
        parent_dir = "E:\IWOC\OUTPUT\BANK RAKYAT\CYCLE/"
        directory = d1+"_"+start_time 
        path1 = os.path.join(parent_dir, directory) # date folder path
        os.mkdir(path1)
        # print("Directory '% s' created" % directory)

        directory = 'BKRCC'
        parent_dir = path1
        path2 = os.path.join(path1, directory) # bkrcc folder path
        os.mkdir(path2)
        # print("Directory '% s' created" % directory)

        directory = 'DIGITAL'
        parent_dir = path2
        path3 = os.path.join(path2, directory) # DIGITAL folder path
        os.mkdir(path3)
        # print("Directory '% s' created" % directory)

        directory = 'PRINTING'
        parent_dir = path2
        path4 = os.path.join(path2, directory) # PRINTING folder path
        os.mkdir(path4)
        # print("Directory '% s' created" % directory)

        return path3

    cppp = 1
    path11=r'E:\IWOC\SOURCE\\'+ files1
    def table3():
        with open(path11)as infile: 
            copy = False
            k2=[]
            k1 = []
            k4 = []
            k3 = []
            # for line in infile:
            for p in range(0,total_lines):
                line=infile.readline()
                line=line.strip()
                def f1(line):
                    
                    k1.append(line[66:74])
                    k2.append(line[82:123])
                    k4.append(line[151:159])
                    k3.append(line[169:179])
                    # print(line,'-------')
                    
                def f2(line):
                    k2.append('Test')
                    k1.append('Test')
                    k4.append('Test')
                    k3.append('Test')


                if line.startswith("TD"):
                    f1(line)
                    continue
                if line.startswith("CT"):
                    f2(line)
                else:
                    pass
        # ---------------------------->

            size1 = len(k1)
            idx_list = [idx + 1 for idx, val in
                    enumerate(k1) if val == 'Test']

            size2 = len(k2)
            idx_list = [idx + 1 for idx, val in
                    enumerate(k2) if val == 'Test']

            size3 = len(k3)
            idx_list = [idx + 1 for idx, val in
                    enumerate(k3) if val == 'Test']

            size4 = len(k4)
            idx_list = [idx + 1 for idx, val in
                    enumerate(k4) if val == 'Test']

            res1 = [k1[i: j] for i, j in
                zip([0] + idx_list, idx_list +
                ([size1] if idx_list[-1] != size1 else []))]

            res2 = [k2[i: j] for i, j in
                zip([0] + idx_list, idx_list +
                ([size2] if idx_list[-1] != size2 else []))]
            
            res3 = [k3[i: j] for i, j in
                zip([0] + idx_list, idx_list +
                ([size3] if idx_list[-1] != size3 else []))]

            res4 = [k4[i: j] for i, j in
                zip([0] + idx_list, idx_list +
                ([size4] if idx_list[-1] != size4 else []))]
        maxList1 = max(len(x) for x in res1)
        maxList2 = max(len(x) for x in res2)
        maxList3 = max(len(x) for x in res3)
        maxList4 = max(len(x) for x in res4)
        for item in res1:               
            while len(item) < maxList1:   
                item.append('Test')
        for item in res2:               
            while len(item) < maxList2:   
                item.append('Test')
        for item in res3:               
            while len(item) < maxList3:   
                item.append('Test')
        for item in res4:               
            while len(item) < maxList4:   
                item.append('Test')
        

    #--------------------------first date table of transaction --------------------
        
        h = 60
        for j in range(0,maxList1):
            if j == 0:
                pdf.ln(1)
                pdf.set_font('Arial', 'B', 10)
                pdf.cell(32)
                pdf.cell(10,h,txt = res2[i][j])
                pdf.set_font('Arial', 'B', 10)
                pdf.cell(130)
                if len(res4[i][j]) > 0:
                    if res4[i][j][-1] == '+':
                        res4[i][j] =  res4[i][j][0:-1].strip()
                        # res4[i][j][-1]  +
                    if res4[i][j][-1] == '-':
                        p = res4[i][j][0:-1].strip()
                        res4[i][j] = res4[i][j][-1]  + p
                a  = res4[i][j]
                n  = len(a)
                if (n <= 7 and a[0] == '-' )or(n <= 6 and a[0] != '-') : 
                    pdf.cell(0,h,txt = str(a))
                else:
                    a = a[0:1] + ',' + a[1:n-1] +   a[n-1:]
                    pdf.cell(0,h,txt =str(a) ,align='R')
            
            if j == 1:
                pdf.ln(1)
                pdf.set_font('Arial', 'B', 10)
                pdf.cell(32)
                pdf.cell(10,h-10,txt = res2[i][j])

                pdf.set_font('Arial', 'B', 10)
                pdf.cell(26)
                pdf.cell(10,h-10,txt = Name1[i])
            
            if 'SUB TOTAL BALANCE ' in res2[i][j]:
                pdf.ln(1) 
                pdf.set_font('Arial', 'B', 10)
                pdf.cell(32)
                pdf.cell(10,h-10,txt = res2[i][j])
                if res4[i][j] != 'Test':
                    pdf.set_font('Arial', 'B', 10)
                    pdf.cell(138)
                    if len(res4[i][j]) > 0:
                        if res4[i][j][-1] == '+':
                            res4[i][j] =res4[i][j][0:-1]
                        if res4[i][j][-1] == '-':
                            p = res4[i][j][0:-1].strip()
                            res4[i][j] = res4[i][j][-1]  + p
                    a  = res4[i][j]
                    n  = len(a)
                    if (n <= 7 and a[0] == '-' )or(n <= 6 and a[0] != '-') : 
                        pdf.cell(0,h-10,txt = str(a),align='R')
                    else:
                        a = a[0:1] + ',' + a[1:n-1] +   a[n-1:]
                        pdf.cell(0,h-10,txt =str(a) ,align='R')
                        
                pdf.ln(1)  
            if res1[i][j] == '00000000':
                pdf.ln(10)
                continue
            elif res1[i][j] == 'Test':    
                continue
            elif res2[i][j] == 'Test':    
                continue
            elif res4[i][j] == 'Test':     # --- adede now to check
                continue
            elif res3[i][j] == 'Test':     # --- adede now to check
                continue
            else:
                a = res1[i][j]
                d = a[0:2] +  "/" + a[2:4] + "/" + a[4:8]
                pdf.ln(1)
                pdf.set_font('Arial', '', 10)
                pdf.cell(5)
                pdf.cell(10,h-10,txt = d)
                pdf.set_font('Arial', '', 10)
                pdf.cell(17)
                pdf.cell(10,h-10,txt = res2[i][j])
                if res4[i][j] != 'Test':
                    pdf.set_font('Arial', '', 10)
                    pdf.cell(130)
                    if len(res4[i][j]) > 0:
                        if res4[i][j][-1] == '+':
                            res4[i][j] =  res4[i][j][0:-1].strip()
                        if res4[i][j][-1] == '-':
                            p = res4[i][j][0:-1].strip()
                            res4[i][j] = res4[i][j][-1]  + p
                    a  = res4[i][j]
                    n  = len(a)
                    if (n <= 7 and a[0] == '-' )or(n <= 6 and a[0] != '-'): 
                        pdf.cell(0,h-10,txt = str(a),align = 'R')
                    elif n == 8 and a[0] == '-':
                        a = a[0:2] + ',' + a[2:n-1] +   a[n-1:]
                        pdf.cell(0,h-10,txt =str(a) ,align='R')
                    else:
                        a = a[0:1] + ',' + a[1:n-1] +   a[n-1:]
                        pdf.cell(0,h-10,txt =str(a) ,align='R')
                pdf.cell(-45)   # 50 first
                a = res3[i][j]
                a = a.replace("+"," ")
                pdf.cell(10,h-10,txt = str(a),align='R')  
                h = h + 6


    #-------------------------------merged the 2 and 4th page of information in the main pdf---------------------------  
    kk=Folder_creation(cppp)
    cppp += 1
    def merge(p,date1):
        pdf_merger = PdfFileMerger()
        pdf_merger.append(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\\\t2.pdf')
            
        pdf_merger.merge(1,r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\page2.pdf')
        pdf_merger.merge(3,r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\page4.pdf')

        d = date1[0:2] 
        m = date1[2:4]
        y = date1[6:8]


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


        # with open(path.abspath(r"C:\IWOC\OUTPUT\C-%s%s%s_0000%s.pdf"%(d,month,y,p)),'wb')  as append_pdf:
        with open(path.abspath(r"%s\C-%s%s%s_0000%s.pdf"%(kk,d,month,y,p)),'wb')  as append_pdf:
            pdf_merger.write(append_pdf)


    Name=[] # -----------Name of the client on 1st page
    Name1 = [] #------------ Name on the client on 3rd page
    ad2=[]
    ad3=[]
    ad4=[]
    ad5=[]
    ad6=[]
    ad7=[]
    ad8=[]
    Statement_date=[]
    Paydue_date=[]
    Combine_Limit=[]
    Customer_title=[]
    credit_no=[]
    Accumulated_points=[] 
    t11=[]
    t12=[]
    t13=[]
    t14=[]
    t15=[]
    #-------------Added new empty list without extracting exact data----
    profit_rate = []   
    current_balance = []
    current_minimum_payment = []
    overdue_amount = []
    min_payment_due = []
    current_points_earned = []
    points_redeemed = []
    total_current_points = []
    total_current_points_rm= []
    profit_rebate_rm = []
    tabung_rakyat_rewards_rm = []
    total_transaction = []
    foreign_currency = []

    #---------------------5th page transaction empty  list----------------------------

    TP = []
    TP_final = []
    TP2 = []
    with open(path11) as file:
        lines=file.readlines()
        total_lines=len(lines)
        file.seek(0)

        def TP_f(TP):
            TP_final.append(TP)

        def TP_F1(l2):
            TP.append(l2[2:26])
            TP.append(l2[26:34])     #28
            TP.append(l2[71:79])     # 71:78
            TP.append(l2[78:83].strip())    # 78:83
            TP.append(l2[85:87])
            TP.append(l2[95:103])
            TP_f(TP)        

        def TP_F2():
            TP2.append('TP_Test')
            TP_f(TP2)
        for i in range(0,total_lines):
    # --------------2nd line in file add in 2nd dataframe------------------------------------
            line=file.readline() 
            line=line.strip()
            TP2  = []
            TP = []

    # ---------------------- Details in table-------------------------------------------
            if line.startswith("TD"):
                l2 = file.readline()
                l2 = l2.strip()
                l4 = line[169:179]
                foreign_currency.append(l4)
                if l2.startswith('CT'):
                    TP_F2()
                if l2.startswith('TP'):
                    TP_F1(l2)

            if line.startswith('CH') and not line.endswith('CT'):
                l1=line[46:86]
                l1=l1.strip()
                n1 = line[46:71]
                n1 = n1.strip()
                Name.append(l1)
                Name1.append(n1)
                l2=line[86:126]
                l2=l2.strip()
                ad2.append(l2)
                l3=line[126:166]
                if  any(c.isalnum() for c in l3):
                    l3=l3.strip()
                    ad3.append(l3)
                else:
                    ad3.append('NULL')
                l4=line[166:206]
                if  any(c.isalnum() for c in l4):
                    l4=l4.strip()
                    ad4.append(l4)
                else:
                    ad4.append('NULL')
                l5=line[208:246]
                if  any(c.isalnum() for c in l5):
                    l5=l5.strip()
                    ad5.append(l5)
                else:
                    ad5.append('NULL')
                l6=line[246:286]
                if  any(c.isalnum() for c in l6):
                    l6=l6.strip()
                    ad6.append(l6)
                else:
                    ad6.append('NULL')
                l7=line[286:311]
                if  any(c.isalnum() for c in l7):
                    l7=l7.strip()
                    ad7.append(l7)
                else:
                    ad7.append('NULL')
                l8=line[311:336]
                if  any(c.isalnum() for c in l8):
                    l8=l8.strip()
                    ad8.append(l8)
                else:
                    ad8.append('NULL')
                
                l9=line[372:380]
                l9=l9.strip()
                Statement_date.append(l9)
                l10=line[388:396]
                l10=l10.strip()
                Paydue_date.append(l10)

                l11=line[402:407]
                if  any(c.isalnum() for c in l8):
                    l11=l11.strip()
                    Combine_Limit.append(l11)
                else:
                    Combine_Limit.append('NULL')

                l12=line[413:420]
                if  any(c.isalnum() for c in l8):
                    l12=l12.strip()
                    Customer_title.append(l12)
                else:
                    Customer_title.append('NULL')
                
    #--------------------------added new data ext from profit rate--------------------------

            if line.startswith('AH'):
                l13=line[162:168]
                if  any(c.isalnum() for c in l13):
                    l13=l13.strip()
                    Accumulated_points.append(l13)
                else:
                    Accumulated_points.append('NULL')
                l14=line[323:328]
                if  any(c.isalnum() for c in l14):
                    l14=l14.strip()
                    profit_rate.append(l14)
                else:
                    profit_rate.append('NULL')

                l15=line[101:108]
                if  any(c.isalnum() for c in l15):
                    l15=l15.strip()
                    current_balance.append(l15)
                else:
                    current_balance.append('NULL')

                l16=line[119:126]
                if  any(c.isalnum() for c in l16):
                    l16=l16.strip()
                    current_minimum_payment.append(l16)
                else:
                    current_minimum_payment.append('NULL')
                
                l17=line[137:142]
                if  any(c.isalnum() for c in l17):
                    l17=l17.strip()
                    overdue_amount.append(l17)
                else:
                    current_minimum_payment.append('NULL')

                l18=line[151:157]
                if  any(c.isalnum() for c in l18):
                    l18=l18.strip()
                    min_payment_due.append(l18)
                else:
                    min_payment_due.append('NULL')

                l19=line[174:179]
                if  any(c.isalnum() for c in l19):
                    l19=l19.strip()
                    current_points_earned.append(l19)
                else:
                    current_points_earned.append('NULL')
                
                l20=line[180:184]
                if  any(c.isalnum() for c in l20):
                    l20=l20.strip()
                    points_redeemed.append(l20)
                else:
                    points_redeemed.append('NULL')

                l21=line[197:203]
                if  any(c.isalnum() for c in l21):
                    l21=l21.strip()
                    total_current_points.append(l21)
                else:
                    total_current_points.append('NULL')
                
                l22=line[197:201]
                if  any(c.isalnum() for c in l22):
                    l22=l22.strip()
                    total_current_points_rm.append(l22)
                else:
                    total_current_points_rm.append('NULL')

                l23=line[230:233]
                if  any(c.isalnum() for c in l23):
                    l23=l23.strip()
                    profit_rebate_rm.append(l23)
                else:
                    profit_rebate_rm.append('NULL')
                
                l24=line[346:350]
                if  any(c.isalnum() for c in l24):
                    l24=l24.strip()
                    tabung_rakyat_rewards_rm.append(l24)
                else:
                    tabung_rakyat_rewards_rm.append('NULL')

                l26=line[101:108]
                if  any(c.isalnum() for c in l26):
                    l26=l26.strip()
                    total_transaction.append(l26)
                else:
                    total_transaction.append('NULL')


    # --------------2nd line in file add in 2nd dataframe------------------------------------

                l21=line[8:27]
                credit_no.append(l21)



    #-------------------------------------CREATING EMPTY DATAFRAMES -------------------------------------------------------
    # print(points_redeemed,'pointsredeemmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
    df1=pd.DataFrame()
    df1['Name']=Name
    df1['Company name']=ad2
    df1['Address1']=ad3
    df1['Address2']=ad4
    df1['Address3']=ad5
    df1['Address4']=ad6
    df1['City']=ad7
    df1['State']=ad8
    df1['Statement date']=Statement_date
    df1['Paydue date']=Paydue_date
    df1['Combine Limit']=Combine_Limit
    df1['Customer Title']=Customer_title
    df1['Accumalated Points']=Accumulated_points
    df1['profit_rate'] = profit_rate
    df1['current_balance'] = current_balance
    df1['current_minimum_payment'] = current_minimum_payment
    df1['overdue_amount'] = overdue_amount
    df1['min_payment_due'] = min_payment_due
    df1['current_points_earned'] = current_points_earned
    df1['points_redeemed'] = points_redeemed
    df1['total_current_points'] = total_current_points
    df1['total_current_points_rm'] = total_current_points_rm
    # df1['TP']  = TP_final
    df1['total_transaction'] = total_transaction
    df1['profit_rebate_rm'] = profit_rebate_rm
    df1['tabung_rakyat_rewards_rm'] = tabung_rakyat_rewards_rm

    #-----------------------5th page creating DF's-------------------------------------------
    df2=pd.DataFrame()
    df2['credit no']=credit_no
    total_clients = df1.shape[0]

    #------------------------------------Code design---------------------------------------
    #------------------------------------------LOG FILE CREATION -----------------------------
    time1 = datetime.now() 
    start_time=time1.strftime("%H:%M:%S")
    date1 = time1.strftime("%d/%b/%Y")
    file=open(r"E:\\IWOC\\LOG_FILES\\bkrcc.txt","a")
    file.write("Pro Office Solutions Sdn. Bhd.\n")
    file.write("FIRST REMINDER\n")
    file.write("=============================================================\n")
    file.write("Program ID           : FIRST REMINDER.PDS\n")
    file.write("Paper Type           :\n")
    file.write("File Name (PDF)      : R1 31102022_011122.srt.PDF\n")
    file.write("Data Name (TXT)      :")
    file.write(" ")
    file.write(str(files1))
    file.write("\n")
    file.write("Total Accounts       :        ")
    file.write(str(total_clients))
    file.write("\n")
    file.write("Total Pages          :        ")
    file.write(str(total_clients))
    file.write("\n")
    file.write("Total Impression     :        ")
    file.write(str(total_clients*2))
    file.write("\n")

    file.write("First Record         : ")
    file.write(df2['credit no'].iat[0])
    file.write("\n")
    file.write("Last Record          : ")
    last_record=str(df2['credit no'].iat[-1])
    # last_record=  ('2222222222')
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

    # last_bkrcc_no = History.objects.order_by('-JobIDX')[0:1]
    # print(last_bkrcc_no,'jobbiddddddddddddd')
    # last_no = list(last_bkrcc_no)
    # print(last_no,type(last_no),'lastnooooooooooooooooooooooooooo')
    # z2 = []
    # for z in last_no:
    #     z2.append(z1)   
    # for z3 in z2:
    #     print(z3)
    #     z1 = z3
    # #------------------------------------------LOG FILE END------------------------------------
    p = 1
    for i in range(0,total_clients):
        pdf = FPDF()
        pdf.add_page() 
        Tp_pages=len(TP_final[i])
        if Tp_pages > 1:
            number_of_pages = 3
        else:
            number_of_pages = 2
        pdf.set_auto_page_break(auto=False)
        pdf.ln(2)
        
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\\fstheading.jpg',5,8,200)
    
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\\BKRStatement-01.jpg',150,32.5,20)
        pdf.set_draw_color(r=128, g=128, b=128)
        pdf.set_line_width(0.3)
        pdf.line(168,33.6,180,33.6)   # 1st horizontal line
        pdf.line(168,41.8,180,41.8)   # 2nd horizonatl line
        pdf.line(180,33.6, 180, 41.8)     # 1st  vertical line  
        
    #-----------------------------value of page number added here---------------------------------
        pdf.set_font('Arial', '', 8)
        pdf.cell(160)
        pdf.cell(20,50,str(pdf.page_no()),'C')
        pdf.cell(-18)
        pdf.cell(10,50,txt ='of '+ str(number_of_pages))

    #-----------------------------STATEMENT DATE AND VALUE ------------------------
        pdf.ln(2)
        pdf.ln(1)
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\\BKRStatement-02.jpg',140,45,60)
        pdf.line(141.5,63,198.8,63)              # horozantal line
        pdf.line(141.5,63, 141.5, 56)        # first vertical lin
        pdf.line(167.8,63, 167.8, 56)
        pdf.line(198.8,63, 198.8, 56) 
        pdf.ln(2)
        pdf.ln(2)
        pdf.cell(134)
        a = df1['Statement date'][i]
        d = a[0:2] +  "/" + a[2:4] + "/" + a[4:8]
        pdf.cell(10,82,txt = str(d))
        pdf.cell(18)
        a = df1['Paydue date'][i]
        d = a[0:2] +  "/" + a[2:4] + "/" + a[4:8]
        pdf.cell(10,82,txt = str(d))


    #--------------------inserting name address city state------------------------------------

        pdf.ln(1)
        pdf.set_font('Arial', '', 8)
        pdf.cell(7,30,txt = df1['Customer Title'][i])
        pdf.cell(1)
        pdf.cell(10,30,txt = df1['Name'][i])
        pdf.ln(3)
        pdf.set_font('Arial', '', 8)
        pdf.cell(10,30,txt = df1['Company name'][i])   
        if not df1['Address1'][i] == 'NULL':
            pdf.ln(1.5)
            pdf.set_font('Arial', '', 8)
            pdf.cell(10,35,txt = df1['Address1'][i])  
            pdf.ln(1.5)
        else:
            pdf.ln(1.5)
            pdf.set_font('Arial', '', 8)
            pdf.cell(10,35,txt = '')  
            pdf.ln(1.5)
        if not df1['Address2'][i] == 'NULL':
            pdf.ln(1.5)
            pdf.set_font('Arial', '', 8)
            pdf.cell(10,35,txt = df1['Address2'][i]) 
            pdf.ln(1.5)
        else:
            pdf.ln(1.5)
            pdf.set_font('Arial', '', 8)
            pdf.cell(10,35,txt = '')  
            pdf.ln(1.5)
        if not df1['Address3'][i] == 'NULL':
            pdf.ln(2)
            pdf.set_font('Arial', '', 8)
            pdf.cell(10,35,txt = df1['Address3'][i]) 
            pdf.set_font('Arial', '', 8)
        else:
            pdf.ln(1.5)
            pdf.set_font('Arial', '', 8)
            pdf.cell(10,35,txt = '')  
            pdf.ln(1.5)
        if not df1['City'][i] == 'NULL':
            pdf.ln(3)
            pdf.set_font('Arial', '', 8)
            pdf.cell(10,35,txt = df1['City'][i]) 
        else:
            pdf.ln(1.5)
            pdf.set_font('Arial', '', 8)
            pdf.cell(10,35,txt = '')  
            pdf.ln(1.5)
        if not df1['State'][i] == 'NULL':
            pdf.ln(3)
            pdf.set_font('Arial', '', 8)
            pdf.cell(10,35,txt = df1['State'][i]) 
        else:
            pdf.ln(1.5)
            pdf.set_font('Arial', '', 8)
            pdf.cell(10,35,txt = '')  
            pdf.ln(1.5)

    #------------------------------------------adding akaun and dashed line here----------------------------------
        pdf.ln(1)
    
    
        pdf.set_font('Arial', '', 8)
        pdf.cell(30)
        pdf.cell(30, 65,'Akaun anda tertunggak selama  0 hari setakat penyata ini. Sila buat bayaran dengan segera','C')
        pdf.ln(4)
        pdf.cell(30)
        pdf.cell(30, 65,'Your account is overdue for 0 days as at this statement. Kindly remit payment immediately.','C')
        pdf.set_line_width(0.1)
        pdf.set_draw_color(r=0, g=0, b=0) 
        pdf.dashed_line(0, 80, 220, 80, 1, 2)
        pdf.ln(7)
    #---------------------------------------NOTA PENTING-------------------------------------------------------
        
        pdf.set_font('Arial', 'B', 8)
        pdf.cell(35,70,'NOTA PENTING:')
        pdf.ln(1)
        pdf.set_font('Arial', '', 6.8)
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\Note icon.jpg',10.8,86,2.5)
        pdf.cell(4)
        pdf.cell(40,75,txt = 'Jika terdapat sebarang percanggahan atas  urusniaga yang  disenaraikan, sila maklumkan kepada kami secara bertulis dalam masa 14 hari dari tarikh penyata kad. Jika tidak,')
        pdf.ln(1)
        pdf.cell(4)
        pdf.cell(48,78,txt = 'penyata kad ini dianggap sah dan tepat.')
        
        pdf.ln(1)
        pdf.set_font('Arial', '', 6.9)
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\Note icon.jpg',10.8,91,2.5)
        pdf.cell(4)
        pdf.cell(40,82,txt = 'Sila maklumkan kepada Pusat Kad Bank Rakyat  terlebih dahulu sebelum anda membuat sebarang urusniaga di luar  negara dan / atau belian secara online melalui internet.')
    
        pdf.ln(1)
        pdf.set_font('Arial', '', 6.8)
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\Note icon.jpg',10.8,94,2.5)
        pdf.cell(4)
        pdf.cell(40,86,txt = 'Untuk pembatalan kad dan penutupan akaun kad kredit-i anda, sila hubungi Pusat Kad Bank Rakyat  untuk pengemaskinian rekod di pihak Bank dan Sistem Maklumat Rujukan')
        pdf.ln(1)
        pdf.cell(4)
        pdf.cell(48,90,txt = 'Kredit Berpusat (CCRIS).')
        
    # ---------------------ADDING  IMPORTANT NOTICE-------------------------------------------
        pdf.ln(1)
        pdf.set_font('Arial', 'B', 8)
        pdf.cell(35,95,'IMPORTANT NOTICE:')

        pdf.ln(1)
        pdf.set_font('Arial', '', 6.9)
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\Note icon.jpg',10.8,104.8,2.5)
        pdf.cell(4)
        pdf.cell(40,100,txt = 'If there is a discrepancy on this card statement, kindly notify  us in writing within 14 days from the date of this  card statement. Otherwise, the card statement shall be deemed')
        pdf.ln(1)
        pdf.cell(4)
        pdf.cell(48,104,txt = 'accurate and endorsed.')

        pdf.ln(1)
        pdf.set_font('Arial', '', 7)
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\Note icon.jpg',10.8,110.5,2.5)
        pdf.cell(4)
        pdf.cell(40,108,txt = 'Kindly notify Bank Rakyat Card Centre in advance prior to card usage for overseas transaction and / or online purchases via internet.')
    
        pdf.ln(1)
        pdf.set_font('Arial', '', 7)
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\Note icon.jpg',10.8,113.2,2.5)
        pdf.cell(4)
        pdf.set_font('Arial', '', 6.9)
        pdf.cell(40,112,txt = "For credit card-i cancellation and account closure, kindly contact  Bank Rakyat Card Centre for the Bank and Central Credit Reference Information System (CCRIS)'s records")
        pdf.ln(1)
        pdf.cell(4)
        pdf.cell(48,116,txt = 'updating purposes.')

    #-------------------------------Third Table Credit card No------------------------------
    

        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\BKRStatement-03.jpg',12,120,188)
    

        pdf.set_line_width(0.3)
        pdf.set_draw_color(r=128,g=128,b=128)
        pdf.line(14,138,198.1,138)  #  3r table  2nd row horizontal line
        pdf.line(14,131, 14, 138)  # 3rd table 2nd row 1 st vertical line 
        pdf.line(56,132, 56, 138)  # 3rd table 2nd row 2 st vertical line
        pdf.line(87.9,132, 87.9, 138)   # 3rd table 2nd row 3 st vertical line
        pdf.line(125.8,132, 125.8, 138)  #3rd table 2nd row 4 st vertical line
        pdf.line(151.8,132, 151.8, 138) # 3rd table 2nd row 5 st vertical line
        pdf.line(198.2,131, 198.2, 138) # 3rd table 2nd row6 st vertical line

        pdf.ln(1)
    
        pdf.ln(4)

    #------------------------------------------Inserting values into 3rd table--------------------------------
        pdf.ln(1)
        pdf.set_font('Arial', '', 8)
        pdf.cell(6)
        pdf.cell(10,138,txt = df2['credit no'][i])
        
        pdf.set_font('Arial', '', 8)
        pdf.cell(36)
        a = df1['Statement date'][i]
        d = a[0:2] +  "/" + a[2:4] + "/" + a[4:8]
        pdf.cell(10,138,txt = str(d))


        pdf.set_font('Arial', '', 8)
        pdf.cell(25)
        a = df1['Combine Limit'][i]
        n = len(a)
        a  = str(a)
        if n >= 4 and a[0] != '0':  
            a = a[0:1] + ',' + a[1:4] + '.' +  a[3:7]
            pdf.cell(10,138,txt = str(a))
        elif n >= 4 and a[0] == '0':  
            a = a[1:-2] + '.' +  a[-2:]
            pdf.cell(10,138,txt = str(a))
        else:
            pdf.cell(10,138,txt = str(a))


        pdf.set_font('Arial', '', 8)
        pdf.cell(26)
        pdf.cell(10,138,txt = '0.00')


        pdf.set_font('Arial', '', 8)
        pdf.cell(20)
        pdf.cell(10,138,txt = df1['profit_rate'][i])

    # ----------------------------Inserting 4th table--------------------------
        pdf.ln(1)
    

        pdf.set_line_width(0.3)
        pdf.set_draw_color(r=128,g=128,b=128)
        pdf.line(20.2,164,190.8,164)      # horizontal line     
        pdf.line(20.2,140, 20.2, 164)       # 1st vertical line
        pdf.line(57.5,152, 57.5, 164)  
        pdf.line(107,155, 107, 164)    
        pdf.line(146,155, 146, 164)  
        pdf.line(190.8,155, 190.8, 164)  


        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\\currentbalance4.png',18.5,140.7,174)    
        pdf.ln(1)
        
        pdf.ln(1)

        pdf.ln(1)
    

    #-----------------------------------------INSERTING 4TH TABLE VALUES---------------------------------
        pdf.ln(2)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25)
        a = df1['current_balance'][i]
        n = len(a)
        if n > 5: 
            a = a[0:1] + ',' + a[1:n-1] +   a[n-1:]
            pdf.cell(10,178,txt =str(a))
        else:
            pdf.cell(10,178,txt = str(a))
        # pdf.cell(10,178,txt = str(a))

        pdf.set_font('Arial', '', 8)
        pdf.cell(25)
        pdf.cell(10,178,txt = df1['current_minimum_payment'][i])

        pdf.set_font('Arial', '', 8)
        pdf.cell(40)
        pdf.cell(10,178,txt = df1['overdue_amount'][i])

        pdf.set_font('Arial', '', 8)
        pdf.cell(30)
        pdf.cell(10,178,txt = df1['min_payment_due'][i])

    #---------------------------INSERTING 5 Th and 6 th TABLE mal and eng -----------------

        pdf.ln(1)                             # 5 th table
        pdf.set_draw_color(r=128, g=128, b=128)
        pdf.set_line_width(0.1)
        pdf.rect(x = 14 , y = 167 , w = 94 , h = 50, style = 'D')

        pdf.set_draw_color(r=128, g=128, b=128)                   # 6 th tbale
        pdf.set_line_width(0.01)
        pdf.rect(x = 109 , y = 167 , w = 90 , h = 50, style = 'D')

    #------------------------------INSERTING HEADER AND VALUES OF 5 AND 6-------------------------

        pdf.ln(100)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(16)
        pdf.cell(20,0,txt = 'NOTIS JIKA HANYA MEMBUAT')

        pdf.set_font('Arial', 'B', 12)
        pdf.cell(70)
        pdf.cell(20,0,txt = 'NOTICE ON PAYING ONLY MINIMUM')

        pdf.ln(1)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(12)
        pdf.cell(10,6,txt = 'BAYARAN MINIMA SETIAP BULAN')

        pdf.set_font('Arial', 'B', 12)
        pdf.cell(95)
        pdf.cell(10,6,txt = 'MONTHLY PAYMENT')

        pdf.ln(1)
        pdf.set_font('Arial', '', 11)
        pdf.cell(7)
        pdf.cell(10,14,txt = 'Jika anda hanya membuat bayaran minima setiap')

        pdf.set_font('Arial', '', 11)
        pdf.cell(85)
        pdf.cell(14,14,txt = 'If you make the minimum payment every month ,')

        pdf.ln(1)
        pdf.set_font('Arial', '', 11)
        pdf.cell(7)
        pdf.cell(10,20,txt = 'bulan,  tempoh bayaran yang akan diambil adalah')

        pdf.set_font('Arial', '', 11)
        pdf.cell(85)
        pdf.cell(10,20,txt = 'it  will take   you longer  to  pay  off  your balance')

        pdf.ln(1)
        pdf.set_font('Arial', '', 11)
        pdf.cell(7)
        pdf.cell(10,26,txt = 'lebih lama untuk menyelesaikan baki semasa, caj')

        pdf.set_font('Arial', '', 10.8)
        pdf.cell(85)
        pdf.cell(10,26,txt = 'including profit and other charges payable.Please')


        pdf.ln(1)
        pdf.set_font('Arial', '', 11)
        pdf.cell(7)
        pdf.cell(10,32,txt = 'keuntungan dan lain - lain caj yang berkaitan. Sila')

        pdf.set_font('Arial', '', 10.8)
        pdf.cell(85)
        pdf.cell(10,32,txt = 'refer to the back page for more information or you')

        pdf.ln(1)
        pdf.set_font('Arial', '', 11)
        pdf.cell(7)
        pdf.cell(10,38,txt = 'lihat muka surat belakang  untuk maklumat  lanjut')

        pdf.set_font('Arial', '', 10.8)
        pdf.cell(85)
        pdf.cell(10,38,txt = 'may refer to the credit card calculator available  at')

        pdf.ln(1)
        pdf.set_font('Arial', '', 10.8)
        pdf.cell(7)
        pdf.cell(10,42,txt ='atau anda boleh rujuk kepada kalkulator kad kredit')

        pdf.set_font('Arial', '', 11)
        pdf.cell(85)
        pdf.cell(10,42,txt = 'www.bankrakyat.com.my or ')

        pdf.ln(1)
        pdf.set_font('Arial', '', 11)
        pdf.cell(7)
        pdf.cell(10,48,txt = 'yang  terdapat   di www.bankrakyat.com.my  atau')

        pdf.set_font('Arial', '', 11)
        pdf.cell(85)
        pdf.cell(10,48,txt = 'www.bankinginfo.com.my')

        pdf.ln(1)
        pdf.set_font('Arial', '', 11)
        pdf.cell(7)
        pdf.cell(10,53,txt = 'www.bankinginfo.com.my')


    #-----------------------INSERTING 7 th table of reywards----------------------
    
        pdf.cell(10)
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\BKRStatement-05.jpg', 12,219,190)
        pdf.set_line_width(0.3)
        pdf.set_draw_color(r=128,g=128,b=128)
        pdf.line(14,253,199.8,253) # first _ line
        pdf.line(14,246, 14, 253)  # 1st vertical line |
        pdf.line(51,247.5, 51, 253)
        pdf.line(86.8,247.5, 86.8, 253)
        pdf.line(128,247.5, 128, 253)
        pdf.line(157.8,247.5, 157.8, 253)
        pdf.line(199.8,246, 199.8, 253)


    #-----------------------------INSERTING COLUMN NAMES OF TABLE 7 RAKYAT REWARDS----------------------

        pdf.ln(38)
        pdf.ln(1)
        pdf.ln(10)
        pdf.ln(3)
        pdf.ln(4)
    

    #-------------------------------INSERTING DATA OF TABLE 7 RAKYAT REWARDS-----------

        pdf.ln(2)
        pdf.set_font('Arial', '', 8)
        pdf.cell(15)
        a = int(df1['Accumalated Points'][i]) 
        a = str(a)
        n = len(a)
        if n > 5: 
            a = a[0:1] + ',' + a[1:n-2] +"."+   a[n-2:]
            pdf.cell(10,20,txt =str(a))
        elif n >= 5 : 
                a = a[0:1] + a[1:n-2] +  "."+  a[n-2:]
                pdf.cell(10,20,txt = str(a))
        else:
            pdf.cell(10,20,txt = str(a))
 
        pdf.set_font('Arial', '', 8)
        pdf.cell(25)
        a = int(df1['current_points_earned'][i]) 
        a = str(a)
        n  = len(a)
        a = a[0:1] +  a[1:n-2] + '.' +  a[n-2:]
        pdf.cell(10,20,txt = str(a))

        pdf.set_font('Arial', '', 8)
        pdf.cell(30)
        if df1['points_redeemed'][i] == '0000':
            pdf.cell(10,20,txt = '0.00')
        else:
            a = int(df1['points_redeemed'][i])
            a = str(a)
            n  = len(a)
            a = a[0:1] +  a[1:n-2] + '.' +  a[n-2:]
            pdf.cell(10,20,txt = str(a))


        pdf.set_font('Arial', '', 8)
        pdf.cell(25)
        a = int(df1['total_current_points'][i])
        a  = str(a) 
        n  = len(a)
        if n > 5:
            a = a[0:1] + ',' + a[1:n-2] + '.' +  a[n-2:]
            pdf.cell(10,20,txt = str(a))
        elif n > 3:
            a = a[0:2] + a[2:n-2]+ "."+ a[n-2:]
            pdf.cell(10,20,txt = str(a))
        else:
            pdf.cell(10,20,txt = str(a))
        pdf.set_font('Arial', '', 8)
        pdf.cell(20)
        a = int(df1['total_current_points_rm'][i])
        a = a / 100
        pdf.cell(10,20,txt = str(a))


    #--------------------------INSERTING 8 TH TABLE OF TABUNG RAKYAT REWARD------------------

        
        # pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\BKRStatement-06.jpg',18,254,145)
        # pdf.set_line_width(0.01)
        # pdf.set_draw_color(r=128,g=128,b=128)
        # pdf.line(19.4,283,160.5,283)

        # pdf.line(19.4,274,19.4,283)  # last | first num
        # pdf.line(92.4,275,92.4,283)  # 2 | num
        # pdf.line(160.5,274,160.5,283) # 3 rd | line

    #---------------------- INSERTING TABLE COLUMNS NAMES OF 8 TH TABLE -----------------------------------
        
        # pdf.ln(2)
        # pdf.ln(4)
        # pdf.ln(2)
        # pdf.ln(5)
        
    #-----------------------INSERTING DATA OF 8 TH TABLE -----------------------

        # pdf.ln(8)
        # pdf.set_font('Arial', '', 8)
        # pdf.cell(30)
        # a = int(df1['profit_rebate_rm'][i])
        # a = a / 100
        # pdf.cell(10,38,txt = str(a))

        # pdf.set_font('Arial', '', 8)
        # pdf.cell(70)
        # a = int(df1['tabung_rakyat_rewards_rm'][i])
        # a = a / 100
        # pdf.cell(10,38,txt = str(a))
        pdf.ln(1)
        pdf.cell(4)
        pdf.set_font('Arial', '', 9)
        pdf.cell(10,34,txt = 'Nota/')
        pdf.cell(-3)
        pdf.set_font('Arial', 'I', 9)
        pdf.cell(10,34,txt = ' Note')
        pdf.ln(1)
        pdf.cell(4)
        pdf.set_font('Arial', '', 9.8)
        pdf.cell(10,39,txt = 'Anda kini boleh memilih untuk menebus mata Ganjaran Rakyat anda untuk dikreditkan ke Akaun Semasa-i/Simpanan-i')
        pdf.ln(1)
        pdf.cell(4)
        pdf.set_font('Arial', '', 9.8)
        pdf.cell(10,45,txt = 'anda. Bagi urusan permohonan  penebusan mata Ganjaran Rakyat  Kad Kredit-i ke  Akaun Semasa-i/Simpanan-i Bank')
        pdf.ln(1)
        pdf.cell(4)
        pdf.set_font('Arial', '', 9.8)
        pdf.cell(10,51,txt = 'Rakyat, sila e-mel ke irewardcc@bankrakyat.com.my')
        pdf.cell(71.5)
        pdf.set_font('Arial', 'I', 9.8)
        pdf.cell(10,51,txt = '/You can now choose to redeem your Rakyat Rewards points to be')
        pdf.ln(1)
        pdf.cell(4)
        pdf.set_font('Arial', 'I', 9.8)
        pdf.cell(10,57,txt = 'credited to your Current/Savings Account-i. To apply for Credit Card-i Rakyat Rewards point redemption to Bank Rakyat')
        pdf.ln(1)
        pdf.cell(4)
        pdf.set_font('Arial', 'I', 9.8)
        pdf.cell(10,63,txt = 'Current Account-i/Savings-i, please email us at irewardcc@bankrakyat.com.my')

    #-------------------ADDING FOOTER LOGO-----------------------------------------------------------------------
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\FormALogo.jpg',10,285,190)
    #------------------------------------------------ADDING 3RD PAGE TABLE OF TR RECORDS--------------
        pdf.add_page()
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\fstheading.jpg',5,8,200)
        pdf.ln(20)
        pdf.ln(2)
        pdf.ln(4)
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\BKRStatement-07.jpg',8,50,200)
        pdf.set_draw_color(r=128,g=128,b=128)
        pdf.set_line_width(0.3)
        pdf.line(10, 63, 10, 260)   #first | line  
        pdf.line(40.8, 64, 40.8, 260)   # second | line
        pdf.line(131.9, 64, 131.9, 260)
        pdf.line(166, 64, 166, 260)
        pdf.line(205.4, 63, 205.4, 260)

        pdf.line(10, 250, 205, 250) # third - line
        pdf.line(10, 260, 205, 260) # fourth - line
        
        pdf.ln(2)
        pdf.cell(180)
        pdf.cell(20,10,str(pdf.page_no() ) ,' C ')
        pdf.cell(-18)
        pdf.cell(10,10,txt ='  of  ' + str(number_of_pages))
        pdf.ln(2)
        pdf.set_font('Arial','B',8)
        pdf.cell(60)
        pdf.cell(10,432,txt = 'TOTAL')
        pdf.cell(100)
        a = df1['total_transaction'][i]
        a  = str(a) 
        n  = len(a)
        if n > 5:
            a = a[0:1] + ',' + a[1:n-2] +  a[n-2:]
            pdf.cell(10,432,txt = str(a))
        elif n > 3:
            a = a[0:2] + a[2:n-2]+ a[n-2:]
            pdf.cell(10,432,txt = str(a))
        else:
            pdf.cell(10,20,txt = str(a))
        # pdf.cell(10,432,txt = str(a))
        pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\FormBLogo.jpg',10,280,180)

        table3()

        a = 'TP_Test'
        b = a.split()
        if TP_final[i] != b:
            # print(TP_final[i],'TPFINAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALLLLLLLLLLLLLLLLL')
            pdf.add_page()
            # print(TP_final[i],'yttttttttttttttttttttttttt')
            pdf.set_auto_page_break(auto=False)
            pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\fstheading.jpg',5,8,200)
            pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\BKRStatement-08.jpg',10,40,190)
            pdf.set_draw_color(r=128,g=128,b=128)
            pdf.set_line_width(0.1)
            pdf.line(12, 58, 12, 270)   #first | line  
            pdf.line(68.8, 58.6, 68.8, 270)   # second | line
            pdf.line(98, 59, 98, 270)    # 3rd vertical line
            pdf.line(129, 59, 129, 270)  
            pdf.line(163, 59, 163, 270)
            pdf.line(198, 58, 198, 270)
            pdf.line(12, 270, 198, 270)    # horizonatl line
            pdf.set_font('Arial','',10)
            pdf.cell(10,50,txt = 'RINGKASAN TRANSAKSI (SECARA ANSURAN) / TRANSACTION SUMMARY (INSTALLMENT)')
            pdf.cell(160)
            pdf.cell(10,50,str(pdf.page_no()),'C')
            pdf.cell(-6)
            pdf.cell(10,50,txt  ='of '+str(number_of_pages))
            pdf.ln(1)
            pdf.cell(4)
            pdf.cell(10,110,txt = str(TP_final[i][0]))  
            pdf.cell(55)
            a = str(TP_final[i][2])
            a  = str(a)
            n  = len(a)
            a = a[0:1] + ',' + a[1:n-1] +   a[n-1:]
            pdf.cell(10,110,txt = str(a))
            pdf.cell(20)
            if len(TP_final[i][3]) == 3:
                a = '0' + TP_final[i][3]
                pdf.cell(10,110,txt  =str(a))
            else:
                pdf.cell(10,110,txt = TP_final[i][3])
            pdf.cell(25)
            pdf.cell(10,110,txt = str(TP_final[i][4]))
            pdf.cell(25)
            a = TP_final[i][5]
            a = str(a)
            n = len(a)
            if n >= 5 : 
                a = a[0:1] + "," + a[1:n-2]+  a[n-2:]
            pdf.cell(10,110,txt = str(a))
            pdf.ln(1)
            pdf.cell(4)
            pdf.cell(10,120,txt = str(TP_final[i][1]))

            pdf.image(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\FormCLogo.jpg',10,280,180)
            
        pdf.output(r'E:\IWOC\APP SCRIPT\BANK RAKYAT\CYCLE\BKRCC\DATA\\t2.pdf')
        merge(p,Statement_date[i])
        p  += 1
    
    time1 = datetime.now()
    end_time=time1.strftime("%H:%M:%S")
    file.write("    ")
    file.write(str(end_time) )
    file.write('\n\n\n\n')
    file.close()

    #--------------PRINTING-------------------------
    
    root = r'E:\IWOC\OUTPUT\BANK RAKYAT\CYCLE/'
    dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]
    # print (dirlist)
    i = 'k'
    for j in dirlist:
        i  = j
    boot = r'\BKRCC\DIGITAL/'
    boot1 = r'\BKRCC\PRINTING/'
    finale_path = root + i + boot
    final_pr = root + i + boot1

    pdfs = os.listdir(finale_path)
    merger = PdfFileMerger(strict=False)
    for file in pdfs:
        if file.endswith(".pdf"):
            path_with_file = os.path.join(finale_path, file)
            merger.append(path_with_file,  import_bookmarks=False )
    merger.write(final_pr + "Combine.pdf")
    merger.close()
#-----------------------------------------printing close-------------------------------
    path20 = r'E:\IWOC\SOURCE' 
    target = r'E:\IWOC\TEMP' 

    for i in move_files:
        src_path = os.path.join(path20, i)
        dst_path = os.path.join(target, i)
        os.rename(src_path, dst_path)
    print('Files Moved................')


    endnow = datetime.now()
    end_time = endnow.strftime("%H:%M:%S")
    # print("Current Time ====================================================", end_time)

    import PyPDF2
    file = open(final_pr + 'Combine.pdf', 'rb')
    readpdf = PyPDF2.PdfFileReader(file)
    totalpages = readpdf.numPages

    with open(r"E:\\IWOC\\LOG_FILES\\bkrcc.txt", "r") as in_file:
        lines2 = in_file.readlines()
        count = 0
        for linew in lines2:
            if 'CUSTOMER NAME' in linew:
                count += 1
    today = date.today()    
    user = DetailActivity.objects.last()
    # print(user,'useerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
    data = History.objects.create(Date = str(today),Start = str(start_time),Finish=str(end_time),User = str(user) ,Product = 'KKK', File= 'BKRCC',Status = 'Enable',Log = str(count),ActiveCount = str(total_clients),Page = str(totalpages),Impression  = 'DONE')


