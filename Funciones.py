from Estructura import Tarjeta as tar
import os as o
"""Creando un arreglo para guardar las cuentas de los usuarios"""
cuentas = []

def crear_cuenta(num, pin):
    cuenta = tar(num, pin)
    cuentas.append(cuenta)
"""Validar el pin y el numero de tarjeta para iniciar sesion"""
def validando(banca, pin):
    for cuenta in cuentas:
        if cuenta.Numero ==  banca and cuenta.Pin == pin:
            return True
"""Validar que la cantidad para depositar/retirar sea múltiplo de 100"""
def validar(x):
    if  x % 100 == 0:
        return True
    else:
        return False
"""Validar si se posee suficiente dinero para realizar el retiro"""
def validar_saldo(saldo, x):
    if x <= saldo:
        return True
    else:
        return False
"""Entrando a su banca"""
def loger():
    op = 0
    while(op != 2):
        banca = input("Digite su # de cuenta: ")
        pin = input("Ingresa el pin: ")
        if(validando(banca, pin)):
            mainMenu(banca)
        else:
            print("Su # de cuenta o pin son incorrectos...")
            o.system("pause")
"""Mostrando el menu de la cuenta de banco"""
def menu():
        o.system("cls")
        print("1. Deposito")
        print("2. Retiro")
        print("3. Ver saldo")
        op = int(input("Escriba su opción: "))
        return op
"""Operacion para depositar dinero de la cuenta"""
def deposito(banca):
    o.system("cls")
    try:
        for c in cuentas:
            if banca == c.Numero:
                x=int(input("Su monto a depositar es: "))
                if(validar(x)):
                    c.Saldo = c.Saldo + x
                else:
                    print("Lamentablemente no se pudo realizar la transacción")
    except:
        print("Ocurrió un error al depositar, intente de nuevo")
        o.system("pause")
"""Operacion para retirar dinero de la cuenta"""
def retiro(banca):
    o.system("cls")
    try:   
        for c in cuentas:
            if banca == c.Numero:
                x=int(input("Su cantidad a retirar es: "))
                if(validar(x) and validar_saldo(c.Saldo,x)):
                    c.Saldo = c.Saldo - x
                else:
                    print("Lamentablemente no se pudo realizar la transacción debido a que no cuentas con los fondos suficientes")
    except:
        print("Ocurrió un error al retirar, intente de nuevo")
        o.system("pause")
"""Mostrar el saldo de cualquier cuenta registrada"""
def mostrar_saldo(banca):
    o.system("cls")
    try:    
        for c in cuentas:
            if banca == c.Numero:
                print("Su saldo disponible es: ", c.Saldo)
                o.system("pause")
    except:
        print("Error al mostrar el saldo disponible")
        o.system("pause")
"""Menu de operaciones de la cuenta"""
def mainMenu(banca):
    op = 0
    while(op!=4):
        if op == 1: deposito(banca)
        elif op == 2: retiro(banca)
        elif op == 3: mostrar_saldo(banca)
        else: print("Opcion no válida")
        op = menu()