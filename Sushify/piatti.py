from functools import reduce




"""I piatti sono modellati mediante i 4 dei cinque sapori principali e il piccante; e da una categoria che ne identifica la
tipologia(nel caso di sushi si parla di nigiri, gunkan... il tipo del pitto).
I sapori serviranno a misurare la distanza tra un piatto e l'altro, mentre la categoria verrà usata per dividere i piatti
in insiemi diversi, così da offrire una scelta maggiore all'utente, non solamente basata sul sapore percepito, ma anche tipo di
cibo che si consuma."""
class Piatto:

    def __init__(self, *args, **kwargs):
        #Parametri descrittori, che servono principalmente alla presentazione del piatto
        self.numero = kwargs['numero']
        self.nome = kwargs['nome']
        self.ingredienti = kwargs['ingredienti']

        #parametri usati per la valutazione dei prodotti
        self.tipo = kwargs['tipo']
        #i sapori li metto in un dizionario per comodità di elaborazione
        self.sapori = { }
        self.sapori['dolce'] = kwargs['dolce']
        self.sapori['amaro'] = kwargs['amaro']
        self.sapori['aspro'] = kwargs['aspro']
        self.sapori['salato'] = kwargs['salato']
        #tecnicamente non è un gusto
        self.sapori['piccante'] = kwargs['piccante']
        #self.umami, non messo perchè non lo conosco

    '''metodo che trasforma i valori dei vari sapori in una lista'''
    def sapori_in_lista(self):
        s = list(self.sapori.values())
        return s

    """Se invogo il la funzone str()sull'oggetto, esso restituisce la concatenazione di numero, nome,tipo,ingredientie array dei 
    valori dei guisti"""
    def __str__(self):
        return ""+str(self.numero)+", "+self.nome+", "+self.tipo+", "+self.ingredienti+" "+str(self.sapori_in_lista())

"""Funzione per creare un menu: un dizionatrio contenente diverse liste di piatti.
E' necessario passare il nome del file che si vuole utilizzare come menu."""
def crea_menu(nome_file=None):
    menu = {}
    if nome_file == None:
        print("Nessun file passato")
        return menu
   
    with open(nome_file,"r") as file:
        #leggo il numero di piatti presenti nel menu
        line = file.readline()
        numero_piatti = int(line)

        for i in range(0,numero_piatti):
            argomenti = {}
            #leggo una linea e la divido in chiave valore
            for j in range(0,9):
                line = file.readline()
                s = line.strip().split("=")
                #se è un valore numerico lo salvo come float, altrimenti come stringa
                try:
                    valore = float(s[1])
                    if valore < 0:
                        valore = 0
                    argomenti[s[0]] = valore
                except:
                    argomenti[s[0]] = s[1]

            #il numero del piatto lo voglio intero
            argomenti["numero"] = int(argomenti["numero"])
            #creo l'oggetto piatto
            p = Piatto((),**argomenti)
            #inserisco il nuovo elemento nella lista del suo tipo se esiste, altrimenti ne creo una nuova se è un nuovo tipo di piatto
            try:
                menu[p.tipo].append(p)
            except:
                menu[p.tipo]=[]
                menu[p.tipo].append(p)

    return menu

"""Funzione per trovare un piatto, dato il suo numero.
Questa versione assume che le liste del menu siano ordinate"""
def trova_piatto(numero_piatto,menu):
    for k in menu:
        lista = menu[k]
        #non ha senso cerca nelle liste di piati il cui estremi non contengono il numero del piatto cercato
        #questo vale solo per liste di piatti ordinate
        if numero_piatto >= lista[0].numero and numero_piatto <= lista[len(lista)-1].numero:
            for elemento in lista:
                if elemento.numero == numero_piatto:
                    return elemento
    #se arrivo qui, non ho trovato il piatto dal numero cercato
    return None

"""Funzione per trovare un piatto, dato il suo numero, in un menu dove non persiste alcuna relazione di ordinamento"""
def simple_trova_piatto(numero_piatto,menu):
    for k in menu:
        lista = menu[k]
        #un ricerca lenta, ma che assicura di valutare ogni singolo elemento
        for elemento in lista:
            if elemento.numero == numero_piatto:
                return elemento
    #se arrivo qui, non ho trovato il piatto dal numero cercato
    return None

"""Funzione che restituisce una versione del menu ordinata.
Non salva lo score di ogni piatto, quindi se si vuole verificarlo
è necessario richiamare la funzione_distaza in un secondo momento"""
def menu_suggerimento(menu, piatto_piaciuto = None, funzione_distanza = None):
    menu_ordinato = {}
    #se è stato passato un dizionario vuoto o non ho passato una funzione, allore non eseguo la ricerca
    if piatto_piaciuto == None or funzione_distanza==None:
        return menu_ordinato
    try:
        for k in menu:
            lista = menu[k]
            menu_ordinato[k] = sorted(lista, key = lambda piatto: funzione_distanza(piatto.sapori_in_lista(), piatto_piaciuto.sapori_in_lista()))
    except:
        print("Errore durante l'ordinamento del menu, verificare che la funzione passata o i parametri siano corretti")
    #restituisco il menu ordinato
    return menu_ordinato

"""Funzione per valutare portate composte da più piatti del menu, come barche e/o piatti mix che coinvolgono solo più
campioni di altri piatti.
Si calcola la distanza dei singoli piatti e la si combina per ottenere il risultato finale """
def distanza_piatto_composto(piatto_piaciuto, funzione_distanza, lista_piatti):
    #creo una lista dei punteggi
    lista_punteggi = map(lambda x: funzione_distanza(piatto_piaciuto.sapori_in_lista(), x.sapori_in_lista()), lista_piatti)
    lista_punteggi = list(lista_punteggi)

    #faccio la media sommando i punteggi
    punteggio_medio = sum(lista_punteggi)
    return punteggio_medio/len(lista_piatti)