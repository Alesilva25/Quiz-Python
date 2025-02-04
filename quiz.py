from colorama import init, Fore

init()

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
default = Fore.WHITE

print("Seja muito bem vindo ao Quiz do Ale!")
answer_user = input("Quer começar? (S/N) ").upper()

if answer_user != "S":
    quit()

print("Começando...\n")
print(f"{yellow}Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n {default}(A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer1 = input("Resposta: ").upper()

if answer1 == "A":
    print(f"{green}Correto!\n {default}")
else: 
    print(f"{red}Incorreto\n {default}")

print(Fore.YELLOW + "Qual o nome do protagonista do jogo GTA San Andreas?\n" + Fore.WHITE + " (A) Carlos John\n (B) Carl Johnson\n (C) Carl Jaqueline\n (D) Carlos Jonhson")
answer2 = input("Resposta: ").upper()

if answer2 == "B":
    print(f"{green}Correto!\n {default}")
else: 
    print(f"{red}Incorreto\n {default}")