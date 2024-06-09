import matplotlib.pyplot as plt  # le librerie da usare devono essere la prima cosa da definire
import numpy as np
import torch
# 1 ## I COMMENTI ## #
# il hastag serve per scrivere il commento come % per Matlab
""" Python non esegue, trattandoli come commenti tutte le stringhe
(anche su più righe) comprese tra le tre virgolette. Questo perchè vede una variabile char non assegnata a nulla
e la ignora allora """


# 2 ## DIALOGO CON UTENTE E MESSA A SCHERMO ## #
# messaggio = input("scrivi qua: ")  # input() funziona come lo stesso comando su Matlab
# print(messaggio)  # restituisce a schermo il contenuto delle () ! senza specificare "print" anche runnando la riga non
# viene restituita a schermo
# non esiste il ; a fine riga ma il tasto "Tab" fa molto di quel lavoro, va a creare un blocco di codice utile es per
# ciclo for


# 3 ## LE VARIABILI ## #
# I nomi per le variabili sono case sensitive, devi assolutamente evitare nomi con spazi, trattini - o che iniziano con
# i numeri
# per definire variabili assieme posso o metterle in colonna oppure separarle con una virgola
x_, y_, z_ = 1, 2, 3
print(x_)
print(y_)
print(z_)
# puoi assegnare lo stesso valore a più variabili in una riga:
a = b = c = "Banana"
print(a)
print(b)
print(c)  # a differenza di Matlab a,b,c restano variabili distinte ma con lo stesso valore, non si
# sovrascrivono a vienda
# I vettori di definiscono come con Matlab
vettore_riga = [9, 8, 7]  # la virgola ora è necessaria e non viene sostituita dallo spazio
print(vettore_riga)
# Se si vuole modificare il valore di un elemento specifico lo si richiama con [] e lo si sovrascrive:
vettore_riga[0] = 10  # similmente coi : posso sovrascrivere più elementi adiacenti in contemporanea
print(vettore_riga)
# Per inserire una nuova voce di elenco, senza sostituire nessuno dei valori esistenti, possiamo usare .insert()
# Il metodo inserisce un elemento in corrispondenza dell'indice specificato in insert(posizione, nuovo elemento)
vettore_riga.insert(1, 9)  # se lo si mette a fine elenco si può direttamente usare .append(nuovo elemento)
print(vettore_riga)
# .remove(elemento da togliere) invece elimina l'elemento dalla lista, con .pop(indice) cancello l'elemento in posizione
# "indice"
# Se si desidera specificare il tipo della variabile che creo posso usare
x = str(4)    # x sarà '4' , nota che la variabile stringa può essere definita indistintamente con la singola o doppia '
y = int(4)    # y sarà 4
z = float(4)  # z sarà 4.0
w = 1j        # w sarà un numero complesso
# È possibile ottenere il tipo di dati di una variabile con la funzione type()
print(type(x))
# È possibile eseguire la conversione da un tipo all'altro con i comandi :int(),float(),complex():
y_float = float(y)  # lo converto da int che era in un float, al posto di y posso mettere direttamente un numero
z_int = int(z)
y_complex = complex(y)
print(y_float, type(y_float))
print(z_int, type(z_int))
print(y_complex, type(y_complex))
# per visualizzare più varibili assieme si può usare un unico print separando gli elementi con una , o un +
print(x_, y_, z_)
print(x_ + y_ + z_)  # se le variabili sono numeriche il + ovviamente ne  calcolerà la somma
print(a + b + c)  # se le varibili sono char invece il + le mette in una unica stringa (per avere spazi tra loro serve
# interporci un + " " + , la , invece le separa con spazi, la , supporta anche tipi diversi di variabili nello stesso
# print, il + no
# Variabili create all'esterno di una funzione (come in tutti gli esempi sopra) sono note come variabili globali.
# Le variabili globali possono essere utilizzate da tutti, sia all'interno di funzioni e all'esterno
""" Se si crea una variabile con lo stesso nome all'interno di una funzione, questa variabile sarà locale e può essere
 utilizzato SOLO all'interno della funzione. La variabile globale con lo stesso nome RIMARRà com'era, 
 globale e con il valore originale  SENZA ESSERE SOVRASCRITTA DALLA LOCALE."""


