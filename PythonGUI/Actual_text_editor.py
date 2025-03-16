from tkinter import *
from tkinter import messagebox
from CollapsiblePane import CollapsiblePane as cp
import os
from PIL import Image, ImageTk
from Scrollable import ScrollableFrame as Sf


root=Tk()
root.geometry("1000x700")

Cutom_Chars_Frame=Frame(root, bg="red", width=1000, height=700)
Cutom_Chars_Frame.grid(row=0, column=0)
Cutom_Chars_Frame.grid_propagate(False)

Main_Frame=Frame(root, bg="#1f1f1f", width=1000, height=700)
Main_Frame.grid(row=0, column=0)
Main_Frame.grid_propagate(False)

Start_Frame=Frame(root, bg="#1f1f1f", width=1000, height=700)
Start_Frame.grid(row=0, column=0)
Start_Frame.grid_propagate(False)

Win_Chnage_panel=Frame(Main_Frame, bg="#1f1f1f", width=200, height=50, highlightbackground="white", highlightthickness=1.5)
Win_Chnage_panel.grid(row=0, column=0)
Win_Chnage_panel.grid_propagate(False)

Top_Tool_panel=Frame(Main_Frame, bg="#1f1f1f", width=800, height=50, highlightbackground="white", highlightthickness=1.5)
Top_Tool_panel.grid(row=0, column=1, columnspan=2)
Top_Tool_panel.grid_propagate(False)

#--------------------------------------------------------------------------------------------------------------------------------------
#main_canvas.scale(ALL, x, y, factor, factor)


#--------------------------------------------------------------------------------------------------------------------------------------

Left_Tool_panel=Frame(Main_Frame, bg="#1f1f1f", width=200, height=650, highlightbackground="white", highlightthickness=1.5)
Left_Tool_panel.grid(row=1,column=0, sticky=NE)
Left_Tool_panel.grid_propagate(False)

SCR_Frame=Sf(Main_Frame, Bg="#1f1f1f", Width=300, Height=650)
SCR_Frame.grid(row=1,column=2, sticky=NW)

canvas_panel=Frame(Main_Frame, bg="#1f1f1f", width=500, height=650)
canvas_panel.grid(row=1, column=1)
canvas_panel.grid_propagate(False)
canvas_panel.grid_rowconfigure(0, weight=1)
canvas_panel.grid_columnconfigure(0, weight=1)

main_canvas=Canvas(canvas_panel, bg="#1f1f1f")
main_canvas.grid(row=0,column=0, sticky=NSEW)
main_canvas.create_rectangle(145,50,355,347, fill="white", tag="RT1")

Transformed_page_panel=cp(SCR_Frame.frame, 'Transform page', 'Transform page', 'black', 'white')
Transformed_page_panel.grid(row=0, column=0, pady=5, padx=10, sticky=W)

Multiple_Rule_Lines=cp(Transformed_page_panel.frame, 'Multiple Lines', 'Multiple Lines', 'black', 'white')
Multiple_Rule_Lines.grid(row=1, column=0, pady=5, padx=10, sticky=W)
Multiple_Rule_Lines._change(NewState="DISABLED")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All_width=800
All_height=700

Start_WImage_Panel=Frame(Start_Frame, width=800, height=700, bg="#33333d", highlightbackground="white", highlightthickness=1.5)
Start_WImage_Panel.grid(row=0, column=0)
Start_WImage_Panel.grid_propagate(False)

Start_Button_Panel=Frame(Start_Frame, bg="#1f1f1f", width=200, height=700, highlightbackground="white", highlightthickness=1.5)
Start_Button_Panel.grid(row=0, column=1)
Start_Button_Panel.grid_propagate(False)

IH_t=Frame(Start_WImage_Panel, width=800, height=50, bg="#33333d")
IH_t.grid(row=0, column=0)

Image_Holder=Frame(Start_WImage_Panel, width=800, height=600, bg="#33333d")
Image_Holder.grid(row=1, column=0)
Image_Holder.grid_propagate(False)
Image_Holder.grid_rowconfigure(0, weight=1)
Image_Holder.grid_columnconfigure(0, weight=1)

original_image = Image.open("Resources/FrontPagePlaceholder.png")

resized_image = original_image.resize((800, 600))
resized_photo = ImageTk.PhotoImage(resized_image)
image_label = Label(Image_Holder, image=resized_photo,)
image_label.grid(row=0, column=0)
image_label.image = resized_photo

IH_b=Frame(Start_WImage_Panel, width=800, height=50, bg="#33333d")
IH_b.grid(row=2, column=0)

def up_frame(ofr):
    ofr.tkraise()

Change_Page_Dimensions=cp(Start_Button_Panel, 'Page Dimensions', 'Page Dimensions', 'black', 'white')
Change_Page_Dimensions.grid(row=0, column=0, pady=5, padx=10, sticky=W)

