from libs.packeges import interface
from libs.config import connect
from clint.textui import colored
import getpass
import os

lista = ['Cadastrar Cliente', 'Consultar Cliente', 'Sair']
flag = cont = 0
while True:
    login = str(input('Login: ')).strip().lower()
    passwd = getpass.getpass('Digite sua senha: ')
    cursor = connect.conexao.cursor()
    cursor.execute('SELECT username, password FROM tbl_staff')
    resultado = cursor.fetchall()
    for Login, Passwd in resultado:
        if Login == login and Passwd == passwd:
            flag += 1
            print('Login efetuado com sucesso.')
            while True:
                opc = interface.menu(lista)
                if opc == 3:
                    interface.titulo('Saindo do Sistema.')
                    break
                else:
                    print(colored.red('ERRO! Digite uma opção valida.'))
    cont += 1
    if flag == 1 or cont == 3:
        break
    print('Login ou tenha invalido.')


