

print("")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("This is the game called JOKENPO. Or Rock, Paper or Scissors.")
print("You have to choose: Rock(R), Paper(P) or Scissors(S).")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("")

# p1 = input("Qual nome do player 1: ")
# p2 = input("Qual nome do player 2: ")
p1 = "Dani"
p2 = "Gisi"
vencedor = ''
print(f"player 1 = {p1}")
print(f"player 2 = {p2}")
print("")

def full_name():
    global p1_choice
    global p2_choice
    if p1_choice.upper() == "R":
        p1_choice = "Rocha"
    elif p1_choice.upper() == "P":
        p1_choice = "Paper"
    elif p1_choice.upper() == "S":
        p1_choice = "Scissors"
    else:
        print("Encontramos um erro. Provavelmente voce digitou algo diferente de R, P ou S")
    if p2_choice.upper() == "R":
        p2_choice = "RocK"
    elif p2_choice.upper() == "P":
        p2_choice = "Paper"
    elif p2_choice.upper() == "S":
        p2_choice = "Scissors"
    else:
        print("Encontramos um erro. Provavelmente voce digitou algo diferente de R, P ou S")


def possibilidades():
    global p1
    global p2
    global vencedor
    if p1_choice == "R" and p2_choice == "R":
        vencedor = "Empate"
    elif p1_choice == 'R' and p2_choice == "P":
        vencedor = p2
    elif p1_choice == 'R' and p2_choice == "S":
        vencedor = p1
    elif p1_choice == 'P' and p2_choice == "R":
        vencedor = p1
    elif p1_choice == 'P' and p2_choice == "P":
        vencedor = "Empate"
    elif p1_choice == 'P' and p2_choice == "S":
        vencedor = p2
    elif p1_choice == 'S' and p2_choice == "R":
        vencedor = p2
    elif p1_choice == 'S' and p2_choice == "P":
        vencedor = p1
    elif p1_choice == 'S' and p2_choice == "S":
        vencedor = "Empate"
    



while True:
    p1_choice = input(f"{p1} voce escolhe R, P or S?").upper()
    print("")
    p2_choice = input(f"{p2} voce escolhe R, P or S?").upper()
    print("")
    possibilidades()
    full_name()
    print(f"{p1} escolheu {p1_choice} e {p2} escolheu {p2_choice}")
    print("")
    print(f"=-=-=-=-   O vencedor foi: {F" ### {vencedor} ###   =-=-=-=-=-="}")
    print(f"")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("PROXIMA RODADA")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("")