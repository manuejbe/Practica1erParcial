from clases.Club import Club, splitearLista
from clases.Empleado import Empleado
from clases.Instalacion import Instalacion
from clases.Pago import Pago
from clases.Persona import Persona
from clases.Reserva import Reserva
from clases.Socio import Socio
import matplotlib.pyplot as plt
from datetime import date
import datetime

#c= Club('river', '1903', 'corrientes 912')
clubes=[] #lista con OBJETOS club de la CLASE Club

def ingreso(archivo):
    print("Bienvenido. Seleccione alguna de las siguientes opciones", '\n',
          "1. Registrarse",'\n',
          "2. Iniciar sesión")
    opcion = verificarNumeroInput("Ingrese la opción: ", "Opcion invalida. Ingrese la opcion que desea elegir: ")
    while opcion not in range(1,3):
        print("Opcion invalida")
        opcion = verificarNumeroInput("Ingrese la opción: ", "Opcion invalida. Ingrese la opcion que desea elegir: ")
    usuario = input("Ingrese usuario: ")
    txt = open(archivo,"r",encoding="utf-8")
    matrizUsuCon = []
    for linea in txt:
        uc = linea[:-1].split(" ")
        matrizUsuCon.append(uc)
    txt.close()
    match opcion:
        case 1:
            esta=True
            while esta==True:
                encontro = False
                for i in range(len(matrizUsuCon)):
                    if matrizUsuCon[i][0] == usuario:
                        encontro=True
                if encontro == True:
                    usuario = input("Este nombre de usuario ya existe, utilice otro: ")
                else:
                    esta=False
            contrasenia = input("Ingrese contraseña: ")
            txt = open(archivo,"a",encoding="utf-8")
            txt.write(usuario + " " + contrasenia + '\n')
            txt.close()
            menuPrincipal()
        case 2:
            sesionIniciada = False
            while (sesionIniciada==False):
                contrasenia = input("Ingrese contraseña: ")
                for i in range(len(matrizUsuCon)):
                    if matrizUsuCon[i][0] == usuario and matrizUsuCon[i][1]==contrasenia:
                        sesionIniciada = True
                if sesionIniciada == False:
                    print("Usuario o contraseña incorrectos. Ingrese los datos nuevamente:")
                    usuario = input("Ingrese usuario: ")
            menuPrincipal()
            


#c.inicializarClub()

def menuPrincipal():
    inicializarListaClubes()
    for c in clubes:
        c.inicializarClub()
    termina=False
    while (not termina):
        print("Menu principal", '\n', 
          "1: Registrar club", '\n',
          "2: Consultar informacion general de un club", '\n',
          "3: Registrar socio en un club", '\n',
          "4: Eliminar socio en un club", '\n',
          "5: Consultar socios de un club", '\n',
          "6: Registrar instalacion en un club", '\n',
          "7: Eliminar instalacion en un club", '\n',
          "8: Consultar instalaciones de un club", '\n',
          "9: Registrar empleado en un club", '\n',
          "10: Consultar empleados de un club", '\n',
          "11: Generar pago en un club", '\n',
          "12: Eliminar pago en un club", '\n',
          "13: Consultar pagos de un club", '\n',
          "14: Crear reserva en una instalacion", '\n', 
          "15: Consultar reservas en una instalacion de un club", '\n',
          "16: Ver un grafico de los socios divididos por rango etario de un club"

          )
        opcionElegida=verificarOpcionMenu("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ", "Opcion invalida. Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ")
        while opcionElegida not in range(17):
            print("Opcion invalida")
            opcionElegida=verificarOpcionMenu("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ", "Opcion invalida. Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ")
        match opcionElegida:
            case 0:
                termina = finalizarPrograma()
            case 1:
                registrarClub()
            case 2:
                consultarInfoClub()
            case 3:
                registrarSocio()
            case 4:
                eliminarSocio()
            case 5:
                consultarSocios()
            case 6:
                registrarInstalacion()
            case 7:
                eliminarInstalacion()
            case 8:
                consultarInstalaciones()
            case 9:
                registrarEmpleado()
            case 10:
                consultarEmpleados()
            case 11:
                generarPago()
            case 12:
                eliminarPago()
            case 13:
                consultarPagos()
            case 14:
                crearReserva()
            case 15:
                consultarReservas()
            case 16:
                graficoEdades()



