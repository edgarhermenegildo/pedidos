# Cores
cor = ['\033[m',        # 0 Limpa
       '\033[1;31m']    # 1 vermelho


def linha(msg='='):
    """Insere uma linha contendo uma frase dentro
    de 50 caracteres completados por sinal de igual.
    :param msg: (Opcional) Mensagem que vai aparecer na lina.
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
        print(f'{c} - {item}')
        c += 1
    linha()
    opc = opcao('Sua Opção: ')
    return opc