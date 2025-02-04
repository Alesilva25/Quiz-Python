print("Seja muito bem vindo ao Quiz do Ale!")
answer_user = input("Quer começar? (S/N) ").upper()
print(answer_user)

if answer_user != "S":
    quit()

print("Começando...\n")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer1 = input("Resposta: ").upper()

if answer1 == "A":
    print("Correto!\n")
else: 
    print("Incorreto\n")

print("Qual o nome do protagonista do jogo GTA San Andreas?\n (A) Carlos John\n (B) Carl Johnson\n (C) Carl Jaqueline\n (D) Carlos Jonhson")
answer2 = input("Resposta: ").upper()

if answer2 == "B":
    print("Correto!\n")
else:
    print("Incorreto\n")