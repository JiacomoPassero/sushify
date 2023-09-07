from sushify.calcolo_distanza import cosine_similarity_mod
from sushify.piatti import crea_menu, trova_piatto, menu_suggerimento, distanza_piatto_composto

menu = crea_menu("menu_default")

for k in menu:
    s = menu[k]
    print(k)
    for elementi in s:
        print("    ",str(elementi))



n_piatto = input("Inserisci il numero del piatto che ti è piaciuto: ")
n_piatto = int(n_piatto)
piatto_piaciuto = trova_piatto(n_piatto,menu)


if piatto_piaciuto != None:

    fuzione_distanza = cosine_similarity_mod
    menu_ordinato = menu_suggerimento(menu,piatto_piaciuto,fuzione_distanza)

    for k in menu_ordinato:
        lista = menu_ordinato[k]
        print(k)
        for elemento in lista:
            if elemento is not piatto_piaciuto:
                print("    ",str(elemento),"   ",fuzione_distanza(elemento.sapori_in_lista(), piatto_piaciuto.sapori_in_lista()))

    print("Il tuo piatto: ",str(piatto_piaciuto))

    barca_nigiri = []
    barca_nigiri.append(trova_piatto(23,menu))
    barca_nigiri.append(trova_piatto(31,menu))
    barca_nigiri.append(trova_piatto(41,menu))
    barca_nigiri.append(trova_piatto(13,menu))

    print("Distanza da un piatto composto: ",distanza_piatto_composto(piatto_piaciuto, cosine_similarity_mod, barca_nigiri))
else:
    print("Piatto non trovato")







