import pymysql      # Importando biblioteca pymysql, para conectar no bancom de dados.
import json        # Importando o modulo dados (local).


# Ler arquivo JSON
try:
    arquivo_json = open('/home/edgar/projetos/pedidos/libs/config/config.json', 'r')
    dados_json = json.load(arquivo_json)
except:
    print('Arquivo não encontrado.')
else:
    conexao = pymysql.connect(
        host='172.16.0.100',
        user=dados_json['userdb'],
        passwd=dados_json['password'],
        db=dados_json['database']
        )
finally:
    arquivo_json.close()