start_button=Button(Start_Button_Panel, text="next page", bg="black", fg="white",command=lambda ofr=Main_Frame: up_frame(ofr))
start_button.grid(row=1, column=0)
start_button.configure(state=DISABLED)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

num=1
RECT_NAMES=[]
RECT_NAMES.append('RT1')
def new_slide():
    global num, ph_change_scl, da_factor
    rect_tag="RT"+str(num)
    ref=main_canvas.find_withtag(rect_tag)
    ref_list=main_canvas.coords(ref)
    pg_height=ref_list[3]-ref_list[1]
    pg_dist=(pg_height/(float(ph_change_scl.get())))*20
    num=num+1
    new_rect_tag="RT"+str(num)
    RECT_NAMES.append(new_rect_tag)
    main_canvas.create_rectangle(ref_list[0],ref_list[3]+pg_dist,ref_list[2],ref_list[3]+pg_dist+pg_height, tag=new_rect_tag, fill="white")
    HOR_RULE_DICT.update({new_rect_tag:{}})
    VER_RULE_DICT.update({new_rect_tag:{}})
    for prev_mr in HOR_RULE_DICT[rect_tag]:
        HOR_RULE_DICT[new_rect_tag].update({prev_mr:[]})
    for prev_nr in VER_RULE_DICT[rect_tag]:
        VER_RULE_DICT[new_rect_tag].update({prev_nr:[]})
    for butt_refs in HOR_RULE_BUTTON_LIST:
        butt_refs.invoke()
    for vbutt_refs in VER_RULE_BUTTON_LIST:
        vbutt_refs.invoke()
    #print(HOR_RULE_DICT)
#ExE_Rect=main_canvas.create_rectangle(145-10,50-10,355+10,347+10, tag="exception", fill="red")
LINE_RECORDS={}
da_factor=1
def do_zoom(event):
    global da_factor, lnstarted, pstarted
    x = main_canvas.canvasx(event.x)
    y = main_canvas.canvasy(event.y)
    factor = 1.0005 ** event.delta
   
    main_canvas.scale(ALL, x, y, factor, factor)
    z=main_canvas.coords(main_canvas.find_withtag("RT1"))
    da_dif=z[3]-z[1]
    da_factor=da_dif/int(ph_change_scl.get())
    if(lnstarted==1):
        for tags in LINE_RECORDS:
            lnmemo=main_canvas.find_withtag(tags)
            main_canvas.itemconfig(lnmemo, width=da_factor)
    for rects in HOR_RULE_DICT:
        for  mulrul in HOR_RULE_DICT[rects]:
            for rulln in HOR_RULE_DICT[rects][mulrul]:
                main_canvas.itemconfig(rulln, width=(da_factor*0.2))
    for rects in VER_RULE_DICT:
        for  mulrul in VER_RULE_DICT[rects]:
            for rulln in VER_RULE_DICT[rects][mulrul]:
                main_canvas.itemconfig(rulln, width=(da_factor*0.2))
    for ls in Letter_list:
        main_canvas.itemconfig(ls, font=("Adobe Devanagari", int(8*da_factor)))
    if(pstarted==1):
        for ptags in PENCIL_RECORDS:
            pmemo=main_canvas.find_withtag(ptags)
            main_canvas.itemconfig(pmemo, width=da_factor)

lnstarted=0
line_num=0
def line_start(event):
    global lnx, lny, lnstarted, lntag, line_num
    lnx=main_canvas.canvasx(event.x)
    lny=main_canvas.canvasy(event.y)
    line_num+=1
    lntag="ln"+str(line_num)
    lnstarted=1

def line_end(event):
    global lnx, lny, da_factor, lntag
    main_canvas.delete(lntag)
    main_canvas.create_line(lnx, lny, main_canvas.canvasx(event.x), main_canvas.canvasy(event.y), tag=lntag, width=da_factor)

def line_end_record(event):
    global lntag,lnx,lny
    cvx=main_canvas.canvasx(event.x)
    cvy=main_canvas.canvasy(event.y)

    LINE_RECORDS.update({lntag:main_canvas.coords(main_canvas.find_withtag(lntag))})

def Line_bind():
    global previous_cursor
    for i in EDITOR_BINDS:
        main_canvas.unbind(i)
    main_canvas.configure(cursor="crosshair")
    previous_cursor="crosshair"
    main_canvas.bind('<ButtonPress-1>', line_start)
    main_canvas.bind('<B1-Motion>', line_end)
    main_canvas.bind('<ButtonRelease-1>',line_end_record)

