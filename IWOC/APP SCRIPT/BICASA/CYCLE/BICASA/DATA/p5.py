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
with open(r'C:\Users\Rahul\Desktop\BICASA\Copy of SA20250931.txt') as file:
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

total_date_list = []
len_list = []
total_credit=[]
total_debit=[]
monthly_average=[]
total_bal = []
bal = []
with open(r'C:\Users\Rahul\Desktop\BICASA\Copy of SA20250931.txt') as file:
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
with open(r'C:\Users\Rahul\Desktop\BICASA\Copy of SA20250931.txt') as file:
        c=-1
        date_start_line_number=[]
        total_debit=[]
        for line in file:
            c=c+1
            line=line.strip()
            if line.startswith('DATE    DESCRIPTION  '):
                date_start_line_number.append(c)
        date_start_line_number.append(total_lines)
        print(date_start_line_number,'iiiiiii')
with open(r'C:\Users\Rahul\Desktop\BICASA\Copy of SA20250931.txt') as file:
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
        print(start_date_list,len(start_date_list))



with open(r'C:\Users\Rahul\Desktop\BICASA\Copy of SA20250931.txt') as file:
        lines=file.readlines()
        total_debit=[]
        total_credit=[]
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
                        total_debit.append(line1[26:50])     
                        flag1='True'  
                    if 'TOTAL CREDIT' in line2:
                        total_credit.append(line2[26:50])     
                        flag2='True'  
                    if 'MONTHLY AVERAGE' in line3:
                        monthly_avg.append(line3[26:50])     
                        flag3='True'  

            if flag1=='False':
                total_debit.append('Test')              
            if flag1=='False':
                total_credit.append('Test')

            if flag1=='False':
                monthly_avg.append('Test')              
            if c==lenght:
                break
            a=b
            b=date_start_line_number[c]
            c=c+1
                    

#-----------------------------------------------------------------------------------
with open(r'C:\Users\Rahul\Desktop\BICASA\Copy of SA20250931.txt') as file:
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
            print(a,b)
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
                    date_list.append(line1[0:8])
                    debit.append(line1[67:72])
                    bal.append(line1[109:119])
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

            len_list.append(len(date_list))
        total_date_list.append(date_list)
        total_desc0.append(desc0)
        total_desc1.append(desc1)
        total_desc2.append(desc2)
        total_desc3.append(desc3)
        total_debit.append(debit)
        total_bal.append(bal)

        print(total_desc0,len(total_desc0),'desc0')
        print('--------------------------------------')
        print(total_desc1,len(total_desc1),'desc1')
        print('--------------------------------------')
        print(total_desc2,len(total_desc2),'desc2')
        print(total_desc3,len(total_desc3),'desc3')

        # total_date_list.pop()
        # total_bal.pop()
        # total_credit.pop()
        # total_debit.pop()
        # total_desc0.pop()
        # total_desc1.pop()
        # total_desc2.pop()
        total_desc3.pop()
        # total_desc4.pop()

        print(total_date_list,'d',len(total_date_list))
        maxList1=max(len_list)
        for item in total_date_list:               
            while len(item) < maxList1:   
                item.append('Test')
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
c = 1