# 4 ## LE STRINGHE ## #
# le stringhe in Python sono matrici di byte che rappresentano caratteri unicode.
# Le parentesi quadre possono essere utilizzate per accedere agli elementi della stringa (OVVERO ALLE SINGOLE LETTERE
# USATE, NON ALLE SINGOLE PAROLE).
a = "Hello, World!"
print(a[1])  # ricorda che per Python il primo carattere è in posizione 0
# similmente a matlab i : mi permettono di selezionare più elementi da start:end (end non incluso)
print(a[2:5])  # secondo elemento incluso e quinto escluso
print(a[:5])  # se non metto il primo elemento da prendere è sottointeso sia il primo
print(a[2:])  # similmente tralasciando l'indice finale prende fino all'ultimo elemento
# si può anche fare una indicizzazione negativa per andare a contare gli elementi dall'ultimo anzichè dal primo
# Poiché infatti le stringhe sono matrici, possiamo scorrere i caratteri in una stringa, con un ciclo for
for x in "Banana":  # i : finali servono per dire "allora cosa fai..."
    print(x)
# La funzione len() restituisce la lunghezza di una stringa:
print(len(a))
# Per verificare se in una frase è presente una certa stringa possiamo usare il comando in (è simile a find di matlab):
# (esiste analogo find anche qua)
txt = "Mi sto rompendo le scatole con Python"
print("Python" in txt)  # se la trova esce un True, false altrimenti
# in può allora essere usato nei cicli if
if "Python" in txt:
    print("'Python' trovato")
# il comando duale è "not in" che da True se non trova la parola nella frase specificata
print(7 in vettore_riga)  # in funziona anche per trovare numeri in un vettore o insieme
# posso usare .replace per sostituire una stringa o numero all'interno della stringa specificata prima del .
print(a.replace("H", "J"))
# possiamo combinare stringhe e numeri usando il comando format()
# Il metodo formatta gli argomenti passati e li inserisce nella stringa in cui si trovano i segnaposto {} :
age = 25
txt = "Sono Paolo ed ho {} anni"
print(txt.format(age))
# Il metodo format() accetta un numero illimitato di argomenti e viene inserito in i rispettivi segnaposto:
quantity = 3
numero_oggetto = 567
prezzo = 49.95
myorder = "Io voglio {} pezzi dell' oggetto #{} per {} euro."  # posso anche usare dentro le graffe degli indici per
# essere sicuro di metterci dentro gli elementi corretti
print(myorder.format(quantity, numero_oggetto, prezzo))


# 5 ## FUNZIONI ## #
# Una funzione si va a definire con il comando def come segue: (LASCIA 2 RIGHE BIANCHE PRIMA DI DEFINIRLA)
def funzione():  # in () si mettono tutti gli argomenti da dare (come Matlab), se il suo numero è sconosciuto si usa *
    # prima del nome del parametro
    print("Hai richiamato la funzione")
# non serve il end in python ma basta cancellare gli spazi per chiudere il blocco di codice, DEVI LASCIARE DUE RIGHE
# BIANCHE DOPO AVER DEFINITO UNA FUNZIONE PRIMA DI SCRIVERE ALTRO


funzione()  # così la si va a richiamare e usare


# Per creare una variabile globale all'interno di una funzione, è possibile utilizzare la parola chiave global
def funzione1():
    global v_gl
    v_gl = "variabile globale dentro una funzione"  # se v_gl esistesse già e la imponessi ora come global allora
    # sovrascriverebbe il suo vecchio valore


funzione1()
print(v_gl)


# 6 ## OPERATORI CONFRONTO E LOGICI ## #
# Gli operatori di confronto vengono utilizzati per confrontare due valori:
# Operator	Name	                    Example
# ==	    Equal	                    x == y
# !=	    Not equal	                x != y
# >	        Greater than	            x > y
# <	        Less than	                x < y
# >=	    Greater than or equal to	x >= y
# <=	    Less than or equal to	    x <= y

# Gli operatori logici vengono utilizzati per combinare istruzioni condizionali:
# Operator	Description                                              Example
# and 	    Returns True if both statements are true	             x < 5 and  x < 10
# or	    Returns True if one of the statements is true	         x < 5 or x < 4
# not	    Reverse the result, returns False if the result is true	 not(x < 5 and x < 10)

# Gli operatori d'identità vengono utilizzati per confrontare gli oggetti, non se sono uguali,
# ma se sono effettivamente lo stesso oggetto, con la stessa posizione di memoria:
# Operator	Description	                                             Example
# is 	    Returns True if both variables are the same object	     x is y
# is not	Returns True if both variables are not the same object 	 x is not y

