from turtle import pen
from PyPDF2 import PdfFileWriter, PdfFileReader
import pandas as pd
from fpdf import FPDF
import docx
import pandas as pd

 #----------------------- data captured from word file-----------------
doc = docx.Document(r'Copy of DD7405F.docx')
all_docs = doc.paragraphs

email_id = []
Account_no = []

for i in all_docs:
    a = i.text
    if '@' in a:
        email_id.append(a[20:52])
        Account_no.append(a[8:19])
    
df1 = pd.DataFrame()
df1['account_no'] = Account_no
df1['email_id'] = email_id


#---------------email data ends here-----
with open(r'C:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Copy of SA20250931.txt') as file:
    k=file.readlines()
    total_lines=len(k)
    total_accounts=0
    for i in k:
        i=i.strip()
        if i.startswith('.'):
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
with open(r'C:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Copy of SA20250931.txt') as file:
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
            l7=l7.strip()
            add4.append(l7[0:15])
            account_no.append(l7[109:120])
            l8=file.readline()
            l9=file.readline()
            l9=l9[89:115]
            l9=l9.strip()
            branch.append(l9)
#-----------------------Total debit, credit----------------------------------------
#------In source file we have keyword DATE DESCRIPTION which is start of transation, 
# -----Here , we have captured start location of this keyword -----------------------------------
with open(r'C:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Copy of SA20250931.txt') as file:
        c=-1
        date_start_line_number=[]
        total_debit=[]
        for line in file:
            c=c+1
            line=line.strip()
            if line.startswith('DATE    DESCRIPTION  '):
                date_start_line_number.append(c)
        date_start_line_number.append(total_lines)
        # print(date_start_line_number,'iiiiiii')
with open(r'C:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Copy of SA20250931.txt') as file:
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
                    # print(line,num,'---')
                    start_date_list.append(num)                
        # print(start_date_list,len(start_date_list))



with open(r'C:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Copy of SA20250931.txt') as file:
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
        c=2
        lenght=len(date_start_line_number)
        # print(lenght,'length')
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
                    # print(line2)
                    if 'TOTAL DEBIT' in line1:
                        msg_total_debit.append(line1[25:50])     
                        flag1='True'  
                    if 'TOTAL CREDIT' in line2:
                        msg_total_credit.append(line2[25:50])     
                        flag2='True'  
                    if 'MONTHLY AVERAGE' in line3:
                        # monthly_avg.append(line3[26:50])     
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
print(msg_total_debit,'msggggg')

#-----------------------------------------------------------------------------------
with open(r'C:\IWOC\APP SCRIPT\BICASA\CYCLE\BICASA\DATA\Copy of SA20250931.txt') as file:
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
            bal_bf.append('Test')
            
            a=date_start_line_number[i]
            b=date_start_line_number[i+1]
            # print(a,b)
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
                    desc0.append(line1[0:8])
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
        # total_credit.pop()
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
print('Total Accounts email-->',Total_email_accounts)
print('Total Accounts without email-->',Total_non_email_account)
pdf = FPDF()

a1,b1,c1,d1 = [2,100,8,100] # 1st line
a10,b10,c10,d10 = [2,118,8,118]  # 10 th line
a,b,c,d = [2,104,8,104] # bs1 + 2 bs2
d01,d02,d03,d04 = [2,108,8,108] # dgr iloc 5 line 
gm1,gm2,gm3,gm4 = [2,112,8,112] # Gm1 7 line
gm21,gm22,gm31,gm41 = [2,114,8,114] # gm2 8 line
p1, p2, p3, p4 = [2,116,8,116] 
pr1,pr2,pr3,pr4 = [200,208,206,208]
rbs1,rbs2,rbs3,rbs4 = [200,220,206,220] # BM right omr 1st line
reoc1,reoc2,reoc3,reoc4 = [200,218,206,218] # righ 2nd line EOC like DGR
bsr1,bsr2,bsr3,bsr4 = [200,214,206,214] # right third BS1
bs1 = 3
bs2 = 5
bs12 = 7
GM1  = 7
GM2 = 13
gm12 = 19
dgr = 1
data_page = 1
p = 0
page2 = 1
reoc = 1 # right eoc page val
rparity = 0

