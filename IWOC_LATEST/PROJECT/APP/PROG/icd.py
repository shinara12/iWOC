from datetime import datetime
from fpdf import FPDF

def ICD(request,files1):
    path11 = r'E:\IWOC\SOURCE\\'+ files1
    with  open(path11) as file:
        line = file.readlines()
        total_line = len(line)
    total_clients = 0
    total_pages = 0
    with  open(path11) as file:
        line = file.readlines()
        for i in line:
            if i.startswith('1MAYBANK'):
                total_clients += 1
    total_pages  = int(total_clients/2) + 1
    with  open(path11) as file:
        # lines = file.readlines()
        run_date = []
        br_name = []
        report_date = []
        report_no = []
        acc_no_range = []
        ptype = []
        batch = []
        total_count = []
        date_received = []
        remarks = []
        total_card_received = []  
        TOTAL_CARDS_RECEIVED_BY_PERSO  = []
        # TOTAL_CARDS_BY_PLASTIC_TYPE = []
        TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL = []
        file.seek(0)
        for i in range(0,total_line):
            line = file.readline()
            if line.startswith('1MAYBANK'):
                run_date.append(line[114:122])
                line = file.readline()
                br_name.append(line[8:40])   # strip()
                report_date.append(line[64:73])
                report_no.append(line[114:122])
                line = file.readline()
                line = file.readline()
                if 'CARD RANGE ' in line:
                    line = file.readline()
                    line = file.readline()
                    acc_no_range.append(line[1:40])
                    ptype.append(line[46:49])
                    batch.append(line[54:60])
                    total_count.append(line[68:71])
                    line = file.readline()
                    line = file.readline()
                    line = file.readline()
                    total_card_received.append(line[119:123])
                    TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL.append('TEST_PERSO')
                else:
                    acc_no_range.append('no_account')
                    ptype.append('no_account')
                    batch.append('no_account')
                    total_count.append('no_account')
                    total_card_received.append('no_account')
                line = file.readline()
                line = file.readline()
                if 'TOTAL CARDS RECEIVED BY PERSO' in line:
                    TOTAL_CARDS_RECEIVED_BY_PERSO.append(line[42:54]) # strip()
                line = file.readline()
                if 'TOTAL CARDS BY PLASTIC TYPE' in line:
                    TOTAL_CARDS_BY_PLASTIC_TYPE = []
                    TOTAL_CARDS_BY_PLASTIC_TYPE.append(line[36:54])
                    line1 = file.readline()
                    line1 = line1.strip()
                    if line1.startswith(('1','2','3','4','5','6','7','8','9')) and not line1.startswith('1MAYBANK'):
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append(line1[0:24])
                    else:
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append('Test')
                    line2 = file.readline()
                    line2 = line2.strip()
                    if line2.startswith(('1','2','3','4','5','6','7','8','9')) and not line2.startswith('1MAYBANK'):
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append(line2[0:24])
                    else:
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append('Test')
                    line3 = file.readline()
                    line3 = line3.strip()
                    if line3.startswith(('1','2','3','4','5','6','7','8','9')) and not line3.startswith('1MAYBANK'):
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append(line3[0:24])
                    else:
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append('Test')
                    line4 = file.readline()
                    line4 = line4.strip()
                    if line4.startswith(('1','2','3','4','5','6','7','8','9')) and not line4.startswith('1MAYBANK'):
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append(line4[0:24])
                    else:
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append('Test')
                    line5 = file.readline()
                    line5 = line5.strip()
                    if line5.startswith(('1','2','3','4','5','6','7','8','9')) and not line5.startswith('1MAYBANK'):
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append(line5[0:24])
                    else:
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append('Test')
                    line6 = file.readline()
                    line6 = line6.strip()
                    if line6.startswith(('1','2','3','4','5','6','7','8','9')) and not line6.startswith('1MAYBANK'):
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append(line6[0:24])
                    else:
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append('Test')
                    line7 = file.readline()
                    line7 = line7.strip()
                    if line7.startswith(('1','2','3','4','5','6','7','8','9')) and not line7.startswith('1MAYBANK'):
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append(line7[0:24])
                    else:
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append('Test')
                    line8 = file.readline()
                    line8 = line8.strip()
                    if line8.startswith(('1','2','3','4','5','6','7','8','9')) and not line8.startswith('1MAYBANK'):
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append(line8[0:24])
                    else:
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append('Test')
                    line9 = file.readline()
                    line9 = line9.strip()
                    if line9.startswith(('1','2','3','4','5','6','7','8','9')) and not line9.startswith('1MAYBANK'):
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append(line9[0:24])
                    else:
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append('Test')
                    line10 = file.readline()
                    line10 = line10.strip()
                    if line10.startswith(('1','2','3','4','5','6','7','8','9'))  and not line10.startswith('1MAYBANK'):
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append(line10[0:24])
                    else:
                        TOTAL_CARDS_BY_PLASTIC_TYPE.append('Test')
                    if 'TOTAL CARDS BY PLASTIC TYPE' in line:
                        TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL.append(TOTAL_CARDS_BY_PLASTIC_TYPE)
        # print(TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL,'finalTOT')
    count  = 1
    pdf = FPDF()
    for i in range(0,len(acc_no_range),2):
        pdf.set_auto_page_break(False)
        pdf.add_page()
        if total_clients < total_pages *2:
            # print(total_clients,total_pages,'0-000')
            pdf.ln(1)
            pdf.set_font('Courier','B',6)
            pdf.cell(10,92,txt = '1MAYBANK ')

            pdf.cell(30)
            pdf.cell(10,92,txt = ' LIST OF ATM CARDS DESPATCH LISTING')

            pdf.cell(50)
            pdf.cell(10,92,txt = 'RUN DATE  : ')

            pdf.cell(5)
            pdf.cell(10,92,txt = str(run_date[i]))

            pdf.cell(20)
            pdf.cell(10,92,txt = ' PAGE:   1 ')

            pdf.ln(1)
            pdf.set_font('Courier','B',6)
            pdf.cell(10,97,txt = br_name[i])

            pdf.cell(50)
            pdf.cell(10,97,txt = 'REPORT DATE : ')

            pdf.cell(8)
            pdf.cell(10,97,txt = report_date[i])

            pdf.cell(40)
            pdf.cell(10,97,txt = 'REPORT NO :')


            pdf.cell(8)
            pdf.cell(10,97,txt = report_no[i])

            pdf.ln(1)
            pdf.cell(10,102,txt = 'PERSO  A   GEMALTO SDN BHD')

            if TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL[i] == 'TEST_PERSO':
                pdf.set_auto_page_break(False)
                pdf.set_draw_color(r=128,g=128,b=128)
                pdf.set_line_width(-0.20)
                pdf.line(4,55,170,55)
                pdf.line(4,62,170,62)

                pdf.line(4,69,170,69)
                pdf.line(4,76,170,76)
                pdf.line(4,83,170,83)
                pdf.line(4,90,170,90)
                pdf.line(4,97,170,97)
                pdf.line(4,104,170,104)
                pdf.line(4,111,170,111)
                pdf.line(4,118,170,118)
                pdf.line(4,125,170,125)
                pdf.line(4,132,170,132)
                pdf.line(4,139,170,139)
                pdf.line(4,146,170,146)
                pdf.line(4,153,170,153)
                pdf.line(4,160,170,160)

                pdf.line(4,55,4,160)     # first vertical line
                pdf.line(170,55,170,160)  # second vertical line

                pdf.ln(1)
                pdf.set_font('Courier','B',6)
                pdf.cell(161)
                count = str(count)
                if len(count) == 1:
                    str_count = '00000' + count
                    pdf.cell(10,92,txt = str_count)
                if len(count) == 2:
                    str_count = '0000' + count
                    pdf.cell(10,92,txt = str_count)
                if len(count) == 3:
                    str_count = '000' + count
                    pdf.cell(10,92,txt = str_count)
                if len(count) == 4:
                    str_count = '00' + count
                    pdf.cell(10,92,txt = str_count)
                if len(count) == 5:
                    str_count = '0' + count
                    pdf.cell(10,92,txt = str_count)
                count = int(count)
                count += 1

                pdf.ln(10)
                pdf.cell(161)
                pdf.cell(10,276,txt = '1')

                pdf.ln(1)
                pdf.cell(10,84,txt = 'CARD RANGE')

                pdf.cell(40)
                pdf.cell(10,84,txt = 'PTYPE ')

                pdf.cell(1)
                pdf.cell(10,84,txt = 'BATCH#')

                pdf.cell(10)
                pdf.cell(10,84,txt = 'TOTAL COUNT')

                pdf.cell(10)
                pdf.cell(10,84,txt = 'DATE RECEIVED')

                pdf.cell(20)
                pdf.cell(10,84,txt = 'REMARKS')

                pdf.ln(1)
                pdf.cell(10,90,txt = str(acc_no_range[i]))

                pdf.cell(42)
                pdf.cell(10,90,txt = ptype[i])

                pdf.cell(1)
                pdf.cell(10,90,txt = batch[i])

                pdf.cell(15)
                pdf.cell(10,90,txt = total_count[i])

                pdf.ln(1)
                pdf.cell(10,98,txt = '-')

                pdf.ln(1)
                # pdf.cell(10,100,txt = '-')

                pdf.cell(92)
                pdf.cell(10,98,txt = ' LAST ISSUE NUMBER    : ')

                pdf.ln(1)
                pdf.cell(10,100,txt = '0')

                pdf.cell(83)
                pdf.cell(10,100,txt = 'TOTAL CARD RECEIVED   : ')

                pdf.cell(24)
                pdf.cell(10,100,txt = total_card_received[i])

                pdf.ln(1)
                pdf.cell(10,102,txt = '-')

                pdf.cell(83)
                pdf.cell(10,104,txt = 'VERIFIED BY : __________________________')

                pdf.ln(1)
                pdf.cell(10,108,txt = ' *** END OF REPORT ***        RETENTION PERIOD FOR HARDCOPY: ')

            else:
                pdf.set_auto_page_break(False)
                pdf.set_draw_color(r=128,g=128,b=128)
                pdf.set_line_width(-0.20)
                pdf.line(4,55,170,55)
                pdf.line(4,62,170,62)

                pdf.line(4,69,170,69)
                pdf.line(4,76,170,76)
                pdf.line(4,83,170,83)
                pdf.line(4,90,170,90)
                pdf.line(4,97,170,97)
                pdf.line(4,104,170,104)
                pdf.line(4,111,170,111)
                pdf.line(4,118,170,118)
                pdf.line(4,125,170,125)
                pdf.line(4,132,170,132)
                pdf.line(4,139,170,139)
                pdf.line(4,146,170,146)
                pdf.line(4,153,170,153)
                pdf.line(4,160,170,160)

                pdf.line(4,55,4,160)     # first vertical line
                pdf.line(170,55,170,160)  # second vertical line

                pdf.set_font('Courier','B',6)
                pdf.cell(10,68,txt = '1MAYBANK ')

                pdf.cell(30)
                pdf.cell(10,68,txt = ' LIST OF ATM CARDS DESPATCH LISTING')

                pdf.cell(50)
                pdf.cell(10,68,txt = 'RUN DATE  : ')

                pdf.cell(5)
                pdf.cell(10,68,txt = str(run_date[i]))

                pdf.cell(20)
                pdf.cell(10,68,txt = ' PAGE:   1 ')

                pdf.ln(1)
                pdf.set_font('Courier','B',6)
                pdf.cell(10,74,txt = br_name[i])

                pdf.cell(50)
                pdf.cell(10,74,txt = 'REPORT DATE : ')

                pdf.cell(8)
                pdf.cell(10,74,txt = report_date[i])

                pdf.cell(40)
                pdf.cell(10,74,txt = 'REPORT NO :')


                pdf.cell(8)
                pdf.cell(10,74,txt = report_no[i])


                pdf.ln(1)
                pdf.cell(10,78,txt = 'PERSO  A   GEMALTO SDN BHD')

                h = 81
                for k in range(0,10):
                    if TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL[i][k] != 'Test':
                        # print(TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL[i][k],'ifififififi')
                        pdf.cell(28)
                        pdf.cell(10,h,txt = TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL[i][k])
                        pdf.ln(1)
                        pdf.cell(18)
                        h += 4
                pdf.cell(92)
                pdf.cell(10,h,txt = 'VERIFIED BY : __________________________')

                pdf.ln(1)
                pdf.cell(10,h,txt = ' *** END OF REPORT ***        RETENTION PERIOD FOR HARDCOPY: ')

            if TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL[i+1] == 'TEST_PERSO':
                pdf.ln(1)
                pdf.line(4,175,170,175)
                pdf.line(4,182,170,182)
                pdf.line(4,189,170,189)
                pdf.line(4,196,170,196)
                pdf.line(4,203,170,203)
                pdf.line(4,210,170,210)
                pdf.line(4,217,170,217)
                pdf.line(4,224,170,224)
                pdf.line(4,231,170,231)
                pdf.line(4,238,170,238)
                pdf.line(4,245,170,245)
                pdf.line(4,252,170,252)
                pdf.line(4,259,170,259)
                pdf.line(4,266,170,266)
                pdf.line(4,273,170,273)
                pdf.line(4,280,170,280)
                pdf.line(4,287,170,287)

                pdf.line(4,175,4,287)    # first vertical line
                pdf.line(170,175,170,287) # second vertical line 


                pdf.ln(1)
                pdf.cell(10,288,txt = '1MAYBANK ')

                pdf.cell(30)
                pdf.cell(10,288,txt = ' LIST OF ATM CARDS DESPATCH LISTING')

                pdf.cell(50)
                pdf.cell(10,288,txt = 'RUN DATE  :')

                pdf.cell(5)
                pdf.cell(10,288,txt = str(run_date[i+1]))

                pdf.cell(20)
                pdf.cell(10,288,txt = ' PAGE:   1 ')


                pdf.ln(1)
                pdf.cell(10,293,txt = br_name[i+1])

                pdf.cell(50)
                pdf.cell(10,293,txt = 'REPORT DATE :')

                pdf.cell(8)
                pdf.cell(10,293,txt = report_date[i+1])
                
                pdf.cell(40)
                pdf.cell(10,293,txt = 'REPORT NO :')

                pdf.cell(8)
                pdf.cell(10,293,txt = report_no[i+1])

                pdf.ln(1)
                pdf.cell(10,298,txt = 'PERSO  A   GEMALTO SDN BHD')

                pdf.ln(1)
                pdf.cell(10,302,txt = 'CARD RANGE')

                pdf.cell(40)
                pdf.cell(10,302,txt = 'PTYPE')

                pdf.cell(1)
                pdf.cell(10,302,txt = 'BATCH#')

                pdf.cell(20)
                pdf.cell(10,302,txt = 'TOTAL COUNT')

                pdf.cell(10)
                pdf.cell(10,302,txt = 'DATE RECEIVED')

                pdf.cell(20)
                pdf.cell(10,302,txt = 'REMARKS')

                pdf.ln(1)
                pdf.cell(10,312,txt = str(acc_no_range[i+1]))

                pdf.cell(42)
                pdf.cell(10,312,txt = ptype[i+1])

                pdf.cell(1)
                pdf.cell(10,312,txt = batch[i+1])

                pdf.cell(20)
                pdf.cell(10,312,txt = total_count[i+1])

                pdf.ln(1)
                pdf.cell(10,320,txt = '-')

                pdf.cell(92)
                pdf.cell(10,318,txt = ' LAST ISSUE NUMBER    : ')

                pdf.ln(1)
                pdf.cell(10,318,txt = '0')

                pdf.cell(92)
                pdf.cell(10,320,txt = 'TOTAL CARD RECEIVED   : ')

                pdf.cell(24)
                pdf.cell(10,320,txt = total_card_received[i+1])

                pdf.ln(1)
                pdf.cell(10,320,txt = '-')

                pdf.cell(92)
                pdf.cell(10,323,txt = 'VERIFIED BY : __________________________')

                pdf.ln(1)
                pdf.cell(10,334,txt = ' *** END OF REPORT ***        RETENTION PERIOD FOR HARDCOPY: ')

                pdf.set_font('Arial','',8)
                pdf.ln(1)
                pdf.cell(161)
                pdf.cell(10,490,txt = '2')

            else:
                pdf.line(4,175,170,175)
                pdf.line(4,182,170,182)
                pdf.line(4,189,170,189)
                pdf.line(4,196,170,196)
                pdf.line(4,203,170,203)
                pdf.line(4,210,170,210)
                pdf.line(4,217,170,217)
                pdf.line(4,224,170,224)
                pdf.line(4,231,170,231)
                pdf.line(4,238,170,238)
                pdf.line(4,245,170,245)
                pdf.line(4,252,170,252)
                pdf.line(4,259,170,259)
                pdf.line(4,266,170,266)
                pdf.line(4,273,170,273)
                pdf.line(4,280,170,280)
                pdf.line(4,287,170,287)

                pdf.line(4,175,4,287)    # first vertical line
                pdf.line(170,175,170,287) #second vertical line

                pdf.ln(1)
                pdf.cell(10,288,txt = '1MAYBANK ')

                pdf.cell(30)
                pdf.cell(10,288,txt = ' LIST OF ATM CARDS DESPATCH LISTING')

                pdf.cell(50)
                pdf.cell(10,288,txt = 'RUN DATE  :')

                pdf.cell(5)
                pdf.cell(10,288,txt = str(run_date[i+1]))

                pdf.cell(20)
                pdf.cell(10,288,txt = ' PAGE:   1 ')


                pdf.ln(1)
                pdf.cell(10,293,txt = br_name[i+1])

                pdf.cell(50)
                pdf.cell(10,293,txt = 'REPORT DATE :')

                pdf.cell(8)
                pdf.cell(10,293,txt = report_date[i+1])
                
                pdf.cell(40)
                pdf.cell(10,293,txt = 'REPORT NO :')

                pdf.cell(8)
                pdf.cell(10,293,txt = report_no[i+1])

                pdf.ln(1)
                pdf.cell(10,298,txt = 'PERSO  A   GEMALTO SDN BHD')

                pdf.ln(1)
                pdf.cell(10,311,txt = 'TOTAL CARDS RECEIVED BY PERSO')

                pdf.ln(1)
                pdf.cell(10,314,txt = ' TOTAL CARDS BY PLASTIC TYPE ')
                h = 314
                for k in range(0,10):
                    if TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL[i+1][k] != 'Test':
                        pdf.cell(28)
                        pdf.cell(10,h,txt = TOTAL_CARDS_BY_PLASTIC_TYPE_FINAL[i+1][k])
                        pdf.ln(1)
                        pdf.cell(18)
                        h += 4
                pdf.cell(92)
                pdf.cell(10,h,txt = 'VERIFIED BY : __________________________')

                pdf.ln(1)
                pdf.cell(10,h,txt = ' *** END OF REPORT ***        RETENTION PERIOD FOR HARDCOPY: ')

                pdf.set_font('Arial','',8)
                pdf.ln(1)
                pdf.cell(161)
                pdf.cell(10,490,txt = '2')

    no = pdf.page_no()
    # print(no,'---')
    pdf.add_page()
    pdf.set_auto_page_break(False)
    pdf.set_font('Courier','B',8)
    pdf.ln(270)
    pdf.rotate(90)
    pdf.cell(10,20,txt = 'Summary Report')

    pdf.rotate(90)
    pdf.cell(10,6,txt = '-------------------------------------------------')

    pdf.rotate(90)
    pdf.cell(10,-8,txt = 'Data Filename')
    pdf.cell(18)
    pdf.cell(10,-7.5,txt = ':')
    pdf.cell(-4)
    pdf.cell(10,-7.5,txt = str(files1))


    now = datetime.now()
    start_time = now.strftime("%d/%m/%Y %H:%M:%S")

    pdf.rotate(90)
    pdf.cell(10,-88,txt = 'Time Start')
    pdf.cell(18)
    pdf.cell(10,-88,txt = ':')
    pdf.cell(-4)
    pdf.cell(10,-88,txt = str(start_time))

    now = datetime.now()
    end_time = now.strftime("%d/%m/%Y %H:%M:%S")

    pdf.rotate(90)
    pdf.cell(10,-168,txt = 'Time Stop')
    pdf.cell(18)
    pdf.cell(10,-168,txt = ':')
    pdf.cell(-4)
    pdf.cell(10,-168,txt = str(end_time))

    pdf.rotate(90)
    pdf.cell(10,-248,txt = 'Total Pages Report')
    pdf.cell(26)
    pdf.cell(10,-248,txt = ':')
    pdf.cell(-4)
    pdf.cell(10,-248,txt = str(total_clients))

    pdf.rotate(90)
    pdf.cell(10,-344,txt = 'Total Pages Of Print')
    pdf.cell(26)
    pdf.cell(10,-344,txt = ':')
    pdf.cell(-4)
    pdf.cell(10,-344,txt = str(no))

    pdf.output('E:\IWOC\OUTPUT\ICD\ICD1.pdf')