selected_rectangle=''
SELECTED_RECT_LIST=[]
def arrow_press(event):
    global selected_rectangle
    arowx=main_canvas.canvasx(event.x)
    arowy=main_canvas.canvasy(event.y)
    main_canvas.itemconfig(selected_rectangle, fill="white")
    SELECTED_RECT_LIST.clear()
    for rect in RECT_NAMES:
        ref=main_canvas.find_withtag(rect)
        ref_coords=main_canvas.coords(ref)
        if(arowx>=ref_coords[0] and arowx<=ref_coords[2]):
            if(arowy>=ref_coords[1] and arowy<=ref_coords[3]):
                selected_rectangle=rect
                SELECTED_RECT_LIST.append(selected_rectangle)
                main_canvas.itemconfig(selected_rectangle, fill="#1F51FF")
    print(SELECTED_RECT_LIST)

def arrow_move(event):
    pass    

def Arrow_bind():
    global previous_cursor
    for i in EDITOR_BINDS:
        main_canvas.unbind(i)
    main_canvas.configure(cursor="hand2")
    previous_cursor="hand2"
    main_canvas.bind('<ButtonPress-1>', arrow_press)
    main_canvas.bind('<B1-Motion>', arrow_move)

Letter_list=[]
def save_page_transform():
    for tag_index in range(len(RECT_NAMES)):
        if(RECT_NAMES[tag_index]=="RT1"):
            main_canvas.delete(RECT_NAMES[tag_index])
            main_canvas.create_rectangle(145,50,145+float(pl_change_scl.get()),50+float(ph_change_scl.get()), fill="white", tag=RECT_NAMES[tag_index])
        else:
            main_canvas.delete(RECT_NAMES[tag_index])
            newref=main_canvas.find_withtag(RECT_NAMES[tag_index-1])
            newref_list=main_canvas.coords(newref)
            newpg_height=newref_list[3]-newref_list[1]
            newpg_dist=(newpg_height/(float(ph_change_scl.get())))*20
            main_canvas.create_rectangle(newref_list[0],newref_list[3]+newpg_dist,newref_list[2],newref_list[3]+newpg_dist+newpg_height, tag=RECT_NAMES[tag_index], fill="white")
    Add_HR.configure(state=NORMAL)
    Add_VER.configure(state=NORMAL)
    Save_transform.configure(state=DISABLED)
    Save_Rule_Files._change(NewState="NORMAL")
    Multiple_Rule_Lines._change(NewState="NORMAL")
    start_button.configure(state=NORMAL)
    # i=0
    # j=0
    # counting_iterations=0
    # for x in range(0, 40):
    #    i+=5
    #    j=0
    #    for y in range(0, 100):
    #        Letter=main_canvas.create_text(145+i, 50+j, text="C", font=("Adobe Devanagari", 8), anchor=NW)
    #        Letter_list.append(Letter)
    #        j+=5
    #        counting_iterations+=1
    # print(counting_iterations)
#lags even when just zooming in or out on dots, the size of the object doesnt matter but the number of objects which are being scaled matters
    

def Draw_Hor_Rules(hor_lnstart_sbox, hor_lnend_sbox, hor_lnnum_sbox, t, br):
    global da_factor
    if(br not in HOR_RULE_BUTTON_LIST):
        HOR_RULE_BUTTON_LIST.append(br)
    for i in RECT_NAMES:
        for rtmrln in HOR_RULE_DICT[i][t]:
            main_canvas.delete(rtmrln)
        HOR_RULE_DICT[i][t].clear()
        pg_ref=main_canvas.find_withtag(i)
        pg_ref_coords=main_canvas.coords(pg_ref)
        pg_ref_rule_width=abs(float(hor_lnstart_sbox.get())-float(hor_lnend_sbox.get()))

        numolns=int(float(hor_lnnum_sbox.get()))-1
        pg_ref_rule_diff=(pg_ref_rule_width/numolns)*da_factor
        pg_ref_lnstart=(float(hor_lnstart_sbox.get())*da_factor)+pg_ref_coords[1]
        for k in range(0,numolns+1):
            ruleln_tag=i+"_"+t+"_ln"+str(k+1)
            HOR_RULE_DICT[i][t].append(ruleln_tag)
            pg_ref_rule_coords= pg_ref_lnstart+(pg_ref_rule_diff*k)
            main_canvas.create_line(pg_ref_coords[0], pg_ref_rule_coords, pg_ref_coords[2], pg_ref_rule_coords, tag=ruleln_tag, width=(da_factor*0.2))
    if t not in HOR_RULE_RECORDS:
        HOR_RULE_RECORDS.update({t:[float(hor_lnstart_sbox.get()), float(hor_lnend_sbox.get()), int(float(hor_lnnum_sbox.get()))]})
    else:
        HOR_RULE_RECORDS[t].clear()
        HOR_RULE_RECORDS[t].append(float(hor_lnstart_sbox.get()))
        HOR_RULE_RECORDS[t].append(float(hor_lnend_sbox.get()))
        HOR_RULE_RECORDS[t].append(int(float(hor_lnnum_sbox.get())))