#-----------------------------function without emailids------------------------------
c=1
for i in range(0,Total_non_email_account):
    c=c+1
    if account_no[i] not in email_account_no: 
        print(account_no[i],'acc')
        pdf.add_page()
        pdf.image('Left_logo.jpg',10,15,60)
        pdf.image('Right_logo.jpg',160,15,33)
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

        if 'Test' in bal_bf[i]:
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
                    if j == 9:
                        pdf.add_page()
                        pdf.set_auto_page_break(auto=False)
                    cc=1

            if msg_total_debit[i] == 'Test':
                pdf.ln(1)
                pdf.set_line_width(0.01)  
                pdf.line(15,h-41,15,h-10)                             # 1st verticl line of total table  
                pdf.line(195,h-41,195,h-10)                           # 2nd vertical line of total tabel

                pdf.set_font('Arial','B',8)
                pdf.cell(20)
                pdf.cell(10,h+20,txt = 'TOTAL DEBIT')

                pdf.cell(30)
                pdf.cell(20,h+20,txt = str(msg_total_debit[i]))

                pdf.ln(1)
                pdf.cell(20)
                pdf.cell(10,h+25,txt = 'TOTAL CREDIT')
                
                pdf.cell(30)
                pdf.cell(20,h+25,txt = str(msg_total_credit[i]))

                pdf.ln(1)
                pdf.cell(20)
                pdf.cell(10,h+30,txt = 'MONTHLY AVERAGE')
                
                # pdf.cell(30)
                # pdf.cell(40,h+30,txt = str(monthly_avg[i][j]))

                pdf.set_fill_color(r=0,g=0,b=0)
                pdf.set_line_width(0.01)
                pdf.rect(x = 15 , y = h-12 , w = 180 , h = 4, style = 'DF')      
                pdf.ln(1)
                pdf.set_font('Arial','',7.2)
                pdf.cell(4)
                pdf.cell(10,h+60,txt ='Sekiranya anda mendapati sebarang perbezaan, sila maklumkan kepada pihak Bank di dalam tempoh 14 hari daripada tarikh penyata ini. Jika tiada perbezaan')   
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h+64 , txt = 'penyata ini akan dianggap betul. ')
                pdf.set_font('Arial','I',7.1)
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h+68.8,txt= 'If you note any discrepancies, please advise the Bank within 14 days from the date of this statement, otherwise this account statement is considered to be correct. ')
                pdf.set_font('Arial','',7.2)
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h+73.8,txt = 'Untuk pertanyaan, ajukan kepada / For enquiries, please channel to: ')
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h+78.8,txt = 'Jabatan Khidmat Pelanggan (Customer Care Department), Tingkat 17, Menara Bank Islam, No 22, Jalan Perak, 50450 Kuala Lumpur')
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h+84,txt = 'Tel: 03-26 900 900 / Faks: 03-2782 1337. Emel / Email: contactcenter@bankislam.com.my')
     
            if msg_total_debit[i] != 'Test':
                pdf.ln(1)
                pdf.set_line_width(0.01)  
                pdf.line(15,h-41,15,h-10)                             # 1st vertical line of total table  
                pdf.line(195,h-41,195,h-10)                           # 2nd vertical line of total tabel

                pdf.set_font('Arial','B',8)
                pdf.cell(20)
                pdf.cell(10,h+20,txt = 'TOTAL DEBIT')

                pdf.cell(30)
                pdf.cell(20,h+20,txt = str(msg_total_debit[i]))
                # print(msg_total_debit,'')

                pdf.ln(1)
                pdf.cell(20)
                pdf.cell(10,h+25,txt = 'TOTAL CREDIT')
                
                pdf.cell(30)
                pdf.cell(20,h+25,txt = str(msg_total_credit[i]))

                pdf.ln(1)
                pdf.cell(20)
                pdf.cell(10,h+30,txt = 'MONTHLY AVERAGE')
                
                # pdf.cell(30)
                # pdf.cell(40,h+30,txt = str(monthly_avg[i][j]))

                pdf.set_fill_color(r=0,g=0,b=0)
                pdf.set_line_width(0.01)
                pdf.rect(x = 15 , y = h-12 , w = 180 , h = 4, style = 'DF')      
                pdf.ln(1)
                pdf.set_font('Arial','',7.2)
                pdf.cell(4)
                pdf.cell(10,h+60,txt ='Sekiranya anda mendapati sebarang perbezaan, sila maklumkan kepada pihak Bank di dalam tempoh 14 hari daripada tarikh penyata ini. Jika tiada perbezaan')   
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h+64 , txt = 'penyata ini akan dianggap betul. ')
                pdf.set_font('Arial','I',7.1)
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h+68.8,txt= 'If you note any discrepancies, please advise the Bank within 14 days from the date of this statement, otherwise this account statement is considered to be correct. ')
                pdf.set_font('Arial','',7.2)
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h+73.8,txt = 'Untuk pertanyaan, ajukan kepada / For enquiries, please channel to: ')
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h+78.8,txt = 'Jabatan Khidmat Pelanggan (Customer Care Department), Tingkat 17, Menara Bank Islam, No 22, Jalan Perak, 50450 Kuala Lumpur')
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h+84,txt = 'Tel: 03-26 900 900 / Faks: 03-2782 1337. Emel / Email: contactcenter@bankislam.com.my')
     
print(Total_non_email_account,'NON_EMAIL ACCOUNTS PDF CREATED')
pdf.output('Non_EmailX.pdf')
#-----------------------------function with emailids--------------------------
pdf = FPDF()
c=1
for i in range(0,Total_email_accounts):
    c=c+1
    if account_no[i] in email_account_no: 
        pdf.add_page()
        pdf.image('Left_logo.jpeg',10,15,60)
        pdf.image('Right_logo.jpeg',160,15,33)
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

        if 'Test' in bal_bf[i]:
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
                    if j == 9:
                        pdf.add_page()
                    cc=1
               
print(Total_email_accounts,'EMAIL ACCOUNTS PDF CREATED')
pdf.output('EmailX.pdf')
