import pymysql      # Importando biblioteca pymysql, para conectar no bancom de dados.
import json        # Importando o modulo dados (local).

# Ler arquivo JSON
try:
    arquivo_json = open('config.json', 'r')
    dados_json = json.load(arquivo_json)
except:
    print('Arquivo não encontrado.')
#connect = pymysql.connect(
#    host = '172.16.0.100',
#    user = dados.userdb,
#    passwd = dados.password,
#    db = dados.database
#    )

print(dados_json)
