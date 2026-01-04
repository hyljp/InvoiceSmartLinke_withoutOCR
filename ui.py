"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class WinGUI(ttk.Window):
    def __init__(self):
        super().__init__(themename="litera")
        self.__win()
        self.tk_button_OPEN_FOLDER_BTN = self.__tk_button_OPEN_FOLDER_BTN(self)
        self.tk_canvas_SHOW_PICTURE = self.__tk_canvas_SHOW_PICTURE(self)
        self.tk_select_box_OS_CHOICE = self.__tk_select_box_OS_CHOICE(self)
        self.tk_label_m1lpeeg9 = self.__tk_label_m1lpeeg9(self)
        self.tk_label_SHOW_PIC_PATH = self.__tk_label_SHOW_PIC_PATH(self)
        self.tk_button_PRE_PIC_BTN = self.__tk_button_PRE_PIC_BTN(self)
        self.tk_button_NEXT_PIC_BTN = self.__tk_button_NEXT_PIC_BTN(self)
        self.tk_button_OCR_BTN = self.__tk_button_OCR_BTN(self)
        self.tk_label_frame_CATEGORY_CONTAINER = self.__tk_label_frame_CATEGORY_CONTAINER(self)
        self.tk_select_box_AccountKind = self.__tk_select_box_AccountKind( self.tk_label_frame_CATEGORY_CONTAINER)
        self.tk_label_m1lqqmcv = self.__tk_label_m1lqqmcv( self.tk_label_frame_CATEGORY_CONTAINER)
        self.tk_label_m1lqr407 = self.__tk_label_m1lqr407( self.tk_label_frame_CATEGORY_CONTAINER)
        self.tk_select_box_AccountItem = self.__tk_select_box_AccountItem( self.tk_label_frame_CATEGORY_CONTAINER)
        self.tk_button_WRITE_EXCEL_BTN = self.__tk_button_WRITE_EXCEL_BTN(self)
        self.tk_label_frame_MD_CONTAINER = self.__tk_label_frame_MD_CONTAINER(self)
        self.tk_label_m1vqsi1l = self.__tk_label_m1vqsi1l( self.tk_label_frame_MD_CONTAINER)
        self.tk_label_m1vqswfo = self.__tk_label_m1vqswfo( self.tk_label_frame_MD_CONTAINER)
        self.tk_input_PRICE_INPUT = self.__tk_input_PRICE_INPUT( self.tk_label_frame_MD_CONTAINER)
        self.tk_input_DATE_INPUT = self.__tk_input_DATE_INPUT( self.tk_label_frame_MD_CONTAINER)
        self.tk_label_frame_m1vrfz9j = self.__tk_label_frame_m1vrfz9j(self)
        self.tk_input_COMMENT_INPUTG = self.__tk_input_COMMENT_INPUTG( self.tk_label_frame_m1vrfz9j)
        self.tk_button_ROTATE_BTN = self.__tk_button_ROTATE_BTN(self)

    def __win(self):
        self.title("InvoiceSmartLink")
        # 设置窗口大小、居中
        width = 800
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.minsize(width=width, height=height)

    def __tk_button_OPEN_FOLDER_BTN(self,parent):
        btn = ttk.Button(parent, text="画像フォルダを選択", takefocus=False, bootstyle="primary")
        btn.place(relx=0.4250, rely=0.0100, relwidth=0.1688, relheight=0.0500)
        return btn

    def __tk_canvas_SHOW_PICTURE(self,parent):
        canvas = ttk.Canvas(parent,bg="#aaa")
        canvas.place(relx=0.0375, rely=0.1200, relwidth=0.6000, relheight=0.8000)
        # サイズ変更イベントをバインド
        canvas.bind("<Configure>", self.on_canvas_resize)
        self.canvas = canvas  # Canvasをインスタンス変数として保持
        return canvas

    def on_canvas_resize(self, event):
        # Canvasのサイズが変更されたときに画像を再描画
        if hasattr(self, 'controller') and self.controller:
            self.controller.redraw_image()

    def __tk_select_box_OS_CHOICE(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("windows","mac os")
        cb.place(relx=0.1750, rely=0.0100, relwidth=0.1875, relheight=0.05)
        return cb

    def __tk_label_m1lpeeg9(self,parent):
        label = ttk.Label(parent,text="システム選択",anchor="center", )
        label.place(relx=0.0375, rely=0.0100, relwidth=0.1250, relheight=0.05)
        return label

    def __tk_label_SHOW_PIC_PATH(self,parent):
        label = ttk.Label(parent,text="パスが指定されていません",anchor="center", )
        label.place(relx=0.0375, rely=0.0700, relwidth=0.6000, relheight=0.0400)
        return label

    def __tk_button_PRE_PIC_BTN(self,parent):
        btn = ttk.Button(parent, text="< 前へ", takefocus=False, bootstyle="secondary")
        btn.place(relx=0.0688, rely=0.9400, relwidth=0.08, relheight=0.05)
        return btn

    def __tk_button_NEXT_PIC_BTN(self,parent):
        btn = ttk.Button(parent, text="次へ >", takefocus=False, bootstyle="secondary")
        btn.place(relx=0.34, rely=0.9400, relwidth=0.08, relheight=0.05)
        return btn

    def __tk_button_OCR_BTN(self,parent):
        btn = ttk.Button(parent, text="画像を識別", takefocus=False, bootstyle="primary-outline")
        btn.place(relx=0.1663, rely=0.9400, relwidth=0.1675, relheight=0.05)
        return btn

    def __tk_label_frame_CATEGORY_CONTAINER(self,parent):
        frame = ttk.LabelFrame(parent,text="勘定科目",)
        frame.place(relx=0.6500, rely=0.0200, relwidth=0.3125, relheight=0.3400)
        return frame

    def __tk_select_box_AccountKind(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(relx=0.0400, rely=0.2353, relwidth=0.9200, relheight=0.1765)
        return cb

    def __tk_label_m1lqqmcv(self,parent):
        label = ttk.Label(parent,text="種類",anchor="center", )
        label.place(relx=0.0400, rely=0.0294, relwidth=0.2000, relheight=0.1765)
        return label

    def __tk_label_m1lqr407(self,parent):
        label = ttk.Label(parent,text="項目",anchor="center", )
        label.place(relx=0.0400, rely=0.4412, relwidth=0.2000, relheight=0.1765)
        return label

    def __tk_select_box_AccountItem(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(relx=0.0400, rely=0.6471, relwidth=0.9200, relheight=0.1765)
        return cb

    def __tk_button_WRITE_EXCEL_BTN(self,parent):
        btn = ttk.Button(parent, text="書き込み", takefocus=False, bootstyle="success")
        btn.place(relx=0.72, rely=0.88, relwidth=0.18, relheight=0.08)
        return btn

    def __tk_label_frame_MD_CONTAINER(self,parent):
        frame = ttk.LabelFrame(parent,text="レシート情報",)
        frame.place(relx=0.6500, rely=0.4000, relwidth=0.3125, relheight=0.2000)
        return frame

    def __tk_label_m1vqsi1l(self,parent):
        label = ttk.Label(parent,text="価額",anchor="center", )
        label.place(relx=0.0160, rely=0.0500, relwidth=0.2000, relheight=0.3000)
        return label

    def __tk_label_m1vqswfo(self,parent):
        label = ttk.Label(parent,text="日付",anchor="center", )
        label.place(relx=0.0200, rely=0.4000, relwidth=0.2000, relheight=0.3000)
        return label

    def __tk_input_PRICE_INPUT(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.2400, rely=0.0500, relwidth=0.7200, relheight=0.3000)
        return ipt

    def __tk_input_DATE_INPUT(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.2400, rely=0.4000, relwidth=0.7200, relheight=0.3000)
        return ipt

    def __tk_label_frame_m1vrfz9j(self,parent):
        frame = ttk.LabelFrame(parent,text="Comment",)
        frame.place(relx=0.6500, rely=0.6200, relwidth=0.3125, relheight=0.1600)
        return frame

    def __tk_input_COMMENT_INPUTG(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.0600, rely=0.0250, relwidth=0.9200, relheight=0.3750)
        return ipt

    def __tk_button_ROTATE_BTN(self,parent):
        btn = ttk.Button(parent, text="回転", takefocus=False, bootstyle="info-outline")
        btn.place(relx=0.5125, rely=0.9400, relwidth=0.08, relheight=0.05)
        return btn

class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.ctl.init(self)
        
    def __event_bind(self):
        self.tk_button_OPEN_FOLDER_BTN.bind('<Button-1>',self.ctl.chooseFolder)
        self.tk_button_PRE_PIC_BTN.bind('<Button-1>',self.ctl.showPrePic)
        self.tk_button_NEXT_PIC_BTN.bind('<Button-1>',self.ctl.showNextPic)
        self.tk_button_OCR_BTN.bind('<Button-1>',self.ctl.picOCR)
        self.tk_button_WRITE_EXCEL_BTN.bind('<Button-1>',self.ctl.WriteData2Excel)
        self.tk_select_box_AccountKind.bind("<<ComboboxSelected>>", self.ctl.on_account_kind_change)
        self.tk_button_ROTATE_BTN.bind('<Button-1>',self.ctl.rotateImage)
        pass

if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()