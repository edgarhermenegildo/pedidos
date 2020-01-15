from libs.packeges import interface
import os

lista = ['Cadastrar Cliente', 'Consultar Cliente', 'Sair']

while True:
    opc = interface.menu(lista)
    if opc == 3:
        interface.titulo('Saindo do Sitema.')
        break
    else:
        print('ERRO! Digite uma opção valida.')
