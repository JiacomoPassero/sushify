import unittest
import random
from piatti import crea_menu, menu_suggerimento, trova_piatto
from calcolo_distanza import cosine_similarity_mod


class MyTestCase(unittest.TestCase):

    """Controllo che vengano caricati correttamente tutti gli elementi dal file"""
    def test_creazione_menu(self):
        menu = crea_menu()
        s = 0
        for k in menu:
            s = s + len(menu[k])

        self.assertEqual(s,58)

    "controllo che il nuovo menu abbia ordinato i piatti correttamente, verificando con un piatto scelto casualmente"
    def test_ordinamento_menu(self):
        menu = crea_menu()
        piatto = random.randint(1,54)
        piatto = trova_piatto(piatto,menu)

        menu_ordinato = menu_suggerimento(menu,piatto, cosine_similarity_mod)

        for k in menu_ordinato:
            lista = menu_ordinato[k]
            #lo stesso ordine di argomenti con cui sono valutati nella vunzione che crea il menu suggerimento
            lista_punti = list(map(lambda x: cosine_similarity_mod(x.sapori_in_lista(),piatto.sapori_in_lista()), lista))

            self.assertGreaterEqual(True,lista_punti[0] >= all(lista_punti[1::]))

    """Controllo di integrità sulla funzione di ordinamento non causi errore anche con parametri erronei"""
    def test_funzione_ordinamento_errata(self):
        menu = crea_menu()
        piatto = trova_piatto(10, menu)
        #caso funzione sbagliata
        menu_ordinato = menu_suggerimento(menu,piatto,random.randint)
        self.assertEqual(menu_ordinato,{})
        #caso funzione corretta, ma con menu e piatto sbagliati
        menu_ordinato = menu_suggerimento({}, (), cosine_similarity_mod)
        self.assertEqual(menu_ordinato, {})


if __name__ == '__main__':
    unittest.main()
