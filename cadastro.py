import tkinter as tk
from tkinter import ttk

class CadastroTk:
    def __init__(self):
        self.janela = tk.Tk()
        self.f1 = tk.Frame (self.janela)
        self.f2 = tk.Frame (self.janela, pady = 10)
        
        
        self.titulo = tk.Label(self.f1, font = 'Arial', text = 'Cadastro')
        self.titulo.grid (row = 1, column = 1)


        self.lnome = tk.Label(self.f2, text = 'Nome: ')
        self.lnome.grid(row = 1, column = 1)
        
        
        self.txtNome = tk.Entry(self.f2,)
        self.txtNome.insert (0, 'Digite seu Nome')
        self.txtNome.bind ('<Button-1>',self.apagar)
        self.txtNome.grid (row =1, column = 2)

        self.lnome = tk.Label(self.f2, text = 'CPF: ')
        self.lnome.grid(row = 2, column = 1)
        
        self.txtCPF = tk.Entry(self.f2)
        self.txtCPF.insert (0, 'Digite seu CPF')
        self.txtCPF.bind ('<Button-1>',self.apagarCPF)
        self.txtCPF.grid (row =2, column = 2, pady = 10)
        

        self.lEMAILL = tk.Label(self.f2, text = 'E-mail: ')
        self.lEMAILL.grid(row = 3, column = 1)
        
        self.txtEMAIL = tk.Entry(self.f2)
        self.txtEMAIL.insert (0, 'Digite seu E-mail')
        self.txtEMAIL.bind ('<Button-1>',self.apagarEMAIL)
        self.txtEMAIL.grid (row =3, column = 2)

        
        self.txtEMAILC = tk.Entry(self.f2)
        self.txtEMAILC.insert (0, 'Confirme seu E-mail')
        self.txtEMAILC.bind ('<Button-1>',self.apagarEMAILC)
        self.txtEMAILC.grid (row =4, column = 2, pady = 10)

        self.btn = tk.Button (self.f2, text = 'Salvar', command = self.Cadastrar)
        self.btn.grid (row = 5, column = 2, sticky = 'e')

        
        self.f1.pack ()
        self.f2.pack ()
               
                     
        self.janela.mainloop()
    def Cadastrar (self):
        pass
        print (self.txtNome.get())
        print (self.txtCPF.get())
        print (self.txtEMAIL.get())

    def apagar (self, Entry):
        self.txtNome.delete(0,tk.END)
    def apagarCPF (self, Entry):
        self.txtCPF.delete(0,tk.END)
    def apagarEMAIL (self, Entry):
        self.txtEMAIL.delete(0,tk.END)
    def apagarEMAILC (self, Entry):
        self.txtEMAILC.delete(0,tk.END)
   

CadastroTk()
