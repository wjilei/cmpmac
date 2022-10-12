
from posixpath import split
from tkinter import EW, NS, NSEW, Tk, ttk, font
import os

class App:
    def __init__(self):
        self.init_ui()
    
    def cmp_mac(self, e):
        mac1 = self.et1.get()
        mac2 = self.et2.get()
        # print(mac1, mac2)
        self.m1.config(text=mac1)
        self.m2.config(text=mac2)

        if mac1 == mac2:
            self.lb_result.configure(text="相同", foreground='green')
        else:
            self.lb_result.configure(text="不相同", foreground="red")

    def et1_enter_press(self, e):
        self.lb_result.configure(text='')
        self.m1.configure(text='')
        self.m2.configure(text='')
        self.et2.focus()
    
    def et2_enter_press(self, e):
        
        self.cmp_mac(e)

        mac1 = self.et1.get()
        mac2 = self.et2.get()
       
        result = self.lb_result.cget("text")
        self.et1.delete(0, len(mac1))
        self.et2.delete(0, len(mac2))
        self.et1.focus()
        file_exists = False
        filename = "result.csv"
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
                f.write("蓝牙卡条码,充电桩条码,对比结果\n")
            exists = False
            for line in lines:
                ll = line.strip('\n').split(',')
                if ll[0] == mac1 and ll[1] == mac2:
                    exists = True
                    break
            
            if not exists:
                f.write(mac1+ "," + mac2 + ", " + result+"\n")
        

    
    def init_ui(self):
        mw = Tk()
        mw.geometry("450x250")
        frm = ttk.Frame(mw, padding=10)
        frm.grid(sticky=NSEW)
        font1 = font.Font(family="幼圆", size=16)
        font2 = font.Font(family="幼圆", size=14)
        font3 = font.Font(family="幼圆", size=50, weight=font.BOLD)
        # print(font.families(mw))

        ttk.Label(frm, text="蓝牙卡条码", font=font1).grid(column=0, row=0, padx=5, pady=5, sticky=EW)
        ttk.Label(frm, text="充电桩条码", font=font1).grid(column=1, row=0, padx=5, pady=5, sticky=EW)

        self.et1 = ttk.Entry(frm, font=font2)
        self.et2 = ttk.Entry(frm, font=font2)
        self.et1.grid(column=0, row=1, padx=5, pady=5, sticky=EW)
        self.et2.grid(column=1, row=1, padx=5, pady=5, sticky=EW)

        self.m1 = ttk.Label(frm, text='', font=font2)
        self.m2 = ttk.Label(frm, text='', font=font2)
        self.m1.grid(column=0, row=2, padx=5, pady=5 )
        self.m2.grid(column=1, row=2, padx=5, pady=5)

        self.lb_result = ttk.Label(frm, text="", font=font3)
        self.lb_result.grid(column=0, columnspan=2, row=3, sticky=NS)

        self.et1.bind("<Return>", self.et1_enter_press)
        self.et2.bind("<Return>", self.et2_enter_press)
        # self.et1.bind("<KeyRelease>", self.cmp_mac)
        # self.et2.bind("<KeyRelease>", self.cmp_mac)
        self.et1.focus()
        # self.lb_result.config(foreground="red")
        mw.columnconfigure(0, weight=1)
        frm.columnconfigure(0, weight=1)
        frm.columnconfigure(1, weight=1)
        frm.rowconfigure(1, weight=1)
        mw.title("MAC比较工具")
        mw.mainloop()

if __name__== "__main__":
    app = App()
    