def Draw_Ver_Rules(ver_lnstart_sbox, ver_lnend_sbox, ver_lnnum_sbox, nrt, vbr):
    global da_factor
    if(vbr not in VER_RULE_BUTTON_LIST):
        VER_RULE_BUTTON_LIST.append(vbr)
    for i in RECT_NAMES:
        for rtnrln in VER_RULE_DICT[i][nrt]:
            main_canvas.delete(rtnrln)
        VER_RULE_DICT[i][nrt].clear()
        pg_ref=main_canvas.find_withtag(i)
        pgref_coords=main_canvas.coords(pg_ref)
        pgref_rule_length=abs(float(ver_lnstart_sbox.get())-float(ver_lnend_sbox.get()))
        numolns=int(float(ver_lnnum_sbox.get()))-1
        pgref_rule_diff=(pgref_rule_length/numolns)*da_factor
        pgref_lnstart=(float(ver_lnstart_sbox.get())*da_factor)+pgref_coords[0]
        for k in range(0,numolns+1):
            ruleln_tag=i+"_"+nrt+"_ln"+str(k+1)
            VER_RULE_DICT[i][nrt].append(ruleln_tag)
            pgref_rule_coords= pgref_lnstart+(pgref_rule_diff*k)
            main_canvas.create_line(pgref_rule_coords, pgref_coords[1], pgref_rule_coords, pgref_coords[3],tag=ruleln_tag, width=(da_factor*0.2))
    if nrt not in HOR_RULE_RECORDS:
        VER_RULE_RECORDS.update({nrt:[float(ver_lnstart_sbox.get()), float(ver_lnend_sbox.get()), int(float(ver_lnnum_sbox.get()))]})
    else:
        VER_RULE_RECORDS[nrt].clear()
        VER_RULE_RECORDS[nrt].append(float(ver_lnstart_sbox.get()))
        VER_RULE_RECORDS[nrt].append(float(ver_lnend_sbox.get()))
        VER_RULE_RECORDS[nrt].append(int(float(ver_lnnum_sbox.get())))
    
previous_cursor="arrow"
def mid_release(event):
    global previous_cursor
    main_canvas.configure(cursor=previous_cursor)

def mid_press(event):
    main_canvas.scan_mark(event.x, event.y)
    main_canvas.configure(cursor="fleur")


def mid_move(event):
    main_canvas.scan_dragto(event.x, event.y, gain=1)
    #main_canvas.create_rectangle(main_canvas.canvasx(0), main_canvas.canvasy(0), main_canvas.canvasx(0)+500, main_canvas.canvasy(0)+650, fill="blue")


Add_page=Button(Top_Tool_panel, text="PAGE+", fg="white", bg="black", command= new_slide)
Add_page.grid(row=0, column=0)

Arrow_Tool=Button(Left_Tool_panel, text="Arrow", fg="white", bg="black", command=Arrow_bind)
Arrow_Tool.grid(row=0, column=0)

Line_Tool=Button(Left_Tool_panel, text="Line", fg="white", bg="black", command= Line_bind)
Line_Tool.grid(row=1, column=0)

ph_change_var= StringVar()
ph_change_lbl=Label(Change_Page_Dimensions.frame, text="Page height: ")
ph_change_scl= Spinbox(Change_Page_Dimensions.frame, textvariable=ph_change_var, from_= 1, to= 500, width=7, increment=0.01)
ph_change_var.set('297')
ph_change_lbl.grid(row=0, column=0, padx=5, sticky=W)
ph_change_scl.grid(row=0, column=1, padx=5, sticky=W)

pl_change_var= StringVar()
pl_change_lbl=Label(Change_Page_Dimensions.frame, text="Page length: ")
pl_change_scl= Spinbox(Change_Page_Dimensions.frame, textvariable=pl_change_var, from_= 1, to= 500, width=7, increment=0.01)
pl_change_var.set('210')
pl_change_lbl.grid(row=1, column=0, padx=5, sticky=W)
pl_change_scl.grid(row=1, column=1, padx=5, sticky=W)

