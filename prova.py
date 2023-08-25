from sushify.piatti import crea_menu

menu = crea_menu("menu_default")

for k in menu:
    print(k)
    piatti = menu[k]
    for p in piatti:
        print("    ",str(p))