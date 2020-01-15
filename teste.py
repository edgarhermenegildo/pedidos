from libs.packeges import interface
from clint.textui import colored
import os

lista = ['Cadastrar Cliente', 'Consultar Cliente', 'Sair']

while True:
    opc = interface.menu(lista)
    if opc == 3:
        interface.titulo('Saindo do Sistema.')
        break
    else:
        print(colored.red('ERRO! Digite uma opção valida.'))