Save_transform=Button(Change_Page_Dimensions.frame,text="Save", fg="white", bg="black", command= save_page_transform)
Save_transform.grid(row=2, column=0, padx=5, sticky=W)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Load_Rule_File(fol_tobe_loaded):
    File_loc="Rule Saves/"+fol_tobe_loaded+"/Horizontal.txt"
    FTBLoaded=open(File_loc,"r")
    MRDict_string=FTBLoaded.read()
    NEW_MR_DICT={}
    ele=-1
    MR=""
    while(True):
        ele+=1
        if(MRDict_string[ele]=="'" and MRDict_string[ele+1]=="M"):
            while(True):
                ele+=1
                MR+=MRDict_string[ele]
                if(MRDict_string[ele+1]=="'"):
                    NEW_MR_DICT.update({MR:[]})
                    break
        if(MRDict_string[ele]=="["):
            while(True):
                MR_NUM=""
                while(True):
                    ele+=1
                    MR_NUM+=MRDict_string[ele]
                    if(MRDict_string[ele+1]=="," or MRDict_string[ele+1]=="]"):
                        ele+=1
                        NEW_MR_DICT[MR].append(float(MR_NUM))
                        break
                if(MRDict_string[ele]=="]" or MRDict_string[ele+1]=="]"):
                    MR=""
                    break
        if(MRDict_string[ele]=="}"):
            break
    FTBLoaded.close()
    VERFile_loc="Rule Saves/"+fol_tobe_loaded+"/Vertical.txt"
    FTBLoaded=open(VERFile_loc,"r")
    NRDict_string=FTBLoaded.read()
    NEW_NR_DICT={}
    Vele=-1
    NR=""
    while(True):
        Vele+=1
        if(NRDict_string[Vele]=="'" and NRDict_string[Vele+1]=="N"):
            while(True):
                Vele+=1
                NR+=NRDict_string[Vele]
                if(NRDict_string[Vele+1]=="'"):
                    NEW_NR_DICT.update({NR:[]})
                    break
        if(NRDict_string[Vele]=="["):
            while(True):
                NR_NUM=""
                while(True):
                    Vele+=1
                    NR_NUM+=NRDict_string[Vele]
                    if(NRDict_string[Vele+1]=="," or NRDict_string[Vele+1]=="]"):
                        Vele+=1
                        NEW_NR_DICT[NR].append(float(NR_NUM))
                        break
                if(NRDict_string[Vele]=="]" or NRDict_string[Vele+1]=="]"):
                    NR=""
                    break
        if(NRDict_string[Vele]=="}"):
            break
    FTBLoaded.close()
    while(len(HOR_DEL_BUTTON_LIST)!=0):
        for RDB_ele in HOR_DEL_BUTTON_LIST:
            RDB_ele.invoke()
    while(len(VER_DEL_BUTTON_LIST)!=0):
        for RDB_ele in VER_DEL_BUTTON_LIST:
            RDB_ele.invoke()
    for fileMRS in NEW_MR_DICT:
        Add_HR_CP(1, NEW_MR_DICT[fileMRS])
    for fileNRS in NEW_NR_DICT:
        Add_VER_CP(1, NEW_NR_DICT[fileNRS])
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Load_Rules=cp(Multiple_Rule_Lines.frame, expanded_text='Load', collapsed_text= 'Load', bg='black', fg='white')
Load_Rules.grid(row=1, column=0, pady=5, padx=10, sticky=W)

def lbl_mouse_enter(event, lbli):
    lbl_list[lbli].config(bg="white", fg="black")
def lbl_mouse_leave(event, lbli):
    lbl_list[lbli].config(bg="black", fg="white")
def lbl_press(event, row_num, filename):
    for ld_butt in load_butt_list:
        ld_butt.destroy()
    load_button=Button(Load_Rules.frame, text="Load", fg="white", bg="black", command=lambda fol_tobe_loaded=filename: Load_Rule_File(fol_tobe_loaded))
    load_button.grid(row=row_num, column=1, padx=5, pady=5, sticky=W)
    load_butt_list.append(load_button)

textfile_list=os.listdir("Rule Saves")
load_butt_list=[]
lbl_list=[]
textfile_counter=0
for folders in textfile_list:
    lbl=Label(Load_Rules.frame, text=folders, bd=3, relief='sunken', bg="black", fg="white")
    lbl.grid(row=textfile_counter, column=0, padx=5, pady=5, sticky=W)
    lbl_list.append(lbl)
    lbl.bind("<Enter>", lambda event, lbli=textfile_counter: lbl_mouse_enter(event, lbli))
    lbl.bind("<Leave>", lambda event, lbli=textfile_counter: lbl_mouse_leave(event, lbli))
    lbl.bind("<Button-1>", lambda event, row_num=textfile_counter, filename=folders: lbl_press(event, row_num, filename))
    textfile_counter+=1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------------------------------------------------------------
