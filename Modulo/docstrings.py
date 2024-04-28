
#   Este módulo "PRIMO", está na pasta da estrutura de repetição acima, apenas puxei
#   para utilizar como exemplo nesse módulo!!


__doc__ = "Esse módulo tem como objetivo retornar um número é primo ou não"
           # O texto inserido sai no terminal da documentação

def primo(numero):
    """
    Essa função tem como objetivo:
        retornar se um número é primo ou não
    Parametros: 
        1 parametro obrigatório - tipo númerico inteiro
    """
    if numero > 1:
        for x in range (2, numero):
            if(numero % x) == 0:
                return"Esse não é primo mano!"
        else:
            return "Ele é primo mano!"
    else:
        return"Esse número não é primo: Número menor ou igual a 1"


if __name__ == '__main__':
    print(primo(5))

