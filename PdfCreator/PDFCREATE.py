from fpdf import FPDF



global dist1
global dist2
class PDF(FPDF):
    def header(self):
        dist1=8
        dist2=8
        self.line(210,32,0,32)#top horizontal up
        self.line(210,33.5,0,33.5)#top horizontal below
        self.line(19,0,19,297)#vertical right
        self.line(17.5,0,17.5,297)#vertical left
        self.line(210,272,0,272)#bottom horizontal up
        self.line(210,273.5,0,273.5)#bottom horizontal below
        for i in range(1,30):
            self.line(210,33+dist1,0,33+dist1)
            dist1=dist1+8
        for i in range(1,30):
            self.set_xy(7,29.35+dist2)
            self.cell(20,5,f'{i})')
            dist2=dist2+8

pdf=PDF('P','mm','A4')
pdf.set_auto_page_break(auto=True)
pdf.set_text_color(5,18,166)
pdf.add_font('KrishnaSonawane1','','Fonts/KrishnaSonawane1.ttf')
pdf.add_font('KrishnaSonawane2','','Fonts/KrishnaSonawane2.ttf')
pdf.add_font('KrishnaSonawane3','','Fonts/KrishnaSonawane3.ttf')
pdf.set_font('KrishnaSonawane1','',16)
pdf.add_page()
#LINES-----------------------------------------------------------------------------------------------

    #c32+=297
    #c335+=297
    #c0+=297
    #c297+=297
    #c272+=297
    #c2735+=297
    #c33+=297
    #c2935+=297




x=20
y=37.35
senlimit=20
breaklimit=0
pg=1
PG_right_lim=208
letter_spacing=2.2
word_spacing=5.5
for i in range(0,2000):
    user_input=int(input("Choice: "))
    if(user_input==0):
        break
    if(user_input==1):
        punctuation=input("Text Type: ")
#----------------------------------------------------------------------------------------------------------------------
        if(punctuation=="P"):
            ln=((y-37.35)/8)+1
            print(f'Current Pos: PG: {pg}, LN: {ln}')
            print(f'Current Cursor Pos: x={x}, y={y}')
            x=float(input("X: "))
            y=float(input("Y: "))
            fontselect=['KrishnaSonawane1','KrishnaSonawane2','KrishnaSonawane3']
            abc=input("Enter Sentence: ")
            placeholder=""
            word_list=[]
            for i in range(0,len(abc)):
                if(abc[i].isspace()==False):
                    placeholder=placeholder+abc[i]
                if(abc[i].isspace()==True):
                    word_list.append(placeholder)
                    placeholder=""
                if(i==(len(abc)-1)):
                    word_list.append(placeholder)
                    placeholder=""
            for i in word_list:
                if(len(i)>=8):
                    for l in range(0,len(i)):
                        x+=letter_spacing
                        x=round(x,2)
                        if(x>=(PG_right_lim-1)):
                            pdf.set_xy(x,y)
                            pdf.cell(3,5,"-")
                            y+=8
                            x=20
                            if(y>261.35):
                                pdf.add_page()
                                y=37.35
                                pg+=1
                        pdf.set_xy(x,y)
                        pdf.cell(3,5,i[l])
                        if(l==(len(i)-1)):
                            x+=word_spacing
                            x=round(x,2)
                if(len(i)<8):
                    pdf.set_font('KrishnaSonawane1','',18)
                    senlimit=x
                    for s in range(0,len(i)):
                        if(s<(len(i)-1)):
                            senlimit=senlimit+2.2
                            senlimit=round(senlimit,2)
                        if(s==(len(i)-1)):
                            senlimit=senlimit+5.5
                            senlimit=round(senlimit,2)
                    if(senlimit>PG_right_lim):
                        y=y+8
                        x=20
                        if(y>261.35):
                            pdf.add_page()
                            y=37.35
                            pg+=1
                    for j in range(0,len(i)):
                        pdf.set_xy(x,y)
                        pdf.cell(3,5,i[j])
                        if(j<(len(i)-1)):
                            x=x+letter_spacing
                            x=round(x,2)
                        if(j==(len(i)-1)):
                            x=x+word_spacing
                            x=round(x,2)
#----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------
        if(punctuation=="sP"):
            xl=int(input("Edge Limit: "))
            if(y>=37.35 and y<=261.35):
                pg=1
            ln=((y-37.35)/8)+1
            print(f'Current Pos: PG: {pg}, LN: {ln}')
            print(f'Current Cursor Pos: x={x}, y={y}')
            x=float(input("X: "))
            y=float(input("Y: "))
            fontselect=['KrishnaSonawane1','KrishnaSonawane2','KrishnaSonawane3']
            abc=input("Enter Sentence: ")
            placeholder=""
            word_list=[]
            for i in range(0,len(abc)):
                if(abc[i].isspace()==False):
                    placeholder=placeholder+abc[i]
                if(abc[i].isspace()==True):
                    word_list.append(placeholder)
                    placeholder=""
                if(i==(len(abc)-1)):
                    word_list.append(placeholder)
                    placeholder=""
            for i in word_list:
                if(len(i)>=8):
                    for l in range(0,len(i)):
                        x+=letter_spacing
                        x=round(x,2)
                        if(x>=(PG_right_lim-1)):
                            pdf.set_xy(x,y)
                            pdf.cell(3,5,"-")
                            y+=8
                            x=xl
                            if(y>261.35):
                                pdf.add_page()
                                y=37.35
                                pg+=1
                        pdf.set_xy(x,y)
                        pdf.cell(3,5,i[l])
                        if(l==(len(i)-1)):
                            x+=word_spacing
                            x=round(x,2)
                if(len(i)<8):
                    pdf.set_font('KrishnaSonawane1','',18)
                    senlimit=x
                    for s in range(0,len(i)):
                        if(s<(len(i)-1)):
                            senlimit=senlimit+2.2
                            senlimit=round(senlimit,2)
                        if(s==(len(i)-1)):
                            senlimit=senlimit+5.5
                            senlimit=round(senlimit,2)
                    if(senlimit>PG_right_lim):
                        y=y+8
                        x=xl
                        if(y>261.35):
                            pdf.add_page()
                            y=37.35
                            pg+=1
                    for j in range(0,len(i)):
                        pdf.set_xy(x,y)
                        pdf.cell(3,5,i[j])
                        if(j<(len(i)-1)):
                            x=x+letter_spacing
                            x=round(x,2)
                        if(j==(len(i)-1)):
                            x=x+word_spacing
                            x=round(x,2)
#----------------------------------------------------------------------------------------------------------

fontselect=['KrishnaSonawane1','KrishnaSonawane2','KrishnaSonawane3']
pdf.output('helloworld2.pdf')