HOR_RULE_DICT={"RT1":{}} #{"R1":{"MR1":[], "MR2":[],......}, "R2":{"MR1":[], "MR2":[],......},..............}
HOR_RULE_RECORDS={}      #{"MR1":[], "MR2":[], "MR3":[], "MR4":[]..................}
HOR_RULE_BUTTON_LIST=[] #stores savehorlines buttons to call Draw_Hor_Rules
HOR_DEL_BUTTON_LIST=[] #stores delete buttons
HR_CP_num=0
def Add_HR_CP(AHP, AHL):
    global HR_CP_num
    HR_CP_num+=1
    HR_CP_name="Rule "+str(HR_CP_num)
    HR_CP=cp(Horizontal_Rules.frame, HR_CP_name, HR_CP_name, 'black', 'white')
    HR_CP.grid(row=(HR_CP_num-1), column=0, padx=5, pady=5, sticky=W)
    
    if(Horizontal_Rules._isactive()):
        pass
    else:
        Horizontal_Rules.toggle()

    def delete_HRCP(dt, But_Ref, Del_But_ref):
        del_detect_mr=[]
        for delrt in RECT_NAMES:
            for delmr in HOR_RULE_DICT[delrt]:
                if(delmr==dt):
                    for delrln in HOR_RULE_DICT[delrt][delmr]:
                        main_canvas.delete(delrln)
                    if delmr in del_detect_mr:
                        pass
                    else:
                        del_detect_mr.append(delmr)
        for delrt in RECT_NAMES:
            for del_mr in del_detect_mr:
                HOR_RULE_DICT[delrt].pop(del_mr)
        del_detect_mr.clear()
        HR_CP.destroy()
        del_HR_CP.destroy()
        Horizontal_Rules.no_kin()
        if But_Ref in HOR_RULE_BUTTON_LIST:
            HOR_RULE_BUTTON_LIST.remove(But_Ref)
        if Del_But_ref in HOR_DEL_BUTTON_LIST:
            HOR_DEL_BUTTON_LIST.remove(Del_But_ref)

    HR_CP_tag="MR"+str(HR_CP_num)

    hor_lnstart_sbox_var= StringVar()
    hor_lnstart_sbox_lbl=Label(HR_CP.frame, text="Line Start: ")
    hor_lnstart_sbox_lbl.grid(row=0, column=0, padx=5, sticky=W)
    hor_lnstart_sbox=Spinbox(HR_CP.frame, textvariable=hor_lnstart_sbox_var, from_=0, to=float(ph_change_scl.get()), width=7, increment=0.01)
    if(AHP==1):
        hor_lnstart_sbox_var.set(str(AHL[0]))
    hor_lnstart_sbox.grid(row=0, column=1, padx=5, sticky=W)

    hor_lnend_sbox_var= StringVar()
    hor_lnend_sbox_lbl=Label(HR_CP.frame, text="Line End: ")
    hor_lnend_sbox_lbl.grid(row=1, column=0, padx=5, sticky=W)
    hor_lnend_sbox=Spinbox(HR_CP.frame, textvariable=hor_lnend_sbox_var, from_=0, to=float(ph_change_scl.get()), width=7, increment=0.01)
    if(AHP==1):
        hor_lnend_sbox_var.set(str(AHL[1]))
    hor_lnend_sbox.grid(row=1, column=1, padx=5, sticky=W)

    hor_lnnum_sbox_var= StringVar()
    hor_lnnum_sbox_lbl=Label(HR_CP.frame, text="No. Of Lines: ")
    hor_lnnum_sbox_lbl.grid(row=2, column=0, padx=5, sticky=W)
    hor_lnnum_sbox=Spinbox(HR_CP.frame, textvariable=hor_lnnum_sbox_var, from_=2, to=500, width=5)
    if(AHP==1):
        hor_lnnum_sbox_var.set(str(AHL[2]))
    hor_lnnum_sbox.grid(row=2, column=1, padx=5, sticky=W)

    for rt in RECT_NAMES:
        HOR_RULE_DICT[rt].update({HR_CP_tag:[]}) 

    Save_horlines=Button(HR_CP.frame, text="Draw Lines", fg="white", bg="black")
    Save_horlines['command']=lambda t=HR_CP_tag, br=Save_horlines: Draw_Hor_Rules(hor_lnstart_sbox, hor_lnend_sbox, hor_lnnum_sbox, t, br)
    Save_horlines.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    if(AHP==1):
        Save_horlines.invoke()

    del_HR_CP=Button(Horizontal_Rules.frame, text="-", fg="white", bg="black")
    del_HR_CP['command']= lambda dt=HR_CP_tag, But_Ref=Save_horlines, Del_But_ref=del_HR_CP: delete_HRCP(dt, But_Ref, Del_But_ref)
    del_HR_CP.grid(row=(HR_CP_num-1), column=1, padx=5, pady=5, sticky=NW)

    if(del_HR_CP not in HOR_DEL_BUTTON_LIST):
        HOR_DEL_BUTTON_LIST.append(del_HR_CP)
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
Horizontal_Rules=cp(Multiple_Rule_Lines.frame, 'Horizontal', 'Horizontal', 'black', 'white')
Horizontal_Rules.grid(row=2, column=0, pady=5, padx=10, sticky=W)
Add_HR_Parameter=0
Add_HR_list=[]
Add_HR=Button(Multiple_Rule_Lines.frame, fg='white', bg='black', text="+", command=lambda AHP=Add_HR_Parameter, AHL=Add_HR_list: Add_HR_CP(AHP, AHL))
Add_HR.grid(row=2, column=1, pady=5, padx=10, sticky=NW)
Add_HR.configure(state=DISABLED)
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#HOR_RULE_DICT={"RT1":{}} #{"R1":{"MR1":[], "MR2":[],......}, "R2":{"MR1":[], "MR2":[],......},..............}
#HOR_RULE_RECORDS={}      #{"MR1":[], "MR2":[], "MR3":[], "MR4":[]..................}
VER_RULE_DICT={"RT1":{}}
VER_RULE_RECORDS={}
VER_RULE_BUTTON_LIST=[]
VER_DEL_BUTTON_LIST=[] 
VER_CP_num=0
def Add_VER_CP(AVP, AVL):
    global VER_CP_num
    VER_CP_num+=1
    VER_CP_name="Rule "+str(VER_CP_num)
    VER_CP=cp(Vertical_Rules.frame, VER_CP_name, VER_CP_name, 'black', 'white')
    VER_CP.grid(row=(VER_CP_num-1), column=0, padx=5, pady=5, sticky=W)

    if(Vertical_Rules._isactive()):
        pass
    else:
        Vertical_Rules.toggle()

    def delete_VERCP(dt, But_Ref, Del_But_ref):
        del_detect_nr=[]
        for delrt in RECT_NAMES:
            for delnr in VER_RULE_DICT[delrt]:
                if(delnr==dt):
                    for delrln in VER_RULE_DICT[delrt][delnr]:
                        main_canvas.delete(delrln)
                    if delnr in del_detect_nr:
                        pass
                    else:
                        del_detect_nr.append(delnr)
        for delrt in RECT_NAMES:
            for del_nr in del_detect_nr:
                VER_RULE_DICT[delrt].pop(del_nr)
        del_detect_nr.clear()
        VER_CP.destroy()
        del_VER_CP.destroy()
        Vertical_Rules.no_kin()
        if But_Ref in VER_RULE_BUTTON_LIST:
            VER_RULE_BUTTON_LIST.remove(But_Ref)
        if Del_But_ref in VER_DEL_BUTTON_LIST:
            VER_DEL_BUTTON_LIST.remove(Del_But_ref)

    VER_CP_tag="NR"+str(VER_CP_num)

    ver_lnstart_sbox_var= StringVar()
    ver_lnstart_sbox_lbl=Label(VER_CP.frame, text="Line Start: ")
    ver_lnstart_sbox_lbl.grid(row=0, column=0, padx=5, sticky=W)
    ver_lnstart_sbox=Spinbox(VER_CP.frame, textvariable=ver_lnstart_sbox_var, from_=0, to=float(pl_change_scl.get()), width=7, increment=0.01)
    if(AVP==1):
        ver_lnstart_sbox_var.set(str(AVL[0]))
    ver_lnstart_sbox.grid(row=0, column=1, padx=5, sticky=W)

    ver_lnend_sbox_var= StringVar()
    ver_lnend_sbox_lbl=Label(VER_CP.frame, text="Line End: ")
    ver_lnend_sbox_lbl.grid(row=1, column=0, padx=5, sticky=W)
    ver_lnend_sbox=Spinbox(VER_CP.frame, textvariable=ver_lnend_sbox_var, from_=0, to=float(pl_change_scl.get()), width=7, increment=0.01)
    if(AVP==1):
        ver_lnend_sbox_var.set(str(AVL[1]))
    ver_lnend_sbox.grid(row=1, column=1, padx=5, sticky=W)

    ver_lnnum_sbox_var= StringVar()
    ver_lnnum_sbox_lbl=Label(VER_CP.frame, text="No. Of Lines: ")
    ver_lnnum_sbox_lbl.grid(row=2, column=0, padx=5, sticky=W)
    ver_lnnum_sbox=Spinbox(VER_CP.frame, textvariable=ver_lnnum_sbox_var, from_=2, to=500, width=5)
    if(AVP==1):
        ver_lnnum_sbox_var.set(str(AVL[2]))
    ver_lnnum_sbox.grid(row=2, column=1, padx=5, sticky=W)

    for rt in RECT_NAMES:
        VER_RULE_DICT[rt].update({VER_CP_tag:[]}) 

    Save_verlines=Button(VER_CP.frame, text="Draw Lines", fg="white", bg="black")
    Save_verlines['command']=lambda nrt=VER_CP_tag, vbr=Save_verlines: Draw_Ver_Rules(ver_lnstart_sbox, ver_lnend_sbox, ver_lnnum_sbox, nrt, vbr)
    Save_verlines.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    if(AVP==1):
        Save_verlines.invoke()

    del_VER_CP=Button(Vertical_Rules.frame, text="-", fg="white", bg="black")
    del_VER_CP['command']= lambda dt=VER_CP_tag, But_Ref=Save_verlines, Del_But_ref=del_VER_CP: delete_VERCP(dt, But_Ref, Del_But_ref)
    del_VER_CP.grid(row=(VER_CP_num-1), column=1, padx=5, pady=5, sticky=NW)

    if(del_VER_CP not in VER_DEL_BUTTON_LIST):
        VER_DEL_BUTTON_LIST.append(del_VER_CP)
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Vertical_Rules=cp(Multiple_Rule_Lines.frame, 'Vertical', 'Vertical', 'black', 'white')
Vertical_Rules.grid(row=3, column=0, pady=5, padx=10, sticky=W)
Add_VER_Parameter=0
Add_VER_list=[]
Add_VER=Button(Multiple_Rule_Lines.frame, fg='white', bg='black', text="+", command=lambda AVP=Add_VER_Parameter, AVL=Add_VER_list: Add_VER_CP(AVP, AVL))
Add_VER.grid(row=3, column=1, pady=5, padx=10, sticky=NW)
Add_VER.configure(state=DISABLED)
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def Rule_File_Create():
    RFilename="Rule Saves/"+Rule_File_Name.get()
    if((Rule_File_Name.get()) in textfile_list):
        messagebox.showwarning("Warning", "File Name Already Exists!")
    elif(len(Rule_File_Name.get())==0):
        messagebox.showwarning("Warning", "File Name Cannot be Empty!")
    else:
        os.makedirs(RFilename)
        textfile_list.append(str(Rule_File_Name.get()))
        Rfile=open(RFilename+"/Horizontal.txt","w")
        Rfile.write(str(HOR_RULE_RECORDS))
        Rfile.close()
        Rfile=open(RFilename+"/Vertical.txt","w")
        Rfile.write(str(VER_RULE_RECORDS))
        Rfile.close
        Rule_File_Name.configure(state=DISABLED)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Save_Rule_Files=cp(Multiple_Rule_Lines.frame, 'Create Save', 'Create Save', 'black', 'white')
