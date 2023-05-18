#%%
import mysql.connector
SERVIDOR = 'localhost' 
USUARIO = 'root' 
CONTRASENA = '' 
BD = 'info1_20192' 
cnx = mysql.connector.connect(user=USUARIO,password=CONTRASENA,host=SERVIDOR, database=BD)
cursor = cnx.cursor()

#%% Otra forma
import mysql.connector
cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1', database='informatica1')
cursor = cnx.cursor()
cursor.execute("SELECT * FROM 'ensayo decimal'")
resultado = cursor.fetchall()
print(resultado)
# cursor.execute("INSERT INTO clientes  VALUES(NULL,'PERRO MOJAO', 'MANRIQUE','Antioqiuia',55515919,'MARLON', NULL)")
cursor.close()
cnx.commit()
cnx.close()


#%% Otra forma
import mysql.connector
cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1', database='info1_20192')
cursor = cnx.cursor()
cursor.execute("SELECT * FROM clientes")
resultado = cursor.fetchall()
# print(resultado)
cursor.execute("INSERT INTO clientes  VALUES(NULL,'PERRO MOJAO', 'MANRIQUE','Antioqiuia',55515919,'MARLON', NULL)")
cursor.close()
cnx.commit()
cnx.close()


# %%
import mysql.connector
cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1', database='info1_20192')
cursor = cnx.cursor()
# sql = "CREATE TABLE TablaEnsayo1(ID)"
# print(cursor.execute("CREATE TABLE ensayo( Dpto VARCHAR(20) NOT NULL , NOMBRE INT(20) NOT NULL , CEDULA INT(20) NOT NULL )"))
sql="""UPDATE  CLIENTES SET POBLACIÓN=ANTIOQUIA """
print(cursor.execute(sql))
cursor.close()
cnx.commit()
cnx.close()