def verificarExistenciaClub(nombreClub):
    existe=False
    aux=-1
    for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
    datos=[existe, aux]
    return datos

def guardarListaClubes():
    club_text = ''
    for c in clubes:
        club_text += c.nombre + ',' + str(c.anioFundacion) + ',' + c.direccion + '|'
    with open("clubes.txt", "w") as f:
            f.write(club_text)

def inicializarListaClubes():
    with open('clubes.txt', 'r') as d:
        text = d.read()
        ListaClubes = text.split('|')
        ListaClubes = splitearLista(ListaClubes, ',')
        for i in range(len(ListaClubes)):
            if ListaClubes[i] != ['']:
                clubes.append(Club(*ListaClubes[i]))            

def verificarExistenciaInstalacion(codigo, indiceClub):
    existe=False
    aux=-1
    for i in range(len(clubes[indiceClub].lista_instalaciones)):
        if clubes[indiceClub].lista_instalaciones[i].codigoInstalacion==codigo:
            aux=i
            existe=True
    datos=[existe, aux]
    return datos

def verificarNumeroInput(texto1, texto2):
    while True:
        varStr = input(texto1)
        try:
            varInt = int(varStr)
            if varInt > 0:
                break
            else:
                print("Ingreso invalido. Por favor, inténtelo de nuevo.")
        except ValueError:
            print(texto2)
    return varInt

def verificarOpcionMenu(texto1, texto2):
    while True:
        varStr = input(texto1)
        try:
            varInt = int(varStr)
            break
        except ValueError:
            print(texto2)
    return varInt

def verificarInputSinNumeros(texto1, texto2):
    data=input(texto1)
    while (data=="" or tieneNumeros(data)):
        data=input(texto2)
    return data

def verificarInputConNumeros(texto1, texto2):
    data=input(texto1)
    while (data==""):
        data=input(texto2)
    return data

def tieneNumeros(data):
    tiene = False
    for char in data:
        if char.isdigit():
            tiene = True
    return tiene

def verificarInputClub (texto1, texto2):
    data=input(texto1)
    while (data=="" or data=="clubes"):
        data=input(texto2)
    return data

def validarFecha(f):
    esValido = False
    if len(f) == 10:
        esValido = True if (f[0] + f[1] + f[3] + f[4] + f[6] + f[7] + f[8] + f[9]).isdigit() and (f[2] + f[5]) == '--' else False 
    return esValido

def clubGrafico():
        nombreClub=input("Ingrese el nombre del club que quiere consultar informacion: ")
        datos=verificarExistenciaClub(nombreClub)
        while(datos[0]==False):
            nombreClub=input("Ese club no existe. Ingrese el nombre del club que quiere consultar informacion: ")
            datos=verificarExistenciaClub(nombreClub)
        for socio in clubes[datos[1]].lista_socios:
            clubes[datos[1]].agregaEdad(socio.edad)
        clubes[datos[1]].clasifica()
        return clubes[datos[1]].clasificacion

def graficoEdades():
    clasificacion = clubGrafico()
    rangos = ["1-18","18-60","+60"]
    cantidad = []
    for i in clasificacion:
        cantidad.append(i)
    plt.title("Socios por rango etario")
    plt.xlabel("Rangos",loc = "right")
    plt.ylabel("Cantidad")
    plt.bar(rangos,cantidad,color="blue",width=0.5)
    return plt.show()

def finalizarPrograma():
    print('Sesión cerrada, programa finalizado')
    for c in clubes:
        c.guardarClub()
    guardarListaClubes()
    return True

def registrarClub():
    nombre=verificarInputClub("Ingrese el nombre del club: ", "Ingrese un nombre de club valido: ")
    anioFundacionInt=verificarNumeroInput("Ingrese el año de fundacion: ", "Ingrese un año de fundacion valido: ")
    direccion=verificarInputSinNumeros("Ingrese la direccion: ", "Ingrese una direccion de club valida: ")
    try:
        club = Club(nombre, anioFundacionInt, direccion)
    except ValueError:
        print("Ese nombre ya existe")
        return menuPrincipal()
    clubes.append(club)

    print("Se ha registrado el club exitosamente")
    