#-----------------------------function with emailids------------------------------
c=1
for i in range(0,Total_email_accounts):
    # print(c,client_name[i])
    c=c+1
    if account_no[i] in email_account_no: 
        pdf.add_page()
        pdf.image('Logo_color.jpg',10,15,60)
        pdf.image('Logo_color2.jpg',160,15,33)
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

        if 'Test' not in bal_bf[i]:
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

            #--------------------------------------------INSERTING 1ST TABLE DATA OF 1ST PAGE-----------------
            v11  = 15
            v2 = 120
            v13 = 15
            v4 = 135

            v21 = 40 
            v23 = 40

            v31 = 110 
            v33 = 110

            v41 = 140 
            v43 = 140

            v51 = 170 
            v53 = 170

            v61 = 195 
            v63 = 195

            d1 = 151
            d2 = 152
            d3 = 153
            d4 = 154
            d5 = 155

            h1 =  15
            h2 =  136
            h3 = 195
            h4 = 136

            pdf.set_line_width(0.01)
            pdf.line(15,120,195,120)                          #  horizontal line bal bf
            
            pdf.set_line_width(0.01)
            pdf.line(15,115, 15, 120)                       # 1  st vertical line bal bf
            pdf.line(195,115, 195, 120)                       # 2 vertical line  bal bf

            pdf.ln(1)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(30)
            pdf.cell(70,144,txt = 'BAL B/F')
            pdf.set_font('Arial', '', 9)
            pdf.cell(65)
            pdf.cell(70,144,txt = str(bal_bf[i]))
               
            for j in range(0,9):
                if total_date_list[i][j] != 'Test':
                    pdf.set_line_width(0.01)
                    pdf.line(v11,v2, v13, v4)                       # 1 vertical line
                    pdf.line(v21,v2, v23, v4)                       # 2 vertical line
                    pdf.line(v31,v2, v33, v4)                       # 3 vertical line
                    pdf.line(v41,v2, v43, v4)                       # 4 vertical line
                    pdf.line(v51,v2, v53, v4)                       # 5 vertical line
                    pdf.line(v61,v2, v63, v4)                       # 6 vertical line

                    pdf.ln(2)
                    pdf.cell(10)
                    pdf.cell(10,d1,txt = str(total_date_list[i][j]))

                    pdf.cell(10)
                    pdf.cell(10,d1,txt = ' 9031 IB DuitNow')

                    pdf.cell(80)
                    pdf.cell(10,d1,txt = str(debit[j]))

                    pdf.cell(35)
                    pdf.cell(10,d1,txt = str(bal[j]))    

                    pdf.ln(2)
                    pdf.cell(30)
                    pdf.set_font('Arial','',8)
                    pdf.cell(20,d2,txt = 'TUAN SULAIMAN AKHLAKEN BIN SADIQ SEGARAG')
                                                
                    pdf.ln(2)                                              
                    pdf.cell(30)
                    pdf.cell(10,d3,txt = 'fav')                              

                    pdf.ln(2)        
                    pdf.cell(30)
                    pdf.cell(10,d4,txt = 'WAN NORFAIZAH')   

                    pdf.ln(2)                     
                    pdf.cell(30)
                    pdf.cell(10,d5,txt = '9804002')

                    pdf.line(h1,h2,h3,h4)    

                    d1 = d1 + 15.5   
                    d2 = d2  + 15.5
                    d3 = d3  + 15.5
                    d4 = d4  + 15.5
                    d5 = d5  + 15.5
                    v2 = v4  
                    v4 = v4 + 18.2

                    h2 = h2 + 18
                    h4 = h2 
                    if j == 8:
                        pdf.add_page()
            if j==8:
                v11  = 15
                v2 = 12
                v13 = 15
                v4 = 30

                v21 = 40 
                v23 = 40

                v31 = 110 
                v33 = 110

                v41 = 140 
                v43 = 140

                v51 = 170 
                v53 = 170

                v61 = 195 
                v63 = 195

                d1 = 12
                d2 = 13
                d3 = 14
                d4 = 15
                d5 = 16

                h1 =  15
                h2 =  12
                h3 = 195
                h4 = 12

                # pdf.line(h1,h2,h3,h4)    
                
                for j in range(9,maxList1):
                    if total_date_list[i][j] != 'Test':
                        # print(i,j,'oooooooooooooooooo')
                        pdf.set_line_width(0.01)
                        pdf.line(v11,v2, v13, v4)                       # 1 vertical line
                        pdf.line(v21,v2, v23, v4)                       # 2 vertical line
                        pdf.line(v31,v2, v33, v4)                       # 3 vertical line
                        pdf.line(v41,v2, v43, v4)                       # 4 vertical line
                        pdf.line(v51,v2, v53, v4)                       # 5 vertical line
                        pdf.line(v61,v2, v63, v4)                       # 6 vertical line

                        pdf.ln(2)
                        pdf.cell(10)
                        pdf.cell(10,d1,txt = str(total_date_list[i][j]))

                        pdf.cell(10)
                        pdf.cell(10,d1,txt = ' 9031 IB DuitNow')

                        pdf.cell(80)
                        pdf.cell(10,d1,txt = str(debit[j]))

                        pdf.cell(35)
                        pdf.cell(10,d1,txt = str(bal[j]))    

                        pdf.ln(2)
                        pdf.cell(30)
                        pdf.set_font('Arial','',8)
                        pdf.cell(20,d2,txt = 'TUAN SULAIMAN AKHLAKEN BIN SADIQ SEGARAG')
                                                    
                        pdf.ln(2)                                              
                        pdf.cell(30)
                        pdf.cell(10,d3,txt = 'fav')                              

                        pdf.ln(2)        
                        pdf.cell(30)
                        pdf.cell(10,d4,txt = 'WAN NORFAIZAH')   

                        pdf.ln(2)                     
                        pdf.cell(30)
                        pdf.cell(10,d5,txt = '980400200000000')

                        h2 = h2 + 18
                        h4 = h2 

                        pdf.line(h1,h2,h3,h4)    

                        d1 = d1 + 15.5   
                        d2 = d2  + 15.5
                        d3 = d3  + 15.5
                        d4 = d4  + 15.5
                        d5 = d5  + 15.5
                        v2 = v4  
                        v4 = v4 + 18.2

                        # if j == maxList1:
                        #     break
        else:
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

            #--------------------------------------------INSERTING 1ST TABLE DATA OF 1ST PAGE-----------------
            v11  = 15
            v2 = 115
            v13 = 15
            v4 = 133


            v21 = 40 
            v23 = 40

            v31 = 110 
            v33 = 110

            v41 = 140 
            v43 = 140

            v51 = 170 
            v53 = 170

            v61 = 195 
            v63 = 195

            d1 = 143
            d2 = 147
            d3 = 150
            d4 = 152
            d5 = 154

            h1 =  15
            h2 =  134
            h3 = 195
            h4 = 134

            for j in range(0,9):
                if total_date_list[i][j] != 'Test':
                    pdf.set_line_width(0.01)
                    pdf.line(v11,v2, v13, v4)                       # 1 vertical line
                    pdf.line(v21,v2, v23, v4)                       # 2 vertical line
                    pdf.line(v31,v2, v33, v4)                       # 3 vertical line
                    pdf.line(v41,v2, v43, v4)                       # 4 vertical line
                    pdf.line(v51,v2, v53, v4)                       # 5 vertical line
                    pdf.line(v61,v2, v63, v4)                       # 6 vertical line

                    pdf.ln(2)
                    pdf.cell(10)
                    pdf.cell(10,d1,txt = str(total_date_list[i][j]))

                    pdf.cell(10)
                    pdf.cell(10,d1,txt = ' 9031 IB DuitNow')

                    pdf.cell(80)
                    pdf.cell(10,d1,txt = str(debit[j]))

                    pdf.cell(30)
                    pdf.cell(10,d1,txt = str(bal[j]))    

                    pdf.ln(2)
                    pdf.cell(30)
                    pdf.set_font('Arial','',8)
                    pdf.cell(20,d2,txt = 'TUAN SULAIMAN AKHLAKEN BIN SADIQ SEGARAG')
                                                
                    pdf.ln(2)                                              
                    pdf.cell(30)
                    pdf.cell(10,d3,txt = 'fav')                              

                    pdf.ln(2)        
                    pdf.cell(30)
                    pdf.cell(10,d4,txt = 'WAN NORFAIZAH')   

                    pdf.ln(2)                     
                    pdf.cell(30)
                    pdf.cell(10,d5,txt = '9804002')

                    pdf.line(h1,h2,h3,h4)    

                    d1 = d1 + 16.5    
                    d2 = d2  + 16.5
                    d3 = d3  + 16.5
                    d4 = d4  + 16.5
                    d5 = d5  + 16.5
                    v2 = v4  
                    v4 = v4 + 18.2

                    h2 = h2 + 18
                    h4 = h2 
                    if j == 8:
                        pdf.add_page()
                        # print(j,'jjj')
            if j==8:
                v11  = 15
                v2 = 12
                v13 = 15
                v4 = 12

                v21 = 40 
                v23 = 40

                v31 = 110 
                v33 = 110

                v41 = 140 
                v43 = 140

                v51 = 170 
                v53 = 170

                v61 = 195 
                v63 = 195

                d1 = 12
                d2 = 13
                d3 = 14
                d4 = 15
                d5 = 16

                h1 =  15
                h2 =  12
                h3 = 195
                h4 = 12
                # pdf.line(h1,h2,h3,h4)
                pdf.set_line_width(0.01)
                
                pdf.set_line_width(0.01)
                pdf.line(v11,v2, v13, v4)                       # 1 vertical line
                pdf.line(v21,v2, v23, v4)                       # 2 vertical line
                pdf.line(v31,v2, v33, v4)                       # 3 vertical line
                pdf.line(v41,v2, v43, v4)                       # 4 vertical line
                pdf.line(v51,v2, v53, v4)                       # 5 vertical line
                pdf.line(v61,v2, v63, v4)                       # 6 vertical line

                for j in range(9,maxList1):
                    if total_date_list[i][j] != 'Test':
                        pdf.set_line_width(0.01)
                        v2 = v4  
                        v4 = v4 + 18.2

                        pdf.line(v11,v2, v13, v4)                       # 1 vertical line
                        pdf.line(v21,v2, v23, v4)                       # 2 vertical line
                        pdf.line(v31,v2, v33, v4)                       # 3 vertical line
                        pdf.line(v41,v2, v43, v4)                       # 4 vertical line
                        pdf.line(v51,v2, v53, v4)                       # 5 vertical line
                        pdf.line(v61,v2, v63, v4)                       # 6 vertical line

                        pdf.ln(2)
                        pdf.cell(10)
                        pdf.cell(10,d1,txt = str(total_date_list[i][j]))

                        pdf.cell(10)
                        pdf.cell(10,d1,txt = ' 9031 IB DuitNow')

                        pdf.cell(80)
                        pdf.cell(10,d1,txt = str(debit[j]))

                        pdf.cell(35)
                        pdf.cell(10,d1,txt = str(bal[j]))    

                        pdf.ln(2)
                        pdf.cell(30)
                        pdf.set_font('Arial','',8)
                        pdf.cell(20,d2,txt = 'TUAN SULAIMAN AKHLAKEN BIN SADIQ SEGARAG')
                                                    
                        pdf.ln(2)                                              
                        pdf.cell(30)
                        pdf.cell(10,d3,txt = 'fav')                              

                        pdf.ln(2)        
                        pdf.cell(30)
                        pdf.cell(10,d4,txt = 'WAN NORFAIZAH')   

                        pdf.ln(2)                     
                        pdf.cell(30)
                        pdf.cell(10,d5,txt = '9804002')
                        h2 = h2 + 18
                        h4 = h2 
               
                        pdf.line(h1,h2,h3,h4)    

                        d1 = d1 + 15.5   
                        d2 = d2  + 15.5
                        d3 = d3  + 15.5
                        d4 = d4  + 15.5
                        d5 = d5  + 15.5

