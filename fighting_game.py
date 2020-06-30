import tkinter as tk
import tkinter.filedialog as fl
import tkinter.messagebox as mb
from PIL import Image, ImageTk

ASAKURA = 'player2.png'
MAKUREGA = 'player1.png'
VS = 'vs.png'

#朝倉の技
hp_asakura = 150
mp_asakura = 0
jab_asakura = 10
kick_asakura = 10
hiza_asakura = 30
tobihiza_asakura = 40

#マクレガーの技
hp_makurega = 100
mp_makurega = 0
jab_makurega = 20
kick_makurega = 10
straight_makurega = 20
spinKick_makurega = 30

#mp
mp_jab = 20
mp_kick = 10
mp_fuck = -30
mp_hissatu = -100

class Game(tk.Frame):

    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.width = 1000
        self.height = 700
        master.geometry(str(self.width)+"x"+str(self.height)) #ウィンドウ生成

        master.title("Fighting GAME")
        #self.master.config(bg = "black")
        self.createWidgets()

    def createWidgets(self):
        #画像配置
        asakura_picure = Image.open(ASAKURA)
        self.asakura_picure = ImageTk.PhotoImage(asakura_picure)
        makurega_picture = Image.open(MAKUREGA) 
        self.makurega_picure = ImageTk.PhotoImage(makurega_picture)  
        vs_picture = Image.open(VS) 
        self.vs_picure = ImageTk.PhotoImage(vs_picture)  
        canvas = tk.Canvas(bg="black", width=1000, height=650)
        canvas.place(x=0, y=0)
        canvas.create_image(650, 30, image = self.asakura_picure, anchor=tk.NW)
        canvas.create_image(30, 30, image = self.makurega_picure, anchor=tk.NW)
        canvas.create_image(430, 200, image = self.vs_picure, anchor=tk.NW)   

        #朝倉のボタン
        self.btn1 = tk.Button(self.master,text = u'ジャブ',command = self.player2_jab)
        self.btn1.place(x = 700,y = 500)   

        self.btn2 = tk.Button(self.master,text = u'蹴り',command = self.player2_kick)
        self.btn2.place(x = 850,y = 500)

        self.btn3 = tk.Button(self.master,text = u'フック',command = self.player2_fuck)
        self.btn3.place(x = 700,y = 550)

        self.btn4 = tk.Button(self.master,text = u'飛び膝蹴り',command = self.player2_tobihiza)
        self.btn4.place(x = 850,y = 550)



        #マクレガーのボタン
        self.btn5 = tk.Button(self.master,text = u'ジャブ',command = self.player1_jab)
        self.btn5.place(x = 30,y = 500)

        self.btn6 = tk.Button(self.master,text = u'蹴り',command = self.player1_kick)
        self.btn6.place(x = 180,y = 500)

        self.btn7 = tk.Button(self.master,text = u'フック',command = self.player1_fuck)
        self.btn7.place(x = 30,y = 550)

        self.btn8 = tk.Button(self.master,text = u'回転蹴り',command = self.player1_spinKick)
        self.btn8.place(x = 180,y = 550)




        #朝倉のHP
        self.label = tk.Label(text = 'HP')
        self.label.place(x=780,y =660)
        self.entry = tk.Entry(width=5)
        self.entry.place(x=800,y=660)
        self.entry.insert(tk.END,hp_asakura)

        #マクレガーのHP
        self.label = tk.Label(text = 'HP')
        self.label.place(x=70,y =660)        
        self.entry1 = tk.Entry(width=5)
        self.entry1.place(x=90,y=660)
        self.entry1.insert(tk.END,hp_makurega)

        #朝倉のMP
        self.label = tk.Label(text = 'MP')
        self.label.place(x=850,y =660)
        self.entry2 = tk.Entry(width=5)
        self.entry2.place(x=870,y=660)
        self.entry2.insert(tk.END,mp_asakura)

        #マクレガーのMP
        self.label = tk.Label(text = 'MP')
        self.label.place(x=140,y =660)        
        self.entry3 = tk.Entry(width=5)
        self.entry3.place(x=160,y=660)
        self.entry3.insert(tk.END,mp_makurega)

    '''ボタンを押されたあとの処理
    '''
    def player1_jab(self):    
        global hp_asakura
        global mp_makurega

        hp_asakura = hp_asakura - jab_makurega
        mp_makurega = mp_makurega + mp_jab
        if hp_asakura <= 0:
            self.win_window1()
        else:
            #txt1 = int(self.entry1.get())
            self.entry.delete(0,tk.END)
            self.entry.insert(0,hp_asakura)       
            self.entry3.delete(0,tk.END)
            self.entry3.insert(0,mp_makurega)  

    def player1_kick(self):            
        global hp_asakura
        global mp_makurega
        hp_asakura = hp_asakura - kick_makurega
        mp_makurega = mp_makurega + mp_jab
        if hp_asakura <= 0:
            self.win_window1()
        else:
            #txt1 = int(self.entry1.get())
            self.entry.delete(0,tk.END)
            self.entry.insert(0,hp_asakura)       
            self.entry3.delete(0,tk.END)
            self.entry3.insert(0,mp_makurega)   

    def player1_fuck(self):            
        global hp_asakura
        global mp_makurega
        #hp_asakura = hp_asakura - straight_makurega
        #mp_makurega = mp_makurega + mp_fuck      
        if mp_makurega < 30:
            self.mp_Fuck()         
        else :
            hp_asakura = hp_asakura - straight_makurega
            mp_makurega = mp_makurega + mp_fuck
            if hp_asakura<=0:
                self.win_window1()
            else :
                self.entry.delete(0,tk.END)
                self.entry.insert(0,hp_asakura)   
                self.entry3.delete(0,tk.END)
                self.entry3.insert(0,mp_makurega) 

    def player1_spinKick(self):            
        global hp_asakura
        global mp_makurega
        if mp_makurega < 100:
            self.mp_Hissatu()
        else :
            hp_asakura = hp_asakura - straight_makurega
            mp_makurega = mp_makurega + mp_hissatu
            if hp_asakura <= 0:
                self.win_window1()
            else :            
                hp_asakura = hp_asakura - spinKick_makurega
                self.entry.delete(0,tk.END)
                self.entry.insert(0,hp_asakura)  
                self.entry3.delete(0,tk.END)
                self.entry3.insert(0,mp_makurega) 

    def player2_jab(self):
        global hp_makurega
        global mp_asakura
        
        hp_makurega = hp_makurega - jab_asakura
        mp_asakura = mp_asakura + mp_jab

        if hp_makurega <= 0:
            self.win_window2()
        else :
            self.entry1.delete(0,tk.END)
            self.entry1.insert(0,hp_makurega)    
            self.entry2.delete(0,tk.END)
            self.entry2.insert(0,mp_asakura) 

    def player2_kick(self):            
        global hp_makurega
        global mp_asakura

        hp_makurega = hp_makurega - kick_asakura
        mp_asakura = mp_asakura + mp_kick

        if hp_makurega <= 0:
            self.win_window2()
        else :
            self.entry1.delete(0,tk.END)
            self.entry1.insert(0,hp_makurega)    
            self.entry2.delete(0,tk.END)
            self.entry2.insert(0,mp_asakura) 

    def player2_fuck(self):            
        global hp_makurega
        global mp_asakura

        if mp_asakura < 30:
            self.mp_Fuck()
        else :
            hp_makurega = hp_makurega - hiza_asakura
            mp_asakura = mp_asakura + mp_fuck

            if hp_makurega <= 0:
                self.win_window2()
            else :

                self.entry1.delete(0,tk.END)
                self.entry1.insert(0,hp_makurega) 
                self.entry2.delete(0,tk.END)
                self.entry2.insert(0,mp_asakura) 

    def player2_tobihiza(self):            
        global hp_makurega
        global mp_asakura

        if mp_asakura < 100:
            self.mp_Hissatu()
        else :
            hp_makurega = hp_makurega - tobihiza_asakura
            mp_asakura = mp_asakura + mp_hissatu

            if hp_makurega <= 0:
                self.win_window2()
            else :

                self.entry1.delete(0,tk.END)
                self.entry1.insert(0,hp_makurega)  
                self.entry2.delete(0,tk.END)
                self.entry2.insert(0,mp_asakura) 

    def mp_Fuck(self):
        dialog = tk.Toplevel()
        dialog.title("MP is not accumulated")
        dialog.geometry("300x300")
        tk.Label(dialog, text = u"フックはMPを30貯めよう").pack(padx=30, pady=30)  
    
    def mp_Hissatu(self):
        dialog = tk.Toplevel()
        dialog.title("MP is not accumulated")
        dialog.geometry("300x300")
        tk.Label(dialog, text = u"必殺技はMPを100貯めよう").pack(padx=30, pady=30)   

    def win_window1(self):
        dialog = tk.Toplevel()
        dialog.title("YOU WIN")
        dialog.geometry("300x300")
        tk.Label(dialog, text = u"YOU WIN").pack(padx=30, pady=30)
        self.entry.delete(0,tk.END)
        self.entry.insert(0,0)             


    def win_window2(self):
        dialog = tk.Toplevel()
        dialog.title("YOU WIN")
        dialog.geometry("300x300")
        tk.Label(dialog, text = u"YOU WIN").pack(padx=30, pady=30)
        self.entry1.delete(0,tk.END)
        self.entry1.insert(0,0)

def main():
    root = tk.Tk()
    root.resizable(width=False, height=False)    
    game = Game(master = root)
    game.mainloop()

if __name__ == "__main__":
    main()