def consultarInfoClub():
    nombreClub=input("Ingrese el nombre del club que quiere consultar informacion: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Ese club no existe. Ingrese el nombre del club que quiere consultar informacion: ")
        datos=verificarExistenciaClub(nombreClub)
    clubes[datos[1]].presentacion()

def registrarSocio():
    nombre=verificarInputSinNumeros("Ingrese el nombre del socio: ", "Ingrese un nombre valido: ")
    apellido=verificarInputSinNumeros("Ingrese el apellido del socio: ", "Ingrese un apellido valido: ")
    sexo=verificarInputSinNumeros("Ingrese el sexo del socio: ", "Ingrese un sexo valido: ")
    edadInt=verificarNumeroInput("Ingrese la edad del socio: ", "Edad invalida. Ingrese la edad del socio: ")
    dniInt=verificarNumeroInput("Ingrese el DNI del socio: ", "DNI invalido. Ingrese el DNI del socio: ")
    nroSocioInt=verificarNumeroInput("Ingrese el numero de socio: ", "Numero de socio invalido. Ingrese el numero de socio: ")
    correoElectronico=verificarInputConNumeros("Ingrese el correo electronico del socio: ", "Ingrese un correo electronico valido: ")
    nombreClub=input("Ingrese el nombre del club en el que desea registrar el socio: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar el socio: ")
        datos=verificarExistenciaClub(nombreClub)
    socio=Socio(nombre, apellido, sexo, edadInt, dniInt, nroSocioInt, correoElectronico)
    clubes[datos[1]].agregarSocio(socio)

def eliminarSocio():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar un socio: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar un socio: ")
        datos=verificarExistenciaClub(nombreClub)
    nroSocioInt=verificarNumeroInput("Ingrese el numero de socio del socio que desea eliminar: ", "Numero de socio invalido. Intente nuevamente")
    clubes[datos[1]].eliminarSocio(nroSocioInt)

def consultarSocios():
    nombreClub=input("Ingrese el club del que quiere consultar los socios: ")
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0]==False):
        nombreClub=input("Nombre de club inexistente. Ingrese el club del que quiere consultar los socios: ")
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_socios)):
        print ("Nombre:",clubes[datos[1]].lista_socios[j].nombre, ", Apellido:",clubes[datos[1]].lista_socios[j].apellido, ", DNI:",clubes[datos[1]].lista_socios[j].DNI, ", Edad:",clubes[datos[1]].lista_socios[j].edad,'\n')

def registrarInstalacion():
    nombre=verificarInputSinNumeros("Ingrese el nombre de la instalacion: ", "Ingrese un nombre valido: ")
    descripcion=verificarInputSinNumeros("Ingrese la descripcion de la instalacion: ", "Ingrese una descripcion valida: ")
    horaApertura=verificarInputConNumeros("Ingrese la hora de apertura de la instalacion: ", "Ingrese un horario valido: ")
    horaCierre=verificarInputConNumeros("Ingrese la hora de cierre de la instalacion: ", "Ingrese un horario valido: ")
    codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea registrar: ","Ingrese un codigo de instalacion valido: " )    
    nombreClub=input("Ingrese el nombre del club en el que desea registrar la instalacion: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar la instalacion: ")
        datos=verificarExistenciaClub(nombreClub)
    instalacion=Instalacion(nombre, descripcion, horaApertura, horaCierre, codigoInstalacionInt)
    clubes[datos[1]].agregarInstalacion(instalacion)

def eliminarInstalacion():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar una instalacion: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar una instalacion: ")
        datos=verificarExistenciaClub(nombreClub)
    codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea eliminar: ","Ingrese un codigo de instalacion valido: ") 
    clubes[datos[1]].eliminarInstalacion(codigoInstalacionInt)