pdf.output('Email1.pdf')

#-----------------------------function with emailids--------------------------
pdf = FPDF()
c = 1 
for i in range(0,Total_non_email_account):
    if account_no[i] not in  email_account_no:
        # print(i)   
        pdf.add_page()
        pdf.image('Logo_color.jpg',10,15,60)
        pdf.image('Logo_color2.jpg',160,15,33)
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
        print(bal_bf,'bal')
            #-----------------------------------INSERTING 2ND PAGE TABLE-------------------------------------
        if 'Test' not in bal_bf[i]:
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

            #--------------------------------------------INSERTING 1ST TABLE DATA OF 1ST PAGE-----------------
            v11  = 15
            v2 = 120
            v13 = 15
            v4 = 135

            v21 = 40 
            v23 = 40

            v31 = 110 
            v33 = 110

            v41 = 140 
            v43 = 140

            v51 = 170 
            v53 = 170

            v61 = 195 
            v63 = 195

            d1 = 151
            d2 = 152
            d3 = 153
            d4 = 154
            d5 = 155

            h1 =  15
            h2 =  136
            h3 = 195
            h4 = 136

            pdf.set_line_width(0.01)
            pdf.line(15,120,195,120)                          #  horizontal line bal bf
            
            pdf.set_line_width(0.01)
            pdf.line(15,115, 15, 120)                       # 1  st vertical line bal bf
            pdf.line(195,115, 195, 120)                       # 2 vertical line  bal bf

            pdf.ln(1)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(30)
            pdf.cell(70,144,txt = 'BAL B/F')
            pdf.set_font('Arial', '', 9)
            pdf.cell(65)
            pdf.cell(70,144,txt = str(bal_bf[i]))
               
            for j in range(0,9):
                if total_date_list[i][j] != 'Test':
                    pdf.set_line_width(0.01)
                    pdf.line(v11,v2, v13, v4)                       # 1 vertical line
                    pdf.line(v21,v2, v23, v4)                       # 2 vertical line
                    pdf.line(v31,v2, v33, v4)                       # 3 vertical line
                    pdf.line(v41,v2, v43, v4)                       # 4 vertical line
                    pdf.line(v51,v2, v53, v4)                       # 5 vertical line
                    pdf.line(v61,v2, v63, v4)                       # 6 vertical line

                    pdf.ln(2)
                    pdf.cell(10)
                    pdf.cell(10,d1,txt = str(total_date_list[i][j]))

                    pdf.cell(10)
                    pdf.cell(10,d1,txt = ' 9031 IB DuitNow')

                    pdf.cell(80)
                    pdf.cell(10,d1,txt = str(debit[j]))

                    pdf.cell(35)
                    pdf.cell(10,d1,txt = str(bal[j]))    

                    pdf.ln(2)
                    pdf.cell(30)
                    pdf.set_font('Arial','',8)
                    pdf.cell(20,d2,txt = 'TUAN SULAIMAN AKHLAKEN BIN SADIQ SEGARAG')
                                                
                    pdf.ln(2)                                              
                    pdf.cell(30)
                    pdf.cell(10,d3,txt = 'fav')                              

                    pdf.ln(2)        
                    pdf.cell(30)
                    pdf.cell(10,d4,txt = 'WAN NORFAIZAH')   

                    pdf.ln(2)                     
                    pdf.cell(30)
                    pdf.cell(10,d5,txt = '9804002')

                    pdf.line(h1,h2,h3,h4)    

                    d1 = d1 + 15.5   
                    d2 = d2  + 15.5
                    d3 = d3  + 15.5
                    d4 = d4  + 15.5
                    d5 = d5  + 15.5
                    v2 = v4  
                    v4 = v4 + 18.2

                    h2 = h2 + 18
                    h4 = h2 
                    if j == 8:
                        pdf.add_page()
            if j==8:
                v11  = 15
                v2 = 12
                v13 = 15
                v4 = 30

                v21 = 40 
                v23 = 40

                v31 = 110 
                v33 = 110

                v41 = 140 
                v43 = 140

                v51 = 170 
                v53 = 170

                v61 = 195 
                v63 = 195

                d1 = 12
                d2 = 13
                d3 = 14
                d4 = 15
                d5 = 16

                h1 =  15
                h2 =  12
                h3 = 195
                h4 = 12
                
                for j in range(9,maxList1):
                    if total_date_list[i][j] != 'Test':
                        pdf.set_line_width(0.01)
                        pdf.line(v11,v2, v13, v4)                       # 1 vertical line
                        pdf.line(v21,v2, v23, v4)                       # 2 vertical line
                        pdf.line(v31,v2, v33, v4)                       # 3 vertical line
                        pdf.line(v41,v2, v43, v4)                       # 4 vertical line
                        pdf.line(v51,v2, v53, v4)                       # 5 vertical line
                        pdf.line(v61,v2, v63, v4)                       # 6 vertical line

                        pdf.ln(2)
                        pdf.cell(10)
                        pdf.cell(10,d1,txt = str(total_date_list[i][j]))

                        pdf.cell(10)
                        pdf.cell(10,d1,txt = ' 9031 IB DuitNow')

                        pdf.cell(80)
                        pdf.cell(10,d1,txt = str(debit[j]))

                        pdf.cell(35)
                        pdf.cell(10,d1,txt = str(bal[j]))    

                        pdf.ln(2)
                        pdf.cell(30)
                        pdf.set_font('Arial','',8)
                        pdf.cell(20,d2,txt = 'TUAN SULAIMAN AKHLAKEN BIN SADIQ SEGARAG')
                                                    
                        pdf.ln(2)                                              
                        pdf.cell(30)
                        pdf.cell(10,d3,txt = 'fav')                              

                        pdf.ln(2)        
                        pdf.cell(30)
                        pdf.cell(10,d4,txt = 'WAN NORFAIZAH')   

                        pdf.ln(2)                     
                        pdf.cell(30)
                        pdf.cell(10,d5,txt = '980400200000000')

                        h2 = h2 + 18
                        h4 = h2 

                        pdf.line(h1,h2,h3,h4)    

                        d1 = d1 + 15.5   
                        d2 = d2  + 15.5
                        d3 = d3  + 15.5
                        d4 = d4  + 15.5
                        d5 = d5  + 15.5
                        v2 = v4  
                        v4 = v4 + 18.2
        
        else:
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

            #--------------------------------------------INSERTING 1ST TABLE DATA OF 1ST PAGE-----------------
            v11  = 15
            v2 = 115
            v13 = 15
            v4 = 133


            v21 = 40 
            v23 = 40

            v31 = 110 
            v33 = 110

            v41 = 140 
            v43 = 140

            v51 = 170 
            v53 = 170

            v61 = 195 
            v63 = 195

            d1 = 143
            d2 = 147
            d3 = 150
            d4 = 152
            d5 = 154

            h1 =  15
            h2 =  134
            h3 = 195
            h4 = 134
            for j in range(0,9):
                if total_date_list[i][j] != 'Test':
                    pdf.set_line_width(0.01)
                    pdf.line(v11,v2, v13, v4)                       # 1 vertical line
                    pdf.line(v21,v2, v23, v4)                       # 2 vertical line
                    pdf.line(v31,v2, v33, v4)                       # 3 vertical line
                    pdf.line(v41,v2, v43, v4)                       # 4 vertical line
                    pdf.line(v51,v2, v53, v4)                       # 5 vertical line
                    pdf.line(v61,v2, v63, v4)                       # 6 vertical line

                    pdf.ln(2)
                    pdf.cell(10)
                    pdf.cell(10,d1,txt = str(total_date_list[i][j]))

                    pdf.cell(10)
                    pdf.cell(10,d1,txt = ' 9031 IB DuitNow')

                    pdf.cell(80)
                    pdf.cell(10,d1,txt = str(total_debit[i][j]))

                    pdf.cell(30)
                    pdf.cell(10,d1,txt = str(total_bal[i][j]))    

                    pdf.ln(2)
                    pdf.cell(30)
                    pdf.set_font('Arial','',8)
                    pdf.cell(20,d2,txt = 'TUAN SULAIMAN AKHLAKEN BIN SADIQ SEGARAG')
                                                
                    pdf.ln(2)                                              
                    pdf.cell(30)
                    pdf.cell(10,d3,txt = 'fav')                              

                    pdf.ln(2)        
                    pdf.cell(30)
                    pdf.cell(10,d4,txt = 'WAN NORFAIZAH')   

                    pdf.ln(2)                     
                    pdf.cell(30)
                    pdf.cell(10,d5,txt = '9804002888888888')

                    pdf.line(h1,h2,h3,h4)    

                    d1 = d1 + 16.5    
                    d2 = d2  + 16.5
                    d3 = d3  + 16.5
                    d4 = d4  + 16.5
                    d5 = d5  + 16.5
                    v2 = v4  
                    v4 = v4 + 18.2

                    h2 = h2 + 18
                    h4 = h2 
                    if j == 8:
                        pdf.add_page()
                        # print(j,'jjj')

            if total_debit[i] != 'Test':
                pdf.set_line_width(0.01)                   
                pdf.line(15,h2-20,15,h2+5)                             # 1st vertical line of total table  
                pdf.line(195,h2-20,195,h2+5)                           # 2nd vertical line of total tabel

                # pdf.line(15,259,195,259)                          # horizontal line wont work after 260 

                pdf.set_font('Arial','B',8)
                pdf.cell(-20)
                pdf.cell(10,h2+20,txt = 'TOTAL DEBIT')

                pdf.cell(30)
                pdf.cell(20,h2+20,txt = str(total_debit[i]))

                pdf.ln(1)
                pdf.cell(20)
                pdf.cell(10,h2+25,txt = 'TOTAL CREDIT')
                
                pdf.cell(30)
                pdf.cell(20,h2+25,txt = str(total_credit[i]))

                pdf.ln(1)
                pdf.cell(20)
                pdf.cell(10,h2+30,txt = 'MONTHLY AVERAGE')
                
                pdf.cell(30)
                pdf.cell(40,h2+30,txt = str(monthly_avg[i]))

                pdf.set_fill_color(r=0,g=0,b=0)
                pdf.set_line_width(0.01)
                pdf.rect(x = 15 , y = h2+5 , w = 180 , h = 4, style = 'DF')      
                pdf.ln(1)
                pdf.set_font('Arial','',7.2)
                pdf.cell(4)
                pdf.cell(10,h2+60,txt ='Sekiranya anda mendapati sebarang perbezaan, sila maklumkan kepada pihak Bank di dalam tempoh 14 hari daripada tarikh penyata ini. Jika tiada perbezaan')   
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h2+64 , txt = 'penyata ini akan dianggap betul. ')
                pdf.set_font('Arial','I',7.1)
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h2+68.8,txt= 'If you note any discrepancies, please advise the Bank within 14 days from the date of this statement, otherwise this account statement is considered to be correct. ')
                pdf.set_font('Arial','',7.2)
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h2+73.8,txt = 'Untuk pertanyaan, ajukan kepada / For enquiries, please channel to: ')
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h2+78.8,txt = 'Jabatan Khidmat Pelanggan (Customer Care Department), Tingkat 17, Menara Bank Islam, No 22, Jalan Perak, 50450 Kuala Lumpur')
                pdf.ln(1)
                pdf.cell(4)
                pdf.cell(10,h2+84,txt = 'Tel: 03-26 900 900 / Faks: 03-2782 1337. Emel / Email: contactcenter@bankislam.com.my')

            if j==8:
                v11  = 15
                v2 = 16
                v13 = 15
                v4 = 16

                v21 = 40 
                v23 = 40

                v31 = 110 
                v33 = 110

                v41 = 140 
                v43 = 140

                v51 = 170 
                v53 = 170

                v61 = 195 
                v63 = 195

                d1 = 0
                d2 = 1
                d3 = 2
                d4 = 3
                d5 = 4

                h1 =  15
                h2 =  12
                h3 = 195
                h4 = 12
                # pdf.line(h1,h2,h3,h4)
                pdf.set_line_width(0.01)
                # pdf.line(15,120,195,120)                          #  horizontal line bal bf
                
                pdf.set_line_width(0.01)
                # pdf.line(15,115, 15, 120)                       # 1  st vertical line bal bf
                # pdf.line(195,115, 195, 120)                       # 2 vertical line  bal bf
                pdf.line(v11,v2, v13, v4)                       # 1 vertical line
                pdf.line(v21,v2, v23, v4)                       # 2 vertical line
                pdf.line(v31,v2, v33, v4)                       # 3 vertical line
                pdf.line(v41,v2, v43, v4)                       # 4 vertical line
                pdf.line(v51,v2, v53, v4)                       # 5 vertical line
                pdf.line(v61,v2, v63, v4)                       # 6 vertical line
                
                for j in range(9,maxList1):
                    if total_date_list[i][j] != 'Test':
                        pdf.set_line_width(0.01)
                        v2 = v4  
                        v4 = v4 + 18

                        pdf.line(v11,v2, v13, v4)                       # 1 vertical line
                        pdf.line(v21,v2, v23, v4)                       # 2 vertical line
                        pdf.line(v31,v2, v33, v4)                       # 3 vertical line
                        pdf.line(v41,v2, v43, v4)                       # 4 vertical line
                        pdf.line(v51,v2, v53, v4)                       # 5 vertical line
                        pdf.line(v61,v2, v63, v4)                       # 6 vertical line

                        pdf.ln(2)
                        pdf.cell(10)
                        pdf.cell(10,d1,txt = str(total_date_list[i][j]))

                        pdf.cell(10)
                        pdf.cell(10,d1,txt = ' 9031 IB DuitNow')

                        pdf.cell(80)
                        pdf.cell(10,d1,txt = str(debit[j]))

                        pdf.cell(35)
                        pdf.cell(10,d1,txt = str(bal[j]))    

                        pdf.ln(2)
                        pdf.cell(30)
                        pdf.set_font('Arial','',8)
                        pdf.cell(20,d2,txt = 'TUAN SULAIMAN AKHLAKEN BIN SADIQ SEGARAG')
                                                    
                        pdf.ln(2)                                              
                        pdf.cell(30)
                        pdf.cell(10,d3,txt = 'fav')                              

                        pdf.ln(2)        
                        pdf.cell(30)
                        pdf.cell(10,d4,txt = 'WAN NORFAIZAH')   

                        pdf.ln(2)                     
                        pdf.cell(30)
                        pdf.cell(10,d5,txt = '11111')
                        h2 = h2 + 20
                        h4 = h2 
               
                        pdf.line(h1,h2,h3,h4)    

                        d1 = d1 + 15.5   
                        d2 = d2  + 15.5
                        d3 = d3  + 15.5
                        d4 = d4  + 15.5
                        d5 = d5  + 15.5 



                

    
print(Total_non_email_account,'t')
pdf.output('Nonemail1.pdf')
# print(maxList1,'Maxlist')    
# print(total_date_list)               

# # #---- added to create file--------------------------------------------------------
# # inputpdf = PdfFileReader(open("nonemail.pdf", "rb"))
# # for i in range(inputpdf.numPages):
# #     output = PdfFileWriter()

# #     pasw = []
# #     pasww = email[i][0:5]
# #     print(pasww)

    
# #     output.addPage(inputpdf.getPage(i))
# #     name = email[i][0:2]  + email[i][6:11] + '300925'
  
# #     with open("SA1-XXXXX-%s.pdf" % name , "wb") as outputStream:
# #         output.write(outputStream)

# #  14014021105894