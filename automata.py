from funciones import * 
from operator import itemgetter
import os
##environment de mi graficadora
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

def thomson_grafic(ingreso, numero = 2):
        #variables iniciales

    i = 0
    trans = []
    infin = []
    cant = 0
    concat = []
    respuesta = []

    while i < len(ingreso):
        
        ## si se ingresa un or entonces crea la grafica 
        if ingreso[i] == "|":
     
            s = concat[-1]
            concat.pop()
            o = concat[-1]
            concat.pop()
            concat.append([s,o, [numero,"e", infin[-2][0]],[numero,"e",infin[-1][0]],[infin[-2][1],"e",numero+1],[infin[-1][1],"e",numero+1]])
            inicial = numero
            final = numero +1
            numero +=2
            infin.pop()
            infin.pop()
            infin.append([inicial,final])
            
            
        ## se realiza kle
        elif ingreso[i] == "*":
        
            inicial = infin[-1][0]
            final = infin[-1][1]
            x = [numero, "e", inicial]
            y = [final, "e", inicial]
            inicial = numero
            numero +=1
            z = [final, "e", numero]
            k = [inicial, "e", numero]
            final = numero
            v = concat[-1]
            concat.pop()
            concat.append([v,x,y,z,k])
            infin.pop()
            infin.append([inicial, final])
            numero += 1
        
        ##concatenacion
        elif ingreso[i] == " ":
            primera = concat[-1]
            concat.pop()
            segunda = concat[-1]
            concat.pop()
            orden_ultima = infin[-1]
            infin.pop()
            orden_penultima = infin[-1]
            infin.pop()
            try:
                 segunda = flat(segunda, [])
                 for a in range(len(segunda)):
                     for n in range(0,3):
                         if segunda[a][n] == orden_penultima[1]:
                             segunda[a][n] = orden_ultima[0]
                            
            except:
                for a in range(len(segunda)):
                    if segunda[a] == orden_penultima[1]:
                        segunda[a] = orden_ultima[0]
            

            infin.append([orden_penultima[0], orden_ultima[1]])
            concat.append([segunda, primera])
        
        ##variable nomral
        elif ingreso[i] != " " and ingreso[i] != "|" and ingreso[i] != "*" :
            concat.append([numero, ingreso[i], numero+1])
            infin.append([numero, numero +1])
            numero +=2
        
        i+=1

    resultado = sorted(flat(concat,[]), key= itemgetter(0))
    return resultado, infin


##imprime el automata
#resultado = las transiciones del automata
#infin = estado inicial y final
def impresion(resultado, infin):
    estados = []
    simbolos = []
    for i in range(len(resultado)):
        if resultado[i][0] not in estados:
            estados.append(resultado[i][0])
                
        if resultado[i][2] not in estados:
            estados.append(resultado[i][2])
                
        if resultado[i][1] not in simbolos:
            simbolos.append(resultado[i][1])
                
    print("--------------------------------------------------------------------------------------")
    print("Q -> Estados")
    print(estados)
    print("--------------------------------------------------------------------------------------")
    print("E -> simbolos")
    print(simbolos)
    print("--------------------------------------------------------------------------------------")
    print("q0 -> Estado inicial: ")
    for i in range(len(infin)):
        print(infin[i][0])
    print("--------------------------------------------------------------------------------------")
    print("F -> Estado de Aceptacion: ")
    for i in range(len(infin)):
        print(infin[i][1])
    print("--------------------------------------------------------------------------------------")
    print("Transiciones:")
    print(resultado)
    print("--------------------------------------------------------------------------------------")
        
    

        
        

   
##eclosure del primer numero 
def eclosure_alone(nodo, lenguaje):
    nodos =[]
    nodos.append(nodo)
    move = posibles_movimientos(nodo, "e", lenguaje)
    for x in move:
        if x[2] not in nodos:
            nodos.append(x[2])
    s = set()
    if isinstance(nodos,list):
        for item in nodos:
            s.add(item)
        return s
    else:
        s.add(nodos)
            
    
#eclusure 
def eclosure(x, lenguaje):
    if isinstance(x, int):
        nodos = []
        nodos.append(x)
    else: 
        nodos = list(x)
    if isinstance(nodos, list):
        for n in nodos:
            move = posibles_movimientos(n, "e", lenguaje)
            for x in move:
                if x[2] not in nodos:
                    nodos.append(x[2])
    s = set()
    for item in nodos:
        s.add(item)
    return s