Save_Rule_Files._change(NewState="DISABLED")
Save_Rule_Files.grid(row=4, column=0, pady=5, padx=10, sticky=W)
Rule_File_Name=Entry(Save_Rule_Files.frame)
Rule_File_Name.grid(row=0, column=0, pady=5, padx=10, sticky=W)
RuleFile_SaveButton=Button(Save_Rule_Files.frame, text="Save File", fg='white', bg='black', command= Rule_File_Create)
RuleFile_SaveButton.grid(row=0, column=1, pady=5, padx=10, sticky=W)
#RuleFile_SaveButton.configure(state=DISABLED)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
def Window_Selected(value):
    return
#--------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------

CW_options=["Edit PDF", "Customize Letters"]
Selected_Window=StringVar()
Selected_Window.set(CW_options[0])
Choose_window=OptionMenu(Win_Chnage_panel, Selected_Window, *CW_options, command=Window_Selected)
Choose_window.grid(row=0, column=0, sticky=NW)
Choose_window.configure(bg="black", fg="white")

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------



EDITOR_BINDS=['<ButtonPress-1>','<B1-Motion>','<ButtonRelease-1>']

main_canvas.bind('<MouseWheel>', do_zoom)
main_canvas.bind('<ButtonPress-2>', mid_press)
main_canvas.bind('<B2-Motion>', mid_move)
main_canvas.bind('<ButtonRelease-2>', mid_release)

