from colorama import Fore, Style

import pyfiglet

print(Fore.BLUE+ pyfiglet.figlet_format("D E B", font="standard") + Style.RESET_ALL)


def tester():
    while True:
        try:
            text = input(Fore.BLUE + "Entrez un text: " + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "veuillez entrer un text valide" + Style.RESET_ALL)

        if "bonjour " in text.lower():
            print(Fore.GREEN + "ok" + Style.RESET_ALL)
            break
        elif text.lower() == "BONJOUR":
            print(Fore.GREEN + "C'est correcte" + Style.RESET_ALL)

        else:
            print(Fore.RED + "non" + Style.RESET_ALL )   
            
tester()
while True:
    try:
        valeur = int(input(Fore.YELLOW + """Que voulez vous faire?"
                   1.Continuer
                   2.Quitter \n"""+ Style.RESET_ALL)) 
        if valeur == 1:
            tester()
        elif valeur == 2:
            print(Fore.GREEN + "Au revoir"+ Style.RESET_ALL)
            break
        else:
            print("veuillez entrer 1 ou 2") 
         
    except ValueError:
        print("Error OO1: entre un nombre valide")
           
          
          
