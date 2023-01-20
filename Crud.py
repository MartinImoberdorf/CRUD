import sqlite3
import os
import time

#CREAR BBDD
def Crear_BBDD():
    print(chr(27)+"[1;37m" +"")
    conexion=sqlite3.connect('BBDD')

    cursor=conexion.cursor()

    try:
        cursor.execute("""CREATE TABLE Usuarios(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre text,
                Apellido text,
                Mail text,
                Telefono INTEGER

                )""")
        
        print(chr(27)+"[0;32m" + "BBDD,BBDD creada con éxito")
        print(chr(27)+"[1;37m" +"")
        

    except:      
        print(chr(27)+"[0;31m" + "¡Atención!,La BBDD ya existe")
        print(chr(27)+"[1;37m" +"")
        
#CREAR NUEVO USUARIO
def Crear_nuevo_usario():
    print(chr(27)+"[1;37m" +"")
    conexion=sqlite3.connect('BBDD')

    cursor=conexion.cursor()

    print("-"*60)
    print("Registro de usuario:")
    print()

    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    mail=input("Mail:")
    telefono=input("Telefono:")

    try:
        cursor.execute("INSERT INTO Usuarios(nombre,apellido,mail,telefono) VALUES (?,?,?,?)",(nombre,apellido,mail,telefono))
        print(chr(27)+"[0;32m" + "Registro creado correctamente.")
        print(chr(27)+"[1;37m" +"")

    except:
        print(chr(27)+"[0;31m" + "!ERROR! al crear registro.")
        print(chr(27)+"[1;37m" +"")

    conexion.commit()
    conexion.close() 

#LEER DATOS DE UN USARIO
def Leer_datos_usuario():
    print(chr(27)+"[1;37m" +"")
    conexion=sqlite3.connect('BBDD')
    cursor=conexion.cursor()

    print("-"*60)
    print("Datos de usuarios:")
    print()

    nombre=input("Nombre a Buscar: ")
    cursor.execute("SELECT * FROM usuarios")

    elUsuario=cursor.fetchall()

    for usuario in elUsuario:
        if usuario[1]==nombre:

            os.system("cls")     

            print(chr(27)+"[0;32m" + "Usuario encontrado.")
            print(chr(27)+"[1;37m" +"")

            time.sleep(3)

            print("-"*60)
            print("Datos del usuario:")
            print()

            print("ID: ",usuario[0])
            print("Nombre: ",usuario[1])
            print("Apellido: ",usuario[2])
            print("Mail: ",usuario[3])
            print("Telefono: ",usuario[4])
        

#ACTUALIZAR BASE DE DATOS
def Actualizar_Datos():
    print(chr(27)+"[1;37m" +"")
    conexion=sqlite3.connect('BBDD')
    cursor=conexion.cursor()

    print("-"*60)
    print("Actualizar datos de usuarios:")
    print()

    nombre_Anterior=input('Digite el nombre a cambiar: ')
    nombre_nuevo=input('Digite el nuevo nombre: ')

    try:
        cursor.execute('UPDATE Usuarios SET nombre= ? WHERE nombre=?',(nombre_nuevo,nombre_Anterior))
        print(chr(27)+"[0;32m" + "Registro actualizado con exito.")
        print(chr(27)+"[1;37m" +"")

    except:
        print(chr(27)+"[0;31m" + "¡Atención!,algo falló.")
        print(chr(27)+"[1;37m" +"")

    conexion.commit()

#ELIMINAR USUARIOS 
def Eliminar_Datos():
    print(chr(27)+"[1;37m" +"")
    conexion=sqlite3.connect('BBDD')
    cursor=conexion.cursor()

    print("-"*60)
    print("Eliminar usuarios:")
    print()

    nombre=input('nombre:')
    apellido=input('apellido:')

    cursor.execute('DELETE  FROM Usuarios WHERE nombre=? AND apellido=?',(nombre,apellido))

    cursor.fetchall()
    conexion.commit()



#MOSTRAR TODOS LOS DATOS
def Mostrar_datos():
    try:
        conexion=sqlite3.connect('BBDD')
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM Usuarios" )
        
        datos=cursor.fetchall()

        print("-"*60)
        print("- Usuarios -")
        print("ID - NOMBRE - MAIL - TELEFONO")

        for x in datos:
            print(x)

    except:
        Crear_BBDD()

def EliminarBBDD():
    conexion=sqlite3.connect('BBDD')
    cur = conexion.cursor()
    cur.execute('DELETE FROM Usuarios')
    conexion.commit()





def main():
    opcion=None

    while opcion !=8:
        print("-"*60)
        print("Registro de usuario:")
        print("-"*60)
        print()

        print('1 - Crear BBDD.')
        print('2 - Creación nuevo usuario.')
        print('3 - Datos de usuario particular.')
        print('4 - Actualizar usuarios.')
        print('5 - Eliminar usuarios.')
        print('6 - Mostrar todos los usuarios.')
        print('7 - Borrar todos los usuarios.')
        print('8 - Salir.')

        print()

        opcion=int(input("Digite la opcion a elegir: "))
        os.system("cls")

        if opcion==1:
            Crear_BBDD()
            time.sleep(3)
            os.system("cls")
            main()
            
        elif opcion==2:
            Crear_nuevo_usario()
            time.sleep(3)
            os.system("cls")
            main()

        elif opcion==3:
            Leer_datos_usuario()
            print()
            input('Presione enter para continuar...')
            os.system("cls")
            main()

        elif opcion==4:
            Actualizar_Datos()
            print()
            input('Presione enter para continuar...')
            os.system("cls")
            main()

        elif opcion==5:
            Eliminar_Datos()
            print()
            input('Presione enter para continuar...')
            os.system("cls")
            main()
            
        elif opcion==6:
            print()
            Mostrar_datos()
            print()
            input('Presione enter para continuar...')
            os.system("cls")
            main()
        
        elif opcion==7:
            print()
            EliminarBBDD()
            print()
            input('Presione enter para continuar...')
            os.system("cls")
            main()
        
        elif opcion==8:
            break

            
        elif opcion!=78:
            print()
            print("-"*60)
            print('Error! Opción INCORRECTA')
            print("-"*60)
            print()
        
        input('Presione enter para continuar...')
        os.system("cls")


if __name__=='__main__':
    main()