root.bind('<Control-a>', lambda event: print("A was pressed"))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PENCIL_RECORDS=[]
pwidth_factor=1
pnum=0
pstarted=0
def pencil_start(event):
    global pencilx, pencily, pstarted, pnum
    pencilx=main_canvas.canvasx(event.x)
    pencily=main_canvas.canvasy(event.y)
    pnum+=1
    pstarted=1

def pencil_move(event):
    global pencilx, pencily, pnum, da_factor
    ptag="pline"+str(pnum)
    PENCIL_RECORDS.append(ptag)
    main_canvas.create_oval(pencilx-da_factor, pencily-da_factor, pencilx+da_factor, pencily+da_factor, tag=ptag, fill="black")
    pencilx=main_canvas.canvasx(event.x)
    pencily=main_canvas.canvasy(event.y)
    pnum+=1

#def pencil_width_change(event):
#    global pwidth_factor
#    if(event.delta>0):
#        pwidth_factor+=0.127429248861097
#        for ptags in PENCIL_RECORDS:
#            pmemo=main_canvas.find_withtag(ptags)
#            main_canvas.itemconfig(pmemo, width=pwidth_factor)
#
#    if(event.delta<0):
#        pwidth_factor-=0.127429248861097
#        for ptags in PENCIL_RECORDS:
#            pmemo=main_canvas.find_withtag(ptags)
#            main_canvas.itemconfig(pmemo, width=pwidth_factor)
    

def Pencil_bind():
    global previous_cursor
    for i in EDITOR_BINDS:
        main_canvas.unbind(i)
    main_canvas.configure(cursor="target")
    previous_cursor="target"
    main_canvas.bind('<ButtonPress-1>', pencil_start)
    main_canvas.bind('<B1-Motion>', pencil_move)
    #This Doesn't work just set distance between two letters

Pencil_Tool=Button(Left_Tool_panel, text="Pencil", fg="white", bg="black", command= Pencil_bind)
Pencil_Tool.grid(row=2, column=0)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()