from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from lectura import *
from creacion_automatas import *
from tkinter import messagebox
from automata import *

automata_kt = []
automata = []
key = []
charss = []
respuestas = []
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
        self.label.configure(text = "Se leyo el documento = "+self.filename)
        s = lectura(self.filename)
        pruebas(s)
        

        
    
def scanner(keywords, token , kt, chars):
    print("scanning")
    key.append(keywords)
    charss = chars
    
    if len(kt)!= 0:
        for i in range(len(kt)):
            infin_nuevo, tabla = automata_AFD(kt[i])
            automata_kt.append([tabla, infin_nuevo])
    
    if len(token)!= 0:
        for i in range(len(token)):
            infin_nuevo, tabla = automata_AFD(token[i])
            automata.append([tabla, infin_nuevo])
    
    root = Root()
    root.mainloop()


def lectura(ts):
    print("lectura")
    my_file = open(ts, "r")
    archivo = []
    for line in my_file:
        archivo.append(line)
    my_file.close()
    return archivo


def pruebas(listas):
    print(listas)
    ress = []
    for w in range(len(listas)):
      
        linea = listas[w].split(" ")
        ##linea =['do while \t do hola como estas do\n', 'do while']
        for i in range(len(linea)):
            yes = 0
            kea = 0

            if len(linea)-1 == i and linea[i][-1] == "\n":
                NL = 0
                keywordi = 0
                tokeni = 0

                re = linea[i].replace("\n", "")
                
                if re in key[0]:
                    print("Keywrod: "+re)
                    keywordi+=1
                else:
                    for q in range(len(automata_kt)):
                        respuesta = existe(re, automata_kt[q][0],automata_kt[q][1])
                        if respuesta == "YES":
                            tokeni +=1

                        respuestasd = existe("\n", automata_kt[q][0],automata_kt[q][1])
                        if respuestasd == "YES":
                            NL +=1

                for r in range(len(automata)):  
                    re = linea[i].replace("\n", "")
                       
                    respuesta = existe(re, automata[r][0],automata[r][1])
                    if respuesta == "YES":
                        tokeni +=1

                    respuestasd = existe("\n", automata[r][0],automata[r][1])
                    if respuestasd == "YES":
                        NL +=1

                if tokeni == 0 and keywordi == 0:
                    print("Error, esta palabra no pertenece: "+re)
                elif keywordi == 0 and tokeni >=1:
                    print("Token: "+re)

                if respuestasd == "NO":
                    print("No existe una nueva linea entonces \n entonces lo demas no pertenece.")
                elif respuestasd == "YES":
                        print("Token: New Line")
     
            else:
                if linea[i] in key[0]:
                    print("Keyword: "+linea[i])
                    kea+=1
                else:
                    
                    for s in range(len(automata_kt)):
                        respuesta = existe(linea[i], automata_kt[s][0],automata_kt[s][1])
                        if respuesta == "YES":
                            yes +=1
                
                for u in range(len(automata)):
                        respuesta = existe(linea[i], automata[u][0],automata[u][1])
                        if respuesta == "YES":
                            yes +=1

                if yes >=1:
                    print("Token: "+linea[i])
                elif kea >=1:
                    pass
                else:
                    print("Error, esta palabra no pertenece: "+linea[i])



            
        


 
 ##existe(cadena, lenguaje,infin)
 #automata_kt.append([tabla, infin_nuevo])
 #    if i !=0:
 #       return "YES"
 #   else:
 #       return "NO"