def consultarInstalaciones():
    nombreClub=input('Ingrese el club del que desea consultar las instalaciones: ')
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar las instalaciones: ')
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_instalaciones)):
        print("Nombre:",clubes[datos[1]].lista_instalaciones[j].nombre, ", Descripcion:",clubes[datos[1]].lista_instalaciones[j].descripcion, ", Codigo:",clubes[datos[1]].lista_instalaciones[j].codigoInstalacion,'\n')

def registrarEmpleado():
    nombre=verificarInputSinNumeros("Ingrese el nombre del empleado: ", "Ingrese un nombre valido: ")
    apellido=verificarInputSinNumeros("Ingrese el apellido del empleado: ", "Ingrese un apellido valido: ")
    sexo=verificarInputSinNumeros("Ingrese el sexo del empleado: ", "Ingrese un sexo valido: ")
    edadInt=verificarNumeroInput("Ingrese la edad del empleado: ", "Edad invalida. Ingrese la edad del empleado: ")
    dniInt=verificarNumeroInput("Ingrese el DNI del empleado: ", "DNI invalido. Ingrese el DNI del empleado: ")
    legajoInt=verificarNumeroInput("Ingrese el numero de legajo del empleado: ", "Numero de legajo invalido. Ingrese el numero de legajo del empleado: ")
    cargo=verificarInputSinNumeros("Ingrese el cargo del empleado: ", "Ingrese un cargo valido: ")
    salarioInt=verificarNumeroInput("Ingrese el salario actual del empleado: ", "Salario invalido. Ingrese el salario del empleado: ")
    nombreClub=input("Ingrese el nombre del club en el que desea registrar el empleado: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar el empleado: ")
        datos=verificarExistenciaClub(nombreClub)
    empleado=Empleado(nombre, apellido, sexo, edadInt, dniInt, legajoInt, cargo, salarioInt)
    clubes[datos[1]].agregarEmpleado(empleado)

def consultarEmpleados():
    nombreClub=input('Ingrese el club del que desea consultar los empleados: ')
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar los empleados: ')
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_empleados)):
        print("Nombre:",clubes[datos[1]].lista_empleados[j].nombre, ", Apellido:",clubes[datos[1]].lista_empleados[j].apellido, ", Cargo:",clubes[datos[1]].lista_empleados[j].cargo,'\n')

