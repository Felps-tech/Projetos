from random import choice

jogador_v = 0
maquina_v = 0


def opcao_jogador():
    esc_jogador = input('Escolha Pedra, Papel ou Tesoura ')
    esc_jogador.lower()

    if esc_jogador == 'pedra':
        return esc_jogador
    elif esc_jogador == 'papel':
        return esc_jogador
    elif esc_jogador == 'tesoura':
        return esc_jogador
    else:
        print('Opcao invalida. Tente novamente')
        opcao_jogador()


def opcao_maquina():
    esc_maquina = choice(['pedra', 'papel', 'tesoura'])
    return esc_maquina


while True:

    print('---' * 30)
    esc_jogador = opcao_jogador()
    esc_maquina = opcao_maquina()
    print('---' * 30)
    print(f'Vitorias do Jogador:{jogador_v}')
    print(f'Vitorias da Maquina:{maquina_v}')
    print('---' * 30)

    if (esc_jogador == 'pedra') and (esc_maquina == 'tesoura') \
        or (esc_jogador == 'papel') and (esc_maquina == 'pedra') \
            or (esc_jogador == 'tesoura') and (esc_maquina == 'papel'):
                    print(f'Jogador escolheu: {esc_jogador} e'
                          f' Maquina escolheu: {esc_maquina}'
                          ' Resultado: Voce ganhou!')
                    jogador_v += 1

    elif (esc_jogador == esc_maquina):
        print(f'Jogador escolheu: {esc_jogador} e'
              f' a Maquina escolheu: {esc_maquina}'
              ' Resultado: Empate!')

    else:
        print(f'Jogador escolheu: {esc_jogador} e'
              f' a Maquina escolheu: {esc_maquina}'
              ' Resultado: A maquina ganhou!')
        maquina_v += 1

    print('---' * 30)

    esc_jogador = input('Jogar Novamente ')

    if esc_jogador in ['SIM', 'Sim', 'SIm', 'sim', 'SiM', 'sIm', 'S', 's']:
        pass
    elif esc_jogador in ['NAO', 'Nao', 'NAo', 'nao', 'NaO', 'nAo', 'N', 'n']:
        break
    else:
        break


'''
def ola_mundo():
    print(ola_mundo)
    ola_mundo()

ola mundo()'''
# loop infinito
