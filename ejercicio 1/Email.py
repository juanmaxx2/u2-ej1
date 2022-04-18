class Email:
    __idcuenta=''
    __dominio=''
    __tipodominio=''
    __contrasenia=''
    def __init__(self, idcuenta='', dominio='', tipodominio='', contrasenia=''):
        self.__idcuenta=idcuenta
        self.__dominio=dominio
        self.__tipodominio=tipodominio
        self.__contrasenia=contrasenia
    def retEmail(self):
        return '\n'+self.__idcuenta+'@'+self.__dominio+'.'+self.__tipodominio
    def getdom(self):
        return '\n'+self.__dominio+'.'+self.__tipodominio
    def cambiaContrasenia(self):
        nuevacontrasenia = input ("ingresa su contraseña actual:")
        if (self.__contrasenia == nuevacontrasenia):
            nuevacontrasenia = input ("la nueva contrasenia es:")
            self.__contrasenia = nuevacontrasenia     

import csv
if __name__ == '__main__':
    print ("ingrese datos:")
    idcuenta=input("cuenta:")
    dominio=input("dominio:")
    tipodominio=input("tipo de dominio:")
    contrasenia=input("contraseña:")
    unEmail = Email (idcuenta, dominio, tipodominio, contrasenia)
    returnemail=unEmail.retEmail()
    dom=unEmail.getdom() 
    print(returnemail)
    print(dom)
    print ("\nEstimado " + idcuenta + " te enviaremos tus mensajes a la dirección " + returnemail)
    cambiarcontrasenia = unEmail.cambiaContrasenia()
    lista=[]
    archivo=open('email.csv')
    reader=csv.reader(archivo,delimiter=',')
    dom_ing=input('ingrese dominio a contar:')
    c=0
    for fila in reader:
        lista=fila[0]+fila[1]+fila[2]
        if fila[1]==dom_ing:
            c+=1
    archivo.close()
    print('\ncantidad de emails con el domino ingresado {}'.format(c))
    