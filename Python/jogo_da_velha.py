jogo = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
jogada = 1
game = True

def funcao_coordenada(ponto):
    global coordenada
    global jogada
    coordenada == ponto
    if jogada % 2 != 0 and jogo[coordenada - 1] == ' ':
        jogada += 1
        return "X"
    elif jogada % 2 == 0 and jogo[coordenada - 1] == ' ':
        jogada += 1
        return "O"
    else:
        print("Posição ocupada!")
        return jogo[coordenada - 1]

def checagem_vitoria():
    global jogada
    global game
    for i in range(0, 9, 3):
        if jogo[i] == jogo[i + 1] == jogo[i + 2] != ' ':
            print(f'Jogador {jogo[i]} ganhou!')
            game = False
            return
    for i in range(0, 7, 3):
        if jogo[i] == jogo[i + 1] == jogo[i + 2] != ' ':
            print(f'Jogador {jogo[i]} ganhou!')
            game = False
            return
    if jogo[0] == jogo[4] == jogo[8] != ' ':
        print(f'Jogador {jogo[0]} ganhou!')
        game = False
        return
    if jogo[2] == jogo[4] == jogo[6] != ' ':
        print(f'Jogador {jogo[2]} ganhou!')
        game = False
        return
    if ' ' not in jogo:
        print("Empate")
        game = False
        return

while game:
    coordenada = int(input("Digite a coordenada da sua jogada \n 1 | 2 | 3 \n ---------- \n 4 | 5 | 6 \n ---------- \n 7 | 8 | 9 \n\n\n     "))
    jogo[coordenada - 1] = funcao_coordenada(coordenada)
    print(f"\n\n\n {jogo[0]} | {jogo[1]} | {jogo[2]} \n ---------- \n {jogo[3]} | {jogo[4]} | {jogo[5]} \n ---------- \n {jogo[6]} | {jogo[7]} | {jogo[8]}")
    checagem_vitoria()
