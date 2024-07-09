from colorama import init, Fore, Style

init()

def cabecalho():
    print(Fore.CYAN + "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" + Style.RESET_ALL)
    print("This is the game called JOKENPO. Or Rock, Paper or Scissors.")
    print("You have to choose: Rock(R), Paper(P) or Scissors(S).")
    print(Fore.CYAN + "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" + Style.RESET_ALL)

# p1 = input("Qual nome do player 1: ")
# p2 = input("Qual nome do player 2: ")
p1 = "Dani"
p2 = "Gisi"
vencedor = ''
qtde_p1 = 0
qtde_p2 = 0
qtde_draw = 0

print(f"\nplayer 1 = {p1}")
print(f"player 2 = {p2}")

def next_round():
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("PROXIMA RODADA")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def full_name():
    global p1_choice
    global p2_choice
    if p1_choice.upper() == "R":
        p1_choice = Fore.RED + "Rock" + Style.RESET_ALL
    elif p1_choice.upper() == "P":
        p1_choice = Fore.RED + "Paper" + Style.RESET_ALL
    elif p1_choice.upper() == "S":
        p1_choice = Fore.RED + "Scissors" + Style.RESET_ALL
    else:
        print("Encontramos um erro. Provavelmente voce digitou algo diferente de R, P ou S")
    if p2_choice.upper() == "R":
        p2_choice = Fore.BLUE + "RocK" + Style.RESET_ALL
    elif p2_choice.upper() == "P":
        p2_choice = Fore.BLUE + "Paper" + Style.RESET_ALL
    elif p2_choice.upper() == "S":
        p2_choice = Fore.BLUE + "Scissors" + Style.RESET_ALL
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
    

cabecalho()

while True:
    #p1_choice = input(f"{p1} voce escolhe R, P or S?").upper()
    p1_choice = "R"
    # p2_choice = input(f"{p2} voce escolhe R, P or S?").upper()
    p2_choice = "P"
    possibilidades()
    full_name()
    print(f"\n{p1} escolheu {p1_choice} e {p2} escolheu {p2_choice}\n")
    print(Fore.GREEN + f"###  O vencedor foi: {F" ### {vencedor} ###"}\n" + Style.RESET_ALL)

    # QUANTIDADE DE VEZES QUE CADA PLAYER GANHOU
    if vencedor == p1:
        qtde_p1 += 1
    elif vencedor == p2:
        qtde_p2 += 1
    elif vencedor == "Empate":
        qtde_draw += 1

    # ESCOLHER SE DESEJA CONTINUAR O JOGO OU PARAR
    continuar = input("Pressione Enter para continuar ou digite Q para sair do jogo: ")
    if continuar == "Q" or continuar == 'q':
        print("Voce escolheu sair do jogo. Obrigado e ate logo\n")
        print("RESULTADOS DO JOGO:\n")
    
        print(f"{p1} ganhou {qtde_p1} vezes, {p2} ganhou {qtde_p2} vezes e aconteceram {qtde_draw} empates.")
        break
    else:
        print("Voce escolheu continuar")
    next_round()