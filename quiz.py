print("Seja muito bem vindo ao Quiz do Ale!")
answer_user = input("Quer começar? (S/N) ").upper()
print(answer_user)

if answer_user != "S":
    quit()

print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer1 = input("Resposta: ").upper()

if answer1 == "A":
    print("Correto!")
else: 
    print("Incorreto")