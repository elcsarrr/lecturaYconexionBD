from sqlite3 import Cursor
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        user='root', 
        password='',
        host='127.0.0.1', 
        database='condominio'
    )
    if conexion.is_connected():
        print("conexion exitosa")
        cursor=conexion.cursor()#un cursor es un objeto relacionado con las bases de datos, hace lecturas de datos, inserciones,actualiza 
        cursor.execute("SELECT database();")
        registro=cursor.fetchone()
        print("conectado a la BD",registro)# las ultimas 3 lineas es para ver si esta conectado a la base de datos
        cursor.execute("SELECT * FROM tipousuario")#lectura de la tabla tipousuario
        resultados=cursor.fetchall()
        for fila in resultados:
            print(fila[0],fila[1],fila[2]) #alverga cada uno de los registros
        print("total de registros", cursor.rowcount)

except Error as ex:
    print("error durante la conexion",ex )
finally:
    if conexion.is_connected():
        conexion.close() # se cerro la conexion a la 80.
        print ("la conexion ha finalizado")