# Gli operatori di appartenenza vengono utilizzati per verificare se una sequenza è presentata in un oggetto:
# Operator	Description	                                                                        Example
# in 	    Returns True if a sequence with the specified value is present in the object	    x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y


# 7 ## CICLO FOR ## #
# È possibile scorrere le voci dell'elenco utilizzando un ciclo for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)  # stampa tutti gli elementi dell'elenco uno a uno
# È inoltre possibile scorrere le voci dell'elenco facendo riferimento al relativo numero d' indice.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])  # Stampa tutti gli elementi facendo riferimento al relativo numero indice
# classica intestazione for per matlab è for i=inizio:step:fine, si può fare la stessa cosa come
# for x in range(inizio, fine, incremento), se non specificato l'incremento è 1  ! come al solito python è stronzo e
# il valore fine non viene usato ma il ciclo si ferma quando x lo raggiunge
for x in range(3, 30, 3):
    print(x)  # notare infatti che 30 non è stampato


# 8 ## CICLO WHILE ## #
# È possibile scorrere le voci dell'elenco utilizzando un ciclo while,
# Utilizzo la funzione len() per determinare la lunghezza dell'elenco,
# quindi inizia da 0 e scorri le voci dell'elenco facendo riferimento ai loro indici.
# Ricorda di aumentare l'indice di 1 dopo ogni iterazione.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
# Con l'istruzione break possiamo interrompere il ciclo anche se nel while la condizione è vera:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break   # esci dal ciclo while quando i=3
    i = i + 1
# Si può usare l'istruzione continue per fermare l'iterazione e proseguire con i successivi comandi (sempre stando in
# ciclo while):
i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)  # stampa i solo da 3 in poi fino a 6
# break e continue valgono anche per i cicli for


# 9 ## CICLO IF ## #
# Ricorda che Python si basa sull'indentazione (spazio vuoto all'inizio di una riga) per definire l'ambito nel codice
# come per Matlab esiste la versione if...else, in Python else è sostituito da elif, in realtà non è proprio lo stesso:
#   else= se condizione di if è falsa allora esegui quello che segue (anche else esiste in Python con tale senso)
#   elif= se condizione di if è falsa allora prova questa condizione (è come se fosse un altro if alternativo al primo)
# Se si dispone di una sola istruzione da eseguire, è possibile inserirla nella stessa riga dell'istruzione if:
if a > b: print("a è maggiore di b")
print("A") if a > b else print("B")  # segue molto il modo di parlare inglese


# 10 ## MODULI PYTHON ## #
# Un modulo non è alto che un altro file di codice che si vuole far eseguire all'interno dello script attuale
# è quindi un file salvato come "Nome.py"
# Possiamo richiamare il modulo creato con "import Nome"
# Se si vuole usare una funzione definita in un altro script si usa la sintassi: module_name.nome_funzione (dopo avere
# importato il suddetto modulo). Similmente si può accedere a dizionari dell'altro script.
# È possibile creare un alias quando si importa un modulo, utilizzando la parola chiave as:
# "import NuovoScript as new"
# È possibile scegliere d' importare solo parti da un modulo, utilizzando la parola chiave from
# "from mymodule import person1"
# molto utile è numpy che contiene molte funzioni matematiche (permette di usare i comandi soliti di matlab anche qua)
# import numpy as np
print(np.pi)
print(np.e)
print(np.array([1, 2, 3]))  # vettore classico di Matlab =\ da list di python
print(np.array([(1, 2, 3), (4, 5, 6)]))  # matrice
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(np.multiply(x, y))  # moltiplicazione elemento per elemento
print(np.dot(x, y))  # classica moltiplicazione matriciale
# altro modulo molto utile è matplotlib.pyplot permette di creare plot analogamente a matlab
# import matplotlib.pyplot as plt (va messo come prima cosa dello script)
x = np.linspace(0, 10)  # stesso comando linspace di Matlab
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, 'b', x, z, 'r')  # doppio plot sovrapposto
plt.xlabel('Radianti')  # nome di asse orizzontale
plt.ylabel('Valore')  # nome di asse verticale
plt.title('Grafico di prova')  # titolo del plot
plt.legend(['Sin', 'Cos'])  # inserisco la legenda
plt.grid()  # attivo la griglia
plt.show()  # senza questa riga non ti fa vedere una pippa, va messa in fondo della costruzione del grafico
plt.plot(y,z)  # altro es
plt.axis('equal')
plt.show()  # notare che non lo sovrascrive al precedente ma ne crea uno nuovo
# es. di subplot
plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title('Sen(x)')
plt.subplot(2, 1, 2)
plt.plot(x, z)
plt.title('Cos(x)')
plt.show()