#nos dice a donde se mueve en los estados que se le proporciona
# nodos = nodos en el que se encuentra ahorita
# cadena = que letra vamos a mover
# lenguaje = nuestras transiciones
def move(nodos, cadena, lenguaje):
    nodos = list(nodos)
    movimiento = []
    if isinstance(nodos, list):
        for n in range(len(nodos)):
            move = posibles_movimientos(nodos[n], cadena, lenguaje)
            for x in move:
                if x[2] not in movimiento:
                    movimiento.append(x[2])
        s = set()
        for item in movimiento:
            s.add(item)
        return s
    
    else:
        move = posibles_movimientos(nodos, cadena, lenguaje)
        for x in move:
            if x[2] not in movimiento:
                movimiento.append(x[2])
                
                
        s = set()
        for item in movimiento:
            s.add(item)
        return s

#nos indica los posibles movimientos que podemos tomar
#nodo = de que nodo queremos ver los movimientos
#cadena = que simbolo queremos buscar los posibles movimientos
#atomata = las transiciones de nuestro automata
def posibles_movimientos(nodo,cadena, automata):
    movimientos = []
    for n in automata:
        if n[0] == nodo and n[1] == str(cadena):
            movimientos.append(n) 
    return movimientos

#nos indica si la cadena existe en nuestro lenguaje
#cadena = la cadena que queremos saber si existe en nuestro lenguaje
#lenguaje = las transiciones de nuestro lenguaje
#infin = el estado final y el inicial
def existe(cadena, lenguaje,infin):
    i = 0
    inicial = infin[0][0]
    
    for n in cadena:

        x = movin(inicial, n, lenguaje)
        if len(x)==0:
            return "NO"
        x = list(x)
        inicial = x[0]
    i = 0 
    for n in range(len(infin)):
        if inicial == infin[n][1]:
            i += 1
    if i !=0:
        return "YES"
    else:
        return "NO"

def movin(nodos, cadena, lenguaje):
    if isinstance(nodos, list):
        nodos = list(nodos)
    else:
        nodos = [nodos]
    
    movimiento = []
    if isinstance(nodos, list):
        for n in range(len(nodos)):
            
            move = posibles_movimientos(nodos[n], cadena, lenguaje)
            
            for x in move:
                if x[2] not in movimiento:
                    movimiento.append(x[2])
        s = set()
        for item in movimiento:
            s.add(item)
        return s
    
    else:
        move = posibles_movimientos(nodos, cadena, lenguaje)
        for x in move:
            if x[2] not in movimiento:
                movimiento.append(x[2])
                
                
        s = set()
        for item in movimiento:
            s.add(item)
        return s
     

##Funciones necesarias: eclosure(nodos, lenguaje), move(nodos, cadena, lenguaje)
##Utiliza: todos los estados, todos los simbolos, las transiciones, estado final e inicial 
def dfa_nfa(transiciones, infin):
    
    ## nos retorna los simbolos que existen en nuestras transiciones
    simbolos = []
    for i in range(len(transiciones)):
        if transiciones[i][1] != "e":
            if transiciones[i][1] not in simbolos:
                simbolos.append(transiciones[i][1])
                
        
    #transiciones
    i = 0
    Dstate =[]
    tablita = []
    Dstate.append(eclosure(infin[0][0], transiciones))
    infin_nuevo =[]
    infin_nuevo.append(eclosure(infin[0][0], transiciones))
    
    
    ##algoritmo utilizado en clase
    while i < len(Dstate):
        for n in simbolos:
            u = eclosure(move(Dstate[i],n,transiciones),transiciones)
            tablita.append([Dstate[i],n,u])
            for w in infin:
                if w[1] in u:
                    infin_nuevo.append(u)
            if u not in Dstate and u is not None:
                Dstate.append(u)         
        i+=1
    
 
    ##Editamos lo que nos devuelve ya que tenemos vacios
    x = 0
    while x < len(tablita):
        if tablita[x][0] == set() or tablita[x][2] == set():
            tablita.pop(x)
            x-=1
            
        x +=1
    
    ##cambiando los estados a letras
    
    yes = ["A","B","C","D","E","F","G","H","I","J","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK", "LL", "MM", "NN", "OO", "PP", "QQ", "RR", "SS",
            "TT", "QQ", "RR", "SS", "TT", "UU", "VV", "WW", "XX", "YY", "ZZ"]

    numerosss = [1,2,3,4,5,6,7,8,9]
    alfabeto = []
    for soo in range(len(numerosss)):
        for ioo in range(len(yes)):
            
            ooo = str(yes[ioo]) + str(numerosss[soo])
            alfabeto.append(ooo)

    
    x = 0 
    while x < len(tablita):
        indice1 = Dstate.index(tablita[x][0])
        tablita[x][0] = alfabeto[indice1]
        indice1 = Dstate.index(tablita[x][2])
        tablita[x][2] = alfabeto[indice1]
        x +=1
    x = 0
    

    #cambiamos el estado final y el inicial 
    while x < len(infin_nuevo):
        indice1 = Dstate.index(infin_nuevo[x])
        infin_nuevo[x]= alfabeto[indice1]
        x+=1
    y = []
    
    for i in range(1,len(infin_nuevo)):
        y.append([infin_nuevo[0],infin_nuevo[i]])
    return tablita, y
        
      
