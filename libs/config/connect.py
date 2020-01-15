import pymysql      # Importando biblioteca pymysql, para conectar no bancom de dados.
import dados        # Importando o modulo dados (local).

connect = pymysql.connect(
    host = '172.16.0.100',
    user = dados.userdb,
    passwd = dados.password,
    db = dados.database
    )