def generarPago():
    montoInt=verificarNumeroInput("Ingrese el monto: ", "Monto invalido. Ingrese el monto: ")
    fecha=verificarInputConNumeros("Ingrese la fecha con el formato DD-MM-YYYY: ", "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
    esValido=validarFecha(fecha)
    while esValido==False:
        fecha=verificarInputConNumeros("Formato invalido. Ingrese la fecha con el formato DD-MM-YYYY: ", "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
        esValido=validarFecha(fecha)
    ano=int(fecha[6:])
    mes=int(fecha[3:5])
    dia=int(fecha[0:2])
    while(mes not in range(1,13) or dia not in range(1,32) or ano<0):
        print('Fecha invalida')
        fecha=verificarInputConNumeros("Ingrese la fecha con el formato DD-MM-YYYY: ", "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
        esValido=validarFecha(fecha)
        while esValido==False:
            fecha=verificarInputConNumeros("Formato invalido. Ingrese la fecha con el formato DD-MM-YYYY: ", "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
            esValido=validarFecha(fecha)
        ano=int(fecha[6:])
        mes=int(fecha[3:5])
        dia=int(fecha[0:2])
    fechadt=date(ano, mes, dia)
    codigoPagoInt=verificarNumeroInput("Ingrese el codigo de pago: ", "Codigo de pago invalido. Ingrese el codigo de pago: ")
    nombreClub=input("Ingrese el nombre del club en el que desea generar el pago: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea generar el pago: ")
        datos=verificarExistenciaClub(nombreClub)
    nroSocioInt=verificarNumeroInput("Ingrese el numero de socio: ", "Numero de socio invalido. Ingrese el numero de socio: ")
    pago=Pago(montoInt, fechadt, nroSocioInt, codigoPagoInt)
    clubes[datos[1]].agregarPago(pago)

def eliminarPago():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar un pago: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar un pago: ")
        datos=verificarExistenciaClub(nombreClub)
    nroPagoInt=verificarNumeroInput("Ingrese el numero de pago del pago que desea eliminar: ","Numero de pago invalido. Ingrese el numero de pago del pago que desea eliminar: " )
    clubes[datos[1]].eliminarPago(nroPagoInt)

def consultarPagos():
    nombreClub=input('Ingrese el club del que desea consultar los pagos: ')
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar los pagos: ')
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_pagos)):
        print("Fecha (año/mes/dia):", clubes[datos[1]].lista_pagos[j].fecha, ", Monto:", clubes[datos[1]].lista_pagos[j].monto, ", Numero de socio: ", clubes[datos[1]].lista_pagos[j].nroSocio,'\n')

def crearReserva():
    fecha=verificarInputConNumeros("Ingrese la fecha con el formato DD-MM-YYYY: ", "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
    esValido=validarFecha(fecha)
    while esValido==False:
        fecha=verificarInputConNumeros("Formato invalido. Ingrese la fecha con el formato DD-MM-YYYY: ", "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
        esValido=validarFecha(fecha)
    ano=int(fecha[6:])
    mes=int(fecha[3:5])
    dia=int(fecha[0:2])
    while(mes not in range(1,13) or dia not in range(1,32) or ano<0):
        print('Fecha invalida')
        fecha=verificarInputConNumeros("Ingrese la fecha con el formato DD-MM-YYYY: ", "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
        esValido=validarFecha(fecha)
        while esValido==False:
            fecha=verificarInputConNumeros("Formato invalido. Ingrese la fecha con el formato DD-MM-YYYY: ", "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
            esValido=validarFecha(fecha)
        ano=int(fecha[6:])
        mes=int(fecha[3:5])
        dia=int(fecha[0:2])
    fechadt=date(ano, mes, dia)
    horaReserva=verificarInputConNumeros("Ingrese la hora de reserva:", "Ingrese una hora valida: ")
    nroReservaInt=verificarNumeroInput("Ingrese el numero de reserva: ", "Numero de reserva invalido. Ingrese el numero de reserva: ")
    nombreClub=input("Ingrese el nombre del club en el que desea realizar la reserva: ")
    datos1=verificarExistenciaClub(nombreClub)
    while(datos1[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea realizar la reserva: ")
        datos1=verificarExistenciaClub(nombreClub)
    codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea reservar: ", "Codigo invalido. Ingrese el codigo de la instalacion que desea reservar: ")
    datos2=verificarExistenciaInstalacion(codigoInstalacionInt, datos1[1])
    while(datos2[0]==False):
        print("Instalacion inexistente. Ingrese el codigo de la instalacion que desea reservar: ")
        codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea reservar: ", "Codigo invalido. Ingrese el codigo de la instalacion que desea reservar: ")
        datos2=verificarExistenciaInstalacion(codigoInstalacionInt, datos1[1])
    reserva=Reserva(fechadt, horaReserva, nroReservaInt)
    clubes[datos1[1]].lista_instalaciones[datos2[1]].agregarReserva(reserva)

def consultarReservas():
    nombreClub=input('Ingrese el nombre del club del que desea consultar las reservas de una instalacion: ')
    datos1=verificarExistenciaClub(nombreClub)
    while (datos1[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el nombre del club del que desea consultar las reservas de una instalacion: ')
        datos1=verificarExistenciaClub(nombreClub)
    codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea consultar las reservas: ", "Codigo invalido. Ingrese el codigo de la instalacion que desea consultar las reservas: ")
    datos2=verificarExistenciaInstalacion(codigoInstalacionInt, datos1[1])
    while (datos2[0] == False):
        print("Instalacion inexistente. Ingrese el codigo de la instalacion que desea consultar las reservas: ")
        codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea consultar las reservas: ", "Codigo invalido. Ingrese el codigo de la instalacion que desea consultar las reservas: ")
        datos2=verificarExistenciaInstalacion(codigoInstalacionInt, datos1[1])
    for r in range(len(clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas)):
        print("Fecha:", clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas[r].fecha, ", Hora:", clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas[r].hora,", Numero de reserva:", clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas[r].nroReserva,'\n')

ingreso("archivo.txt")


