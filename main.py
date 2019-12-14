import sqlite3
#w3school.com/sql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

def ingresar_usuario():
    x=()
    documento=input("Ingrese su número de identificación")
    nombre=input("Ingrese su nombre")
    usuario=input("Ingrese su usuario")
    correo=input("Ingrese su correo")
    contraseña=input("Ingrese su contraseña")
    x=(documento,nombre,usuario,correo,contraseña)
    return x

def ingresar_producto():
    y=()
    codigo=int(input("Ingrese el codigo del producto"))
    producto=input("Ingrese el nombre del producto")
    precio=float(input("Ingrese el precio del producto"))
    cantidad=float(input("Ingrese la cantidad del prducto"))
    proveedor=int(input("Ingrese el codigo del proveedor"))
    y=(codigo,producto,precio,cantidad,proveedor)
    return y

def ingresar_proveedor():
    z=()
    codigo=int(input("Ingrese el codigo del proveedor"))
    nombre=input("Ingrese el nombre del proveedor")
    direccion=input("Ingrese la direccion del proveedor")
    telefono=input("Ingrese el telefono del proveedor")
    correo=input("Ingrese el correo del proveedor")
    ciudad=input("Ingrese la ciudad")
    z=(codigo,nombre,direccion,telefono,correo,ciudad)
    return z

