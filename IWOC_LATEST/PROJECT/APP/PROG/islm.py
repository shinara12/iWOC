from fpdf import FPDF
import PyPDF2

def ISLM(request,files1):
    path11 = r'E:\IWOC\SOURCE\\'+ files1
    with open(path11) as file:
        lines = file.readlines()
        total_lines = len(lines)
        print(total_lines)
    with open(path11) as file:
        NULL_DATA = []
        Date1 = []
        Name = []
        Add1 = []
        Add2 = []
        Add3 = []
        Add4 = []
        Account_no = []
        Date2= []
        Bal = []
        city = []
        a1 = []
        a2 = []
        a3 = []
        phone_no = []
        currency = []
        for i in range(0,total_lines-1):
            line = file.readline()
            line = line.split('|')
            Date1.append(line[0])
            Name.append(line[1])
            NULL_DATA.append(line[2])
            Add1.append(line[3])
            Add2.append(line[4])
            Add3.append(line[5])
            Add4.append(line[6])
            Account_no.append(line[7])
            Date2.append(line[8])
            Bal.append(line[9])
            city.append(line[10])
            a1.append(line[11])
            a2.append(line[12])
            a3.append(line[13])
            phone_no.append(line[14])
            currency.append(line[15])
        kk2 = []
        pst = Add4
        for i in range(len(pst)):
            if pst[i] != '':
                a = pst[i].split()
                kk2.append(a[0])
        # print(kk2)
        postcode0 = []
        with open(path11) as file:
            for i in range(0,total_lines-1):
                line = file.readline()
                line = line.split('|')
                if line[4].startswith(('0','1','2','3','4','5','6','7','8','9')) and ',' not in line[4]  and len(line[4].strip()) > 4 and '/' not in line[4]:
                    pst = line[4].split()
                    postcode0.append(pst[0]) 
                elif line[5].startswith(('0','1','2','3','4','5','6','7','8','9')) and ',' not in line[5] and len(line[5].strip()) > 4 and '/' not in line[5]:
                    pst = line[5].split()
                    postcode0.append(pst[0]) 
                elif line[6].startswith(('0','1','2','3','4','5','6','7','8','9')) and ',' not in line[6] and len(line[6].strip()) > 4 and ',' not in line[6]:
                    pst = line[6].split()
                    postcode0.append(pst[0]) 
                else:
                    postcode0.append('00000') 
                
        postcode=[]
        for i in postcode0:
            print(i,'---------------------')
            i = int(i)
            # ----------1-10-----------
            if i>=1000 and i<=2999:
                postcode.append('001')
            elif i>=5000 and i<=6999:
                postcode.append('002')
            elif i>=7000 and i<=7999:
                postcode.append('003')
            elif i>=8000 and i<=8099:
                postcode.append('004')
            elif (i>=8100 and i<=8899) or (i>=9100 and i<=9599) or (i>=9700 and i<=9899) or i==34950:
                postcode.append('005')
            elif i>=9000 and i<=9099 or (i>=9600 and i<=9699):
                postcode.append('006')
            elif i>=10000 and i<=10999 or (i>=11000 and i<=1150) or i==11800 or (i>=13100 and i<=13310) or i==13050 or (i>=14100 and i<=14390):
                postcode.append('007')
            elif i==11600 or i==11700:
                postcode.append('008')
            elif i>=11900 and i<=11999:
                postcode.append('009')
            elif i>=12000 and i<=12300 or (i>=12700 and i<=12990) or (i>=13000 and i<=13020) or i==13400 or i==13800:
                postcode.append('010')
            
            # -----------11-20---------------------
            elif i == 13500 or i == 13600 or i == 13700:
                postcode.append('011')
            elif i>=14000 and i<= 14020 or i == 14400:
                postcode.append('012')
            elif i >= 30000 and i <= 30999:
                postcode.append('013')
            elif i == 31450 or i == 31500 or i == 31650:
                postcode.append('014')
            elif (i >= 31000 and i <= 31100) or i == 31200 or i == 31300 or i == 31350 or (i >= 31550 and i <=31610) or (i >=31700 and i <=32900) or (i >= 33100 and i <= 33500) or (i >= 34100 and i <= 34500) or i == 34800 or i == 34900 or (i >= 35000 and i <= 35999) or (i >= 39000 and i <= 39999):
                postcode.append('015')
            elif i == 31400 or i == 31150 or i ==  31250:
                postcode.append('016')
            elif  (i >= 33000 and i <= 33099) or i == 33600 or i == 33700:
                postcode.append('017') 
            elif (i >= 34000 and i <= 34099) or i == 34600 or i == 34650  or i == 34700 or i == 34750 or i == 34850:
                postcode.append('018')
            elif (i >= 36000 and i <= 36999):
                postcode.append('019')        
            elif i == 40150:
                postcode.append('020')

            # -----------21-30---------------------
            elif i == 40400 or (i>= 40460 and i <= 40690) or i == 42450:
                postcode.append('021')
            elif i == 40000 or i == 40100 or i == 40200 or i == 40300 or i == 40450:
                postcode.append('022')
            elif (i >= 40700 and i <= 40990):
                postcode.append('023')
            elif i == 41000  or i == 41100 or i == 41200 or i == 41250 or (i >= 41500 and i <= 41990):
                postcode.append('024')
            elif i == 40170 or i == 41050 or i == 41150 or i == 41300 or i == 41400 or i == 42100:
                postcode.append('025')
            elif (i >= 42000 and i <=42009) or i == 42920:
                postcode.append('026')
            elif i == 42600 or i == 42700 or (i >=45000 and i <= 45030) or i == 45100:
                postcode.append('027')
            elif i == 42500 or i == 42800 or i == 45800 or (i >= 44000 and  i <= 44300) or i == 48100 or i == 42940 or i == 42960 or i == 45200 or i == 45300 or i == 45400 or i == 45500 or i == 45600 or i == 45700:
                postcode.append('028')
            elif i == 43900 or i == 43950 or i == 64000:
                postcode.append('029')
            elif (i >= 43000 and i <= 43009) or (i >= 43600 and i <= 43650) or (i >= 62000 and i <= 62306):
                postcode.append('030')

            # -----------31-40---------------------
            elif i == 43100 or (i >= 43200 and i <= 43207):
                postcode.append('031')
            elif (i >= 43300 and i <= 43499):
                postcode.append('032')
            elif i == 43500 or i == 43700:
                postcode.append('033')
            elif (i >= 46000 and i <= 46999):
                postcode.append('034')
            elif i == 40160 or i == 47000 or i == 47810 or i == 48050:
                postcode.append('035')
            elif (i >= 47100  and i <= 47190) or i == 42610:
                postcode.append('036')
            elif i == 47200 or (i >= 47300 and i <= 47308):
                postcode.append('037')
            elif i == 47400 or i == 47410 or i == 47800 or i == 47820 or i == 47830:
                postcode.append('038')
            elif (i >= 47500 and i <= 47699):
                postcode.append('039')
            elif i == 48000 or i == 48010 or i == 48020 or (i >= 48200 and i <= 48399):
                postcode.append('40')


            # -----------41-50---------------------
            elif (i >= 62400 and i <= 62688) or i == 62692:
                postcode.append('041')
            elif (i >=42200 and i <= 42300):
                postcode.append('042')
            elif (i >= 43800 and i <= 43809) or (i >= 63000 and i <= 63300):
                postcode.append('043')
            elif (i >= 50000 and i <= 50400):
                postcode.append('044')
            elif (i >= 50500 and i <= 50699):
                postcode.append('045')
            elif (i >= 50450 and i <= 50490):
                postcode.append('046')
            elif (i >= 50700 and i <= 50990):
                postcode.append('047')
            elif (i >= 51000 and i <= 51200) or ( i >= 51700 and i <= 51990):
                postcode.append('048')
            elif i == 52000 or ( i >= 52100 and i <= 52200):
                postcode.append('049')
            elif (i >= 53000 and i <= 53300) or (i >= 53700 and i <= 53990):
                postcode.append('050')

            
            # -----------51-60---------------------
            elif (i >= 54000 and i <= 54200):
                postcode.append('051')
            elif (i >= 55000 and i <= 55300) or (i >= 55700 and i <= 55990):
                postcode.append('052')
            elif (i >= 56000 and i <= 56100):
                postcode.append('053')
            elif (i >= 58000 and i <= 58200) or (i >= 58700 and i <= 58990):
                postcode.append('054')
            elif (i >= 590000 and i <= 59200)  or (i >= 59700 and i <= 59900):
                postcode.append('055')
            elif (i >= 57000 and i <= 57100) or (i >= 57700 and i <= 57990):
                postcode.append('056')
            elif i == 60000:
                postcode.append('057')    
            elif i == 68000:
                postcode.append('058')
            elif i == 68100:
                postcode.append('059')
            elif i == 70000 or (i >= 70100 and i <= 70200) or (i >= 70500  and i <= 70990) or i == 71450 or i == 71770:
                postcode.append('060')


            # -----------61-70---------------------                 
            elif i == 70300 or(i >= 70400 and i <= 70450):
                postcode.append('061')
            elif (i >=71000 and i <=71009) or i == 71010 or i == 72100 or i == 71760 or (i >= 71800 and i <= 71809) or i == 71900 or (i >= 71950 and i <= 71960) or (i >= 72000 and i <= 72009) or (i >=71500 and i <= 71550) or i == 72500 or (i>=73100 and i <= 73500):
                postcode.append('062')
            elif (i >= 71050 and i <= 71409) or (i >= 71600 and i <= 71759) or (i >= 72120 and i <= 72400) or (i >= 73200 and i <= 73400):
                postcode.append('063')
            elif (i >= 75000  and i <= 75260):
                postcode.append('064')
            elif i == 75460 or i == 76100 or i == 76400 or i == 76450:
                postcode.append('065')
            elif i == 77500 or i == 76200 or i == 76300 or i == 78000 or i == 78100 or i == 78200 or i == 78300:
                postcode.append('066')
            elif (i >= 80000  and i <= 80999):
                postcode.append('067')
            elif (i >= 81100 and i <=  81109):
                postcode.append('068')
            elif (i >= 81200  and i <= 81299):
                postcode.append('069')
            elif i == 81300 or i == 81310 or i == 81550 or i == 81560 or i == 81110 or i == 79000 or i == 79100 or i == 79150 or i == 79200 or i== 79250:
                postcode.append('070')
            
            # -----------71-80--------------------- 
            elif (i >= 81700  and i <= 81799):
                postcode.append('071')
            elif (i >= 81000 and i <= 81099) or (i >= 81400 and i <= 81499):
                postcode.append('072')
            elif (i >= 81600 and i <= 81699) or i == 81800 or (i >= 81900 and i <= 81990):
                postcode.append('073')
            elif(i >= 82000  and i <= 82099) or i == 81500:
                postcode.append('074')
            elif (i >= 83000 and i <=  83999 ) or i ==  86400:
                postcode.append('075')
            elif (i >= 84000  and i  <=  84999):
                postcode.append('076')
            elif (i >= 85000 and i <= 85099) or i == 86500:
                postcode.append('077')
            elif (i >= 86000 and i <= 86399) or (i >= 86600 and i <= 86999) or i == 81850:
                postcode.append('078')
            elif(i >= 25000 and i <= 25989) or (i >= 26000 and i <= 26040) or i == 26060:
                postcode.append('079')
            elif i == 25990 or i == 26050 or (i >= 26070 and i <= 26090) or (i >= 26100 and i <= 26999):
                postcode.append('080')

            # -----------81-90--------------------- 
            elif (i >= 27000 and i <= 27699) or (i >= 49000 and i <= 49099):
                postcode.append('081')
            elif (i >= 28000 and i <= 28899) or (i >= 96000 and i <= 69099):
                postcode.append('082')
            elif (i >= 20000 and i <= 21009) or (i >= 21070 and i <= 21090) or (i>=21100 and i <= 21109) or(i >= 24100 and i >= 24109) or (i >= 24200 and i <= 24209):
                postcode.append('083')
            elif (i >= 21010 and i <= 21030) or i == 21060 or (i >= 21200 and i <= 21309) or i == 21450 or i == 21500 or (i >= 22000 and i <= 22020) or (i >= 22100 and i <= 22120) or (i >= 22200 and i <= 22309) or (i >= 23000 and i <= 23050) or (i >= 23100 and i <= 23400):
                postcode.append('084')
            elif i == 21040 or i == 21400 or (i >= 21600 and i <= 21820) or (i >= 24000 and i <= 24009) or (i >= 24050 and i <= 24060) or i == 24300:
                postcode.append('085')
            elif (i >= 15000 and i <= 15999) or i == 16010 or i == 16150:
                postcode.append('086')
            elif (i >= 16020 and i <= 16090) or i == 16100 or (i >= 16200 and i <= 16899) or (i >= 17000 and i <= 17999) or (i >= 18000 and i <= 18999):
                postcode.append('087')
            elif (i >= 87000 and i <= 87999):
                postcode.append('088')
            elif (i >= 88000 and i <= 88899):
                postcode.append('089')
            elif (i >= 89000 and i <=89999):
                postcode.append('090')

            # -----------91-100--------------------- 
            elif (i >= 90000 and i <= 90999):
                postcode.append('091')
            elif (i >= 91000 and i <= 91099) or (i >=  91200 and i <=91399):
                postcode.append('092')
            elif (i >= 91100 and i <= 91199):
                postcode.append('093')
            elif (i >= 93000 and i <= 93049) or (i >=93100 and i <=93300):
                postcode.append('094')
            elif (i >= 93050 and i <= 93099) or (i >=  93350 and i <= 93450):
                postcode.append('095')
            elif(i>= 94000 and i <= 95999):
                postcode.append('096')
            elif (i >= 96000 and i <=  96999):
                postcode.append('097')
            elif (i >= 97000 and i <= 97999):
                postcode.append('098')
            elif (i >= 98000 and i <= 98999 ):
                postcode.append('099')
            else:
                postcode.append('000')
                                                                                                
        print(postcode,'-----postcode')
        count = 1 
        pdf = FPDF()
        for i in range(0,total_lines-1):
            pdf.add_page()
            pdf.set_auto_page_break(auto=False)
            pdf.set_line_width(6)
            pdf.set_draw_color(r=0, g=0, b=0)
            pdf.line(4, 5, 200, 5)         #1st horizontal line
            pdf.line(5, 290,200,290)     #2nd horizontal line 
            pdf.line(4,6,4,290)                         # 1st vertical line
            pdf.line(200,6,200,290)                     # 2nd vertical line    

            pdf.image(r'E:\IWOC\APP SCRIPT\ISLM\CYCLE\ILS\DATA\heading.png',15,9,80)
            pdf.image(r'E:\IWOC\APP SCRIPT\ISLM\CYCLE\ILS\DATA\sidehaeding.png',142,9,50)
            pdf.ln(1)
            pdf.set_font('Arial','I',7)
            pdf.cell(7)
            pdf.cell(10,48,txt = 'Date/Tarikh : ')
            pdf.set_font('Arial','',7)
            pdf.cell(5)
            pdf.cell(10,48,txt = str(Date1[i]))
            pdf.ln(1)
            pdf.set_font('Arial','',7)
            pdf.cell(7)
            pdf.cell(10,60,txt = str(Name[i]))
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,65,txt = str(Add1[i]))
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,70,txt = str(Add2[i]))
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,75,txt = str(Add3[i]))
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,80,txt = str(Add4[i]))

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,110,txt = 'Sir/Madam')
            pdf.set_font('Arial','B',7)
            pdf.cell(148)
            pdf.cell(10,110,txt = 'REMINDER')
            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,115,txt = 'NOTICE ON DORMANT ACCOUNT')
            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,120,txt = 'ACCOUNT NUMBER')
            pdf.cell(42)
            pdf.set_font('Arial','B',7)
            pdf.cell(10,120,txt = ':')
            pdf.set_font('Arial','',7)
            pdf.cell(-7)
            pdf.cell(10,120,txt = str(Account_no[i]))
            pdf.ln(1)
            pdf.set_font('Arial','B',7)
            pdf.cell(7)
            pdf.cell(10,126,txt = 'BALANCE AS AT')
            pdf.set_font('Arial','',7)
            pdf.cell(18)
            pdf.cell(10,126,txt = str(Date2[i]))
            pdf.cell(14)
            pdf.set_font('Arial','B',7)
            pdf.cell(10,126,txt = ':')
            pdf.set_font('Arial','',7)
            pdf.cell(-6)
            pdf.cell(10,126,txt = str(currency[i]))
            pdf.cell(-4)
            pdf.cell(10,126,txt = str(Bal[i]))

            pdf.set_line_width(0.05)
            pdf.line(18,87,190,87)
            pdf.set_font('Arial','',7.2)
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,138,txt = 'Kindly be informed that if a Current Account- /Foreign Currency Current Account-i/Savings Account- (CASA- ) has been inactive for more than twelve (12) ')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,144,txt = 'months, it will be classified as a  Dormant Account. A yearly  Dormant Account fee of RM10.00 or respective foreign currency equivalent shall be charged')
            pdf.ln(1)
            pdf.cell(7)
            pdf.set_font('Arial','',7)
            pdf.cell(10,150,txt = 'for maintenance and if the account remains dormant for seven (7) years or more,the account will be closed and the balance will be transferred to the Registrar')
            pdf.ln(1)
            pdf.cell(7)
            pdf.set_font('Arial','',7.2)
            pdf.cell(10,156,txt = 'of Unclaimed Moneys as stipulated in the Unclaimed Moneys Act 1965(an act relating to the payment of unclaimed moneys into the Federal Consolidated')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,162,txt = 'Fund).')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,172,txt = 'We would like to inform you that your CASA-  account has been classified as a Dormant Account. Please activate your account by performing any deposit')
            pdf.ln(1)
            pdf.cell(7)
            pdf.set_font('Arial','',7.1)
            pdf.cell(10,178,txt = 'or withdrawal transaction over-the-counter within three(3) months from the date of this notice. Should you fail do so, the Dormant Account fee of RM10.00 or ')
            pdf.ln(1)
            pdf.cell(7)
            pdf.set_font('Arial','',7.2)
            pdf.cell(10,184,txt ='respective foreign currency equivalent shall be charged to your account. For accounts with balances of RM10.00 or respective foreign currency equivalent')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,190,txt = 'or less, the account will be closed by the Bank and the balance will be absorbed as service fee.')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,200,txt = 'We apologise for any inconvenience caused and hope you can visit our branch nearest to you for account activation.')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,210,txt = 'Thank you.')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,220,txt = 'Yours faithfully')

            pdf.ln(1)
            pdf.cell(7)
            pdf.set_font('Arial','B',7)
            pdf.cell(10,226,txt = 'MBSB Bank Berhad (Registration No. 200501033981) (716122-P)')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,234,txt = 'Note:')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,240,txt= 'a. This is a computer-generated document. No signature is required.')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,246,txt= 'b. In the event of any discrepancy between the English text and the Bahasa Malaysia translation, the English text will prevail.')

            pdf.set_line_width(0.05)
            pdf.line(18,168,190,168)

            pdf.ln(1)
            pdf.cell(7)
            pdf.set_font('Arial','',7)
            pdf.cell(10,260,txt = 'Tuan/Puan,')
            pdf.cell(146)
            pdf.set_font('Arial','B',7)
            pdf.cell(10,260,txt = 'PERINGATAN')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,270,txt = 'NOTIS TERHADAP AKAUN TIDAK AKTIF')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,280,txt = 'NOMBOR AKAUN')

            pdf.cell(42)
            pdf.cell(10,280,txt = ":")

            pdf.cell(-7)
            pdf.set_font('Arial','',7)
            pdf.cell(10,280,txt =str(Account_no[i]))

            pdf.ln(1)
            pdf.set_font('Arial','B',7)
            pdf.cell(7)
            pdf.cell(10,286,txt = 'BAKI SEMASA SETAKAT')
            pdf.set_font('Arial','',7)
            pdf.cell(22)
            pdf.cell(10,286,txt = str(Date2[i]))
            pdf.cell(10)
            pdf.set_font('Arial','B',7)
            pdf.cell(10,286,txt = ':')
            pdf.set_font('Arial','',7)
            pdf.cell(-6)
            pdf.cell(10,286,txt = str(currency[i]))
            pdf.cell(-4)
            pdf.cell(10,286,txt = str(Bal[i]))

            pdf.set_line_width(0.05)
            pdf.line(18,194,190,194)

            pdf.ln(1)
            pdf.set_font('Arial','',7.2)
            pdf.cell(7)
            pdf.cell(10,296,'Sila ambil maklum sekiranya  Akaun Semasa- /Akaun Semasa Mata Wang Asing-i/Akaun Simpanan- (CASA- ) tidak aktif melebihi tempoh dua belas (12)')
            pdf.ln(1)
            pdf.set_font('Arial','',7.2)
            pdf.cell(7)
            pdf.cell(10,302,txt = 'bulan, ianya akan diklasifikasikan sebagai  Akaun  Tidak Aktif. Yuran  penyelenggaraan  tahunan sebanyak RM10.00  atau nilai  mata  wang  asing  yang')
            pdf.set_font('Arial','',7)
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,308,txt = 'bersamaan,akan dikenakan dan sekiranya akaun tersebut kekal sebagai Akaun Tidak Aktif selama tujuh(7) tahun atau lebih, akaun tersebut akan ditutup dan')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,314,txt = 'baki akaun tersebut  akan dipindahkan ke  Pendaftar  Wang Tidak Dituntut seperti yang termaktub di dalam Akta Wang Tidak Dituntut 1965 (suatu  akta yang')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,320,txt = 'berkaitan dengan pembayaran wang yang tidak dituntut kepada Kumpulan Wang Disatukan Persekutuan).')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,330,txt = 'Kami ingin memaklumkan bahawa akaun CASA- anda telah diklasifikasikan sebagai Akaun Tidak Aktif. Sila aktifkan akaun anda dengan melakukan transaks')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,336,txt = 'deposit atau pengeluaran melalui kaunter dalam  tempoh tiga (3) bulan  dari tarikh notis ini. Sekiranya anda gagal berbuat demikian, yuran Akaun Tidak Aktif')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,342,txt = 'sebanyak RM10.00 atau nilai mata wang asing yang bersamaan akan dikenakan ke atas akaun anda. Bagi akaun yang berbaki sebanyak RM10.00 atau nila')
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,348,txt = 'mata wang bersamaan atau kurang, pihak Bank akan menutup akaun tersebut dan baki akaun akan diserap sebagai yuran perkhidmatan.')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,358,txt = 'Kami memohon maaf di atas segala kesulitan dan berharap anda boleh mengunjungi cawangan kami yang berhampiran bagi pengaktifan akaun.')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,368,txt = 'Terima kasih.')

            pdf.ln(2)
            pdf.cell(7)
            pdf.cell(10,378,txt = 'Yang Bena,')

            pdf.set_font('Arial','B',7)
            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,384,txt = 'MBSB Bank Berhad (No. Pendaftaran 200501033981) (716122-P)')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,394,txt ='Nota:')

            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,400,txt ='a. Dokumen ini adalah cetakan komputer. Tiada tandatangan diperlukan.')


            pdf.ln(1)
            pdf.cell(7)
            pdf.cell(10,406,txt ='b. Jika terdapat sebarang percanggahan di antara teks Bahasa Inggeris dan terjemahan Bahasa Malaysia ini, maka teks Bahasa Inggeris akan')


            pdf.ln(1)
            pdf.cell(9)
            pdf.cell(10,412,txt =' diterima pakai.')

            pdf.set_font('Arial','',6)
            pdf.cell(120)
            pdf.cell(10,428,txt = '00000' +str(count) + '(1)ISLM_DORREM_20221220.pdf')
            


            pdf.add_page()

            import pyqrcode
            import png
            from pyqrcode import QRCode
            s = 'ISL' +  str(Name[i]) +  str(Add1[i]) +  str(Add2[i])  + str(Add3[i]) +  str(Add4[i]) +  str(Date1[i]) +  str(Account_no[i])
            url = pyqrcode.create(s)
            url.png(r'E:\IWOC\APP SCRIPT\ISLM\CYCLE\ILS\DATA\barcode\\-%s.png' %(count), scale = 6)
            
    #-------------------------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------------------------
        
            pdf.set_font('Courier','B',7.2)
            pdf.cell(80)
            pdf.cell(10,340,txt = 'PRIVATE  & CONFIDENTIAL')

            pdf.ln(1)
            pdf.cell(50)
            pdf.cell(10,400,txt = '(' + str(postcode[i])  +'-00000' + str(count) + ')')
            # pdf.cell(10,400,txt = '222' + str(count))

            pdf.ln(1)
            pdf.cell(50)
            pdf.cell(10,406,txt = str(Name[i]))

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

            pdf.image(r'E:\IWOC\APP SCRIPT\ISLM\CYCLE\ILS\DATA\MBSB02.png',18,20,180)
            pdf.image(r'E:\IWOC\APP SCRIPT\ISLM\CYCLE\ILS\DATA\MBSB01.png',150,164,40)
            pdf.image(r'E:\IWOC\APP SCRIPT\ISLM\CYCLE\ILS\DATA\NearQR1.PNG',147,40,38)
            pdf.image(r'E:\IWOC\APP SCRIPT\ISLM\CYCLE\ILS\DATA\barcode\\-%s.png' %(count),100,42,10)

            pdf.set_font('Arial','',6)
            pdf.cell(-18)
            pdf.rotate(180)
            pdf.cell(10,10,txt = '00000' +str(count) + '(1)ISLM_DORREM_20221220.pdf')
            count +=1
        
    pdf.output('E:\IWOC\APP SCRIPT\ISLM\CYCLE\ILS\DATA\islm1.pdf')


pdf_in = open(r'E:\\IWOC\APP SCRIPT\\ISLM\\CYCLE\\ILS\DATA\\islm1.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    if pagenum % 2:
        page.rotateClockwise(180)
    pdf_writer.addPage(page)

pdf_out = open(r'E:\IWOC\OUTPUT\ISLM\ISLMPDF_1.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()    








