from clint.textui import colored


def printc(msg):
    """
    Função para dar um print numa linha centralizado em 80 caracteres.
    :param msg: Mensagem que vai aparecer na linha
    """
    print(colored.blue(f'{msg:^80}'))


def linha(msg='='):
    """Insere uma linha contendo uma frase dentro
    de 50 caracteres completados por sinal de igual.
    :param msg: (Opcional) Mensagem que vai aparecer na linha.
    ex: linha(' TESTE ')
    ===================== TESTE ======================
    """
    print(f'{msg:=^80}')


def titulo(msg):
    """
    Formata o titulo para o programa.
    :param msg: Mensagem que vai aparecer centralizado
    """
    linha()
    print(f'{msg:^80}')
    linha()


def opcao(msg):
    """
    Valida se um input é um número inteiro.
    Se digitar qualquer outro caracter que não seja inteiro
    a função retorna 99.
    Se der Ctrl+c retorna 3
    :param msg: Mensagem do input.
    :return: retorna quando o número for inteiro (n). 
    """
    try:
        n = int(input(msg))
    except (ValueError, TypeError):
        return 99
    except KeyboardInterrupt:
        print()
        return 3
    else:
        return n


def menu(lista):
    """
    Função para criar um menu através de uma lista.
    :param lista: Lista coma as opções do menu.
    :return: Retorna a opção escolhida do menu.
    """
    c = 1
    titulo('Sistema para cadastro de clientes')
    for item in lista:
        printc(f'{c:>3}- {item:<20}')
        c += 1
    linha()
    opc = opcao(colored.green('Sua Opção: '))
    return opc