#inserta datos a la base de datos
def insertar_usuario():
    datos=ingresar_usuario()
    #conexion a la base de datos
    con_bd = sqlite3.connect('proyecto.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()
    #consultas
    cursor_agenda.execute("INSERT INTO usuarios(documento, nombre, usuario, correo, contraseña) VALUES(?, ?, ?, ?, ?)", datos)
    #se ejecutan los cambios
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()



#inserta datos a la base de datos
def insertar_producto():
    product=ingresar_producto()
    #conexion a la base de datos
    con_bd = sqlite3.connect('proyecto.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()
    #consultas
    cursor_agenda.execute("INSERT INTO productos(codigo,producto,precio,cantidad,proveedor) VALUES(?, ?, ?, ?, ?)", product)
    #se ejecutan los cambios
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()
   
   #inserta datos a la base de datos
def insertar_proveedor():
    provee=ingresar_proveedor()
    #conexion a la base de datos
    con_bd = sqlite3.connect('proyecto.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()
    #consultas
    cursor_agenda.execute("INSERT INTO proveedores(codigo,nombre,direccion,telefono,correo,ciudad) VALUES(?, ?, ?, ?, ?, ?)", provee)
    #se ejecutan los cambios
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()

def consultar():
    #conexion a la base de datos
    con_bd = sqlite3.connect('proyecto.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()
    #consultas

    pregunta=int(input("Ingrese la opción que desea\n 1.Usuarios \n 2.Proveedores\n 3.Productos\n"))
    if pregunta==1:
            comando=input("¿Ingrese la información que desea consultar?").lower()
            id=input("Ingrese el documento sobre el cual desea consultar") 
            ejecucion="SELECT {0} FROM usuarios WHERE documento=? ".format(comando) 
            consulta = cursor_agenda.execute(ejecucion,(id,))
    else:
        if pregunta==2:
            comando=input("¿Ingrese la información que desea consultar?").lower()
            codigo=input("Ingrese el codigo sobre el cual desea consultar") 
            ejecucion="SELECT {0} FROM proveedores WHERE codigo=? ".format(comando) 
            consulta = cursor_agenda.execute(ejecucion,(codigo,))
        else:
            if pregunta==3:
                comando=input("¿Ingrese la información que desea consultar?").lower()
                id=input("Ingrese el codigo sobre el cual desea consultar") 
                ejecucion="SELECT {0} FROM productos WHERE codigo=? ".format(comando) 
                consulta = cursor_agenda.execute(ejecucion,(codigo,))

    #impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()

def borrar_registro():
    #conexion a la base de datos
    con_bd = sqlite3.connect('proyecto.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()
    #consultas

    pregunta=int(input("Ingrese la opción que desea eliminar\n 1.Usuarios \n 2.Proveedores\n 3.Productos\n"))
    if pregunta==1:
            id=input("Ingrese el documento sobre el cual desea eliminar el registro") 
            consulta = cursor_agenda.execute("DELETE FROM  usuarios WHERE documento=? ",(id,))
    else:
        if pregunta==2:
            codigo=input("Ingrese el codifo sobre el cual desea eliminar el registro") 
            consulta = cursor_agenda.execute("DELETE FROM  proveedore WHERE codigo=? ",(codigo,))
        else:
            if pregunta==3:
                codigo=input("Ingrese el documento sobre el cual desea eliminar el registro") 
                consulta = cursor_agenda.execute("DELETE FROM  productos WHERE codigo=? ",(codigo,))

    #impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()

def actualizar_registro():
    #conexion a la base de datos
    con_bd = sqlite3.connect('proyecto.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()
    #consultas

    pregunta=int(input("Ingrese la opción que desea actualizar \n 1.Usuarios \n 2.Proveedores\n 3.Productos\n"))
    if pregunta==1:
        id=input("Ingrese el documento sobre el cual desea actualizar") 
        comando=input("¿Ingrese el campo que desea actulizar?").lower()
        cambio=input("Ingrese le cambio")
        ejecucion="UPDATE usuarios SET {0}=? WHERE documento=? ".format(comando) 
        consulta = cursor_agenda.execute(ejecucion,(cambio,id,))
    else:
        if pregunta==2:
            codigo=input("Ingrese el codigo sobre el cual desea actualizar") 
            comando=input("¿Ingrese el campo que desea actulizar?").lower()
            cambio=input("Ingrese le cambio")
            ejecucion="UPDATE usuarios SET {0}=? WHERE documento=? ".format(comando) 
            consulta = cursor_agenda.execute(ejecucion,(cambio,codigo,))
        else:
            if pregunta==2:
                codigo=input("Ingrese el codigo sobre el cual desea actualizar") 
                comando=input("¿Ingrese el campo que desea actulizar?").lower()
                cambio=input("Ingrese le cambio")
                ejecucion="UPDATE usuarios SET {0}=? WHERE documento=? ".format(comando) 
                consulta = cursor_agenda.execute(ejecucion,(cambio,codigo,))
  
    #impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()


def correo():
    #conexion a la base de datos
    con_bd = sqlite3.connect('proyecto.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()
    #consultas
    #id=input("Ingrese el documento del usuario al cual desea enviar el correo") 
    consulta = cursor_agenda.execute("SELECT correo FROM proveedores WHERE producto='piña'")
    print(consulta)
    for fila in consulta:
        print(fila)
    #impresion de todos los campos
    #conexion a servidor
    proveedor_correo = 'smtp.gmail.com: 587'
    remitente =("danidvc1609@gmail.com") 

    password = ("colombia1694")
    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()
    #autenticacion
    servidor.login(remitente, password)
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print(campo)
            #mensaje 
            mensaje ="2 X 1 en piñas"
            msg = MIMEMultipart()
            msg.attach(MIMEText(mensaje, 'html'))
            msg['From'] = remitente
            msg['To'] = campo
            msg['Subject'] = ("Oferta")
            servidor.sendmail(msg['From'] , msg['To'], msg.as_string())

            #print("Campo de la fila: {0}".format(campo))
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()

menu="Bienvenido al menu, Eliga la opción correspondiente\n"
menu+="1. Usuario\n"
menu+="2. Proveedor\n"
menu+="3. Producto\n"

ingreso=int(input(menu))

if ingreso==1:
    menu="eliga la opción correspondiente: \n"
    menu+="1. Registrar Usuario\n"
    menu+="2. Actualizar Usuario\n"
    menu+="3. Consultar Usuario\n"
    menu+="4. Eliminar Usuario\n"
    opcion=int(input(menu))
    if opcion==1:
        insertar_usuario()
    else:
        if opcion==2:
            actualizar_registro()
        else:
            if opcion==3:
                consultar()
            else:
                if opcion==4:
                    borrar_registro()
else:
    if ingreso==2:
        menu="eliga la opción correspondiente: \n"
        menu+="1. Registrar Proveedor\n"
        menu+="2. Actualizar Proveedor\n"
        menu+="3. Consultar Proveedor\n"
        menu+="4. Eliminar Proveedor\n"
        opcion=int(input(menu))
        if opcion==1:
            insertar_proveedor()
        else:
            if opcion==2:
                actualizar_registro()
            else:
                if opcion==3:
                    consultar()
                else:
                    if opcion==4:
                        borrar_registro()
    else:
        if ingreso==3:
            menu="eliga la opción correspondiente: \n"
            menu+="1. Registrar Producto\n"
            menu+="2. Actualizar Producto\n"
            menu+="3. Consultar Producto\n"
            menu+="4. Eliminar Producto\n"
            opcion=int(input(menu))
            if opcion==1:
                insertar_producto()
            else:
                if opcion==2:
                    actualizar_registro()
                else:
                    if opcion==3:
                        consultar()
                    else:
                        if opcion==4:
                            borrar_registro()



