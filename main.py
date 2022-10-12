
from tkinter import END, EW, NS, NSEW, StringVar, Tk, ttk, font
import os

class App:
    def __init__(self):
        self.init_ui()
    
    def cmp_mac(self):
        mac1 = self.et1.get()
        mac2 = self.et2.get()
        mac3 = ""
        val = self.select.get();
        
        # print(mac1, mac2)
        self.m1.config(text=mac1)
        self.m2.config(text=mac2)
        if(val == "摩托车"):
            mac3 = self.et3.get()
            self.m3.config(text=mac3)

        if (val != "摩托车" and mac1 == mac2) or (val == "摩托车" and mac1 == mac2 and mac2 == mac3):
            self.lb_result.configure(text="相同", foreground='green')
        else:
            self.lb_result.configure(text="不相同", foreground="red")

    def et1_enter_press(self, e):
        self.lb_result.configure(text='')
        self.m1.configure(text='')
        self.m2.configure(text='')
        self.et2.focus()
    
    def do_cmp_and_write_result(self):
        self.cmp_mac()
        val = self.select.get()

        mac1 = self.et1.get()
        mac2 = self.et2.get()
        mac3 = ""
        result = self.lb_result.cget("text")
        self.et1.delete(0, END)
        self.et2.delete(0, len(mac2))
        if(val == "摩托车"):
            mac3 = self.et3.get()
            self.et3.delete(0, len(mac3))
        self.et1.focus()
        file_exists = False
        filename = val + "_result.csv"
        if os.path.exists(filename):
            file_exists = True
        lines = []
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            pass
        
        with open(filename, mode="a") as f:
            if not file_exists:
                if val != "摩托车":
                    f.write("蓝牙卡条码,充电桩条码,对比结果\n")
                else:
                    f.write("钥匙1条码,钥匙1条码,摩托车条码,对比结果\n")
            exists = False
            for line in lines:
                ll = line.strip('\n').split(',')
                if val == "摩托车":
                    if ll[0] == mac1 and ll[1] == mac2 and ll[2] == mac3:
                        exists = True
                        break
                else:
                    if ll[0] == mac1 and ll[1] == mac2:
                        exists = True
                        break
            
            if not exists:
                if val != "摩托车":
                    f.write(mac1+ "," + mac2 + "," + result+"\n")
                else:
                    f.write(mac1+ "," + mac2 + "," + mac3 + "," + result+"\n")

    def et2_enter_press(self, e):
        val = self.select.get()
        if(val == "摩托车"):
            self.et3.focus()
            return

        self.do_cmp_and_write_result()

    def et3_enter_press(self, e):
        self.do_cmp_and_write_result()

        
    def rd_btn_click(self):
        val = self.select.get()
        if(val == "充电桩"):
            self.lb1.configure(text="蓝牙卡条码")
            self.lb2.configure(text="充电桩条码")
            self.lb3.grid_forget();
            self.et3.grid_forget();
        else:
            self.lb1.configure(text="钥匙1条码")
            self.lb2.configure(text="钥匙2条码")
            self.lb3.grid(column=2, row=0, padx=5, pady=5, sticky=EW)
            self.et3.grid(column=2, row=1, padx=5, pady=5, sticky=EW)
        

    
    def init_ui(self):
        mw = Tk()
        mw.geometry("450x250")

        self.select = StringVar()
        self.select.set("充电桩")

        frmSelect = ttk.Frame(mw, padding=10)
        frmSelect.grid(column=0, row=0, sticky=NSEW)
        rd1 = ttk.Radiobutton(frmSelect, text="充电桩", value="充电桩", variable=self.select, command=self.rd_btn_click)
        rd1.grid(column=0, row=0, sticky=EW)
        rd2 = ttk.Radiobutton(frmSelect, text="摩托车", value="摩托车", variable=self.select, command=self.rd_btn_click)
        rd2.grid(column=1, row=0, sticky=EW)

        frm = ttk.Frame(mw, padding=10)
        frm.grid(sticky=NSEW)
        font1 = font.Font(family="幼圆", size=16)
        font2 = font.Font(family="幼圆", size=14)
        font3 = font.Font(family="幼圆", size=50, weight=font.BOLD)
        # print(font.families(mw))
        
        self.lb1 = ttk.Label(frm, text="蓝牙卡条码", font=font1)
        self.lb1.grid(column=0, row=0, padx=5, pady=5, sticky=EW)
        self.lb2 = ttk.Label(frm, text="充电桩条码", font=font1)
        self.lb2.grid(column=1, row=0, padx=5, pady=5, sticky=EW)
        self.lb3 = ttk.Label(frm, text="摩托车条码", font=font1)
        # self.lb3.grid(column=2, row=0, padx=5, pady=5, sticky=EW)

        self.et1 = ttk.Entry(frm, font=font2, width=12)
        self.et1.grid(column=0, row=1, padx=5, pady=5, sticky=EW)
        self.et2 = ttk.Entry(frm, font=font2, width=12)        
        self.et2.grid(column=1, row=1, padx=5, pady=5, sticky=EW)
        self.et3 = ttk.Entry(frm, font=font2, width=12)        
        # self.et3.grid(column=2, row=1, padx=5, pady=5, sticky=EW)

        self.m1 = ttk.Label(frm, text='', font=font2)
        self.m2 = ttk.Label(frm, text='', font=font2)
        self.m1.grid(column=0, row=2, padx=5, pady=5 )
        self.m2.grid(column=1, row=2, padx=5, pady=5)
        self.m3 = ttk.Label(frm, text='', font=font2)
        self.m3.grid(column=2, row=2, padx=5, pady=5 )

        self.lb_result = ttk.Label(frm, text="", font=font3)
        self.lb_result.grid(column=0, columnspan=3, row=3, sticky=NS)

        self.et1.bind("<Return>", self.et1_enter_press)
        self.et2.bind("<Return>", self.et2_enter_press)
        self.et3.bind("<Return>", self.et3_enter_press)
        # self.et1.bind("<KeyRelease>", self.cmp_mac)
        # self.et2.bind("<KeyRelease>", self.cmp_mac)
        self.et1.focus()
        # self.lb_result.config(foreground="red")
        # mw.columnconfigure(0, weight=1)
        frm.columnconfigure(0, weight=1)
        frm.columnconfigure(1, weight=1)
        frm.rowconfigure(1, weight=1)
        mw.title("MAC比较工具")
        mw.mainloop()

if __name__== "__main__":
    app = App()
    