def prueba(entraa):
    entraa = str_to_list(entraa)
    pare = False
    nueva = []
    for i in entraa:
        if i == "(":
            pare = True
        if i == ")":
            pare = False
            
        if pare == True:
            nueva.append(i)
            
        if pare == False:
            nueva.append(i)
            nueva.append("|")
            
def character(entraa):
    entraa = str_to_list(entraa)
    pare = False
    nueva = []
    for i in entraa:
        if i == "(":
            pare = True
    if pare == False:
        entraa = str_to_list(entraa)
        entraa = intersperse(entraa, '|')
        entraa =  str_to_list(entraa)
        entraa.append(")")
        entraa.insert(0,"(")
        return listToStr(entraa)

    hola = False
    if pare == True:
        nueva = []
        for i in entraa:
            if i == "(":
                hola = True
            if i == ")":
                hola = False
                
            if hola == True:
                if i == "(" or i == ")":
                    pass
                else:
                    nueva.append(i)
            if hola == False:
                if i == ")":
                    pass
                else:
                    nueva.append(i)
                
                nueva.append("|")
           
        if nueva[len(nueva)-1] == "|":
            nueva.pop()
        if nueva[len(nueva)-1] == " ":
            nueva.pop()
            nueva.pop()
          
        print(nueva)
        nueva.append(")")
        nueva.insert(0,"(")
        return listToStr(nueva)
            
        
    
        
def compro(entraa, comprobar):
    entraa = str_to_list(entraa)
    entraa = intersperse(entraa, '|')
    entraa =  str_to_list(entraa)
    entraa.append(")*")
    entraa.insert(0,"(")
    ingreso = infix_to_postfix(expandir(entraa))
    i = 0
    while i < len(ingreso):
        if ingreso[i] == "(":
            ingreso.pop(i)
            i-=1
        i+=1
    resultado, infin = thomson_grafic(ingreso)
    tabla, infin_nuevo = dfa_nfa(resultado, infin)
    ##TABLA = NUESTRAS TRANSICIONES DEL AUTOMATA
    ##INFIN_NUEVO = NUESTRO ESTADO FINAL E INICIAL
    print(existe(comprobar, tabla, infin_nuevo))
    return existe(comprobar, tabla, infin_nuevo)
    
##junta los nfa (cuando son mas de 1)
#resultado = las transiciones del automata
#infin = estado inicial y final
def juntar_nfa(resultados, infins):
    infins =  sorted(infins, key= itemgetter(1))
    alto = len(infins)-1
    numero = infins[alto][1] + 1
    respuesta = flat(resultados, [])
    final = []
    for i in range(0,len(infins)):
        respuesta.append([numero,"e",infins[i][0]])
        final.append([numero, infins[i][1]])
    return respuesta, final

def automata_AFD(kt):
    ingreso = infix_to_postfix(kt)
    resultado, infin = thomson_grafic(ingreso)
    tabla, infin_nuevo = dfa_nfa(resultado, infin)
    return infin_nuevo, tabla
    
#
#def character(entraa):
#    entraa = str_to_list(entraa)
#    entraa = intersperse(entraa, '|')
#    entraa =  str_to_list(entraa)
#    entraa.append(")*")
#    entraa.insert(0,"(")
#    ingreso = infix_to_postfix(expandir(entraa))
#    i = 0
#    while i < len(ingreso):
#        if ingreso[i] == "(":
#            ingreso.pop(i)
#            i-=1
#        i+=1
#    resultado, infin = thomson_grafic(ingreso)
#    tabla, infin_nuevo = dfa_nfa(resultado, infin)
#    return tabla, infin_nuevo

    
