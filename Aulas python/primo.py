# print(primo.__doc__)
__doc__ = 'Esse módulo tem como objetivo retornar se um numero é primo ou não'

def valor_primo(numero):
    # print(primo.primo.__doc__)
    '''
        Essa função tem como objetivo:
            retornar se um número é primo ou não
        Parâmetros (numero):
            1 parâmetro obrigatório - do tipo numérico inteiro        
    '''
    if numero > 1:
        for x in range(2, numero):
            if (numero % x) == 0:
                return 'Esse numero nao eh primo'
        else:
            return 'Esse numero eh primo'
    else:
        return 'Esse numero nao eh primo: numero menor ou igual a 1'

if __name__ == '__main__':
    print('ola mundo do modulo primo')