# 11 ## CLASSI PYTHON ## #
# Definiamo una classe Python 'Car' con variabili 'modello','colore','velocity' e funzioni 'accelerare','rallentare',
# 'stato'. Creo poi un oggetto 'macchina1' dalla classe Car e ci usiamo su le funzioni create in Car.

class Car:
    # Inizializzazione delle variabili
    def __init__(self, modello, colore):
        self.modello = modello
        self.colore = colore
        self.velocity = 0

    def accelerare(self, incremento):
        self.velocity += incremento

    def rallentare(self, decremento):
        if self.velocity - decremento >= 0:
            self.velocity -= decremento
        else:
            print("La macchina è già ferma!")

    def stato(self):
        print(f"Modello: {self.modello}")
        print(f"Colore: {self.colore}")
        print(f"Velocità: {self.velocity} km/h")


# Creiamo un oggetto macchina1 della classe Car (devo specificarne le variabili date nell' __init__)
macchina1 = Car("SUV", "Blu")
# Usiamo la funzione accelerare per aumentare la velocità
macchina1.accelerare(50)
# Chiamiamo la funzione stato per vedere le info sulla macchina
macchina1.stato()
# Usiamo la funzione rallentare per ridurre la velocità
macchina1.rallentare(20)
# Vediamo di nuovo lo stato
macchina1.stato()


# 12 ## TORCH ## #
# Come si crea una matrice con torch
vx = torch.tensor([[1, 0, 3],
                   [0, 0, 0],
                   [-1, 0, -3]])
print(vx)
# Creazione di una maschera booleana che controlla se gli elementi del tensore vx sono non nulli
vx_non_nulla_mask = vx != 0
print(vx_non_nulla_mask)
vx_non_nulla_mask_un = vx_non_nulla_mask.unsqueeze(1)
print(vx_non_nulla_mask_un)
# Applicazione della maschera tramite torch.where
rew = torch.where(vx_non_nulla_mask, torch.ones_like(vx), torch.zeros_like(vx))
print('rew', rew)

# Crea un tensore di elementi tutti uguali di dim 2x4x3
pos_in = torch.ones(2,4,3) * 0.25
print(pos_in)
pos_fin = torch.ones(2,4,3)
spostamento = pos_fin - pos_in
print(spostamento)
# Calcolo della norma del vettore distanza per ogni robot e per ogni gamba
norme_spostamento = torch.norm(spostamento, dim=2, keepdim=True)
# Stampa del risultato
print(norme_spostamento)

# 13 DIZIONARI ------------------------------------------------------------------------------------------------------- #
# creazione di un dizionario = insieme non ordinato di coppie chiave:valore
failure_dataset = { 'dof_pos': {
                       'test1': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                    },
                    'dof_vel': {
                       'test1': torch.ones(8),
                       'test2': torch.zeros(8)
                    },
                    'base_quat': {

                    },
                    'base_pos': {

                    },
                    'base_velocities': {

                    }
}
# estrazione dei valori delle grandezze definite dentro una lista
lista_dof_pos = list(failure_dataset['dof_pos'].values())    # per accedere a un elemento della lista usare le []
lista_dof_vel = list(failure_dataset['dof_vel'].values())
lista_base_quat = list(failure_dataset['base_quat'].values())
lista_base_pos = list(failure_dataset['base_pos'].values())
lista_base_velocities = list(failure_dataset['base_velocities'].values())

print("failure_dataset  = ", failure_dataset)  # così mostra tutto il dizionario
print("La key dof_pos è ", failure_dataset['dof_pos'])
print("---------------------------------------------")
print("I dof_pos aggiunti sono ", lista_dof_pos)  # così accedo a tutti gli elementi di 'dof_pos' inseriti in una lista
print("I dof_vel aggiunti sono ", lista_dof_vel)
print("I base_quat aggiunti sono ", lista_base_quat)

# -------------------------------------------------------------------------------------------------------------------- #