from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from lectura import *
from creacion_automatas import *
from tkinter import messagebox

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Browse file")
        self.minsize(640,400)
        #self.configure(background = '#4D4D4D')
        
        self.labelFrame = ttk.LabelFrame(self,text = "Open a File")
        self.label= ttk.Label(self.labelFrame, text = "\n\n\n\n\n")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        self.button()

    def button(self):
        self.label= ttk.Label(self.labelFrame, text = "\n\n\n\n\n")
        self.button = ttk.Button(self.labelFrame, text = "Browse a File", command = self.fileDialog)
        self.button.grid(column = 10, row = 30)
        
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "\Desktop", title= "Select a File", filetype = (("Texto", "*.txt"),("All Files", "*.*"),("jpg", "*.jpg")))
        self.label= ttk.Label(self.labelFrame, text = "\n\n\n\n\n")
        self.label.grid(column = 1, row =2)
        texto = open(self.filename, "r")
        
        antes, character, keywords, tokens, producciones = read(self.filename)
        self.label.configure(text = "Se leyo el documento = "+self.filename)
#        print(antes)
#        print(character)
#        print(keywords)
#        print(tokens)
#        print(producciones)
        self.button2()
        
    def button2(self):
        self.label= ttk.Label(self.labelFrame, text = "\n\n\n\n\n")
        self.button = ttk.Button(self.labelFrame, text = "Continue", command = self.create)
        self.button.grid(column = 20, row = 30)
    
    def create(self):
        antes, character, keywords, tokens, producciones = read(self.filename)
        print("continuamos")   
        crear(antes, character, keywords, tokens, producciones)
        messagebox.showwarning('Proceso creado','Se creo el proceso correctamente')
        
if __name__ == '__main__':
    root = Root()
    root.mainloop()