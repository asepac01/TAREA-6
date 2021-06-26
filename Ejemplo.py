class Ejercicios1:
    def __init__(self):
        pass

    def superficie_circulo(self):
        radio= float(input("Ingresar el radio del círculo: "))
        superficie= 3.1416*(radio**2)
        print("La superficie del círculo es {}" .format(superficie))


#EJERCICIO2
totaldecompra=input("Ingrese el total de la compra: ")
desct=totaldecompra*0.15
cantidadapagar=totaldecompra-desct
print("El total de la compra es:{}".format(totaldecompra))


#EJERCICIO3
sueldobase=float(input("Ingrese el valor de su sueldo:  "))
venta1=float(input("Ingrese el valor de su primera venta: "))
venta2=float(input("Ingrese el valor de su segunda venta: "))
venta3=float(input("Ingrese el valor de su tercera venta: "))
comision=(venta1+venta2+venta3)*0.1
print("Su sueldo final es de:{} $".format(sueldobase+comision))

#EJERCICIO4
calificacion=float(input("Ingrese su calificacion: "))
if calificacion>=70:
	print(" APROBADO " )

#EJERCICIO5
notaexamen=float(input("Ingrese la calificacion: "))
if notaexamen>=7 :
	print(" APROBADO " )
else:
 print("REPROBADO")

#EJERCICIO6
sueldo=float(input("Ingrese el sueldo: "))
if sueldo <600:
    print("Usted recibira un aumento en el sueldo por lo tanto ganara:{} $".format((sueldo*0.10)+sueldo))
else:
    print("Su sueldo total es: ",sueldo)

#EJERCICIO7
h_trabajadas, h_extras, h_extras_triple = 0,0,0
valor_hora, pago_horas_extra, pago_total= 0,0,0
h_trabajadas=int(input("Ingrese las horas trabajadas "))
valor_hora=float(input("Ingrese el valor por hora "))
if (h_trabajadas >40):
    h_extras= h_trabajadas -40
    if (h_extras > 8):
        pago_horas_extra=valor_hora*2*8+valor_hora*3*h_extras_triple
    else:
        pago_horas_extra=valor_hora*2*8+valor_hora*3*h_extras_triple
    pago_total=valor_hora*40+pago_horas_extra
else:
    pago_total=valor_hora*h_trabajadas

print("""horastrabajadas: {} Horasextras: {} horastriple:{} valorhora:{}
Pagovalor extra: {} pago total: {}""".format(h_trabajadas,h_extras, h_extras_triple, valor_hora, pago_horas_extra,pago_total))
    
    
#EJERCICIO8
numero1,numero2,numero3=0,0,0
numero1=int(input("Ingrese el numero1: "))
numero2=int(input("Ingrese el numero2: "))
numero3=int(input("Ingrese el numero3: "))
if (numero1>numero2>numero3):
    print(numero1)
elif (numero2>numero1>numero3):
    print(numero2)
else:
    print(numero3)


#EJERCICIO9
numero, v = 0, 0
numero = int(input("Ingrese un número como opción: "))
v = float(input("Ingrese cualquier número que desee: "))

if (numero == 1):
            resp = 100 * v
elif (numero == 2):
            resp = 100 ** v
elif (numero == 3):
            resp = 100 / v
else:
            resp = 0
print('Resultado:', resp)


#EJERCICIO10 
calif1= int(input("Ingresar su primera calificación: "))
calif2= int(input("Ingresar su segunda calificación: "))
if calif1 >=80 and calif2>=80:
    print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(calif1,calif2))
else:
    print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(calif1,calif2))


#EJERCICIO11
suma=0
for i in range(1,101):
	suma+= i**2
print("suma:", suma)


#EJERCICIO12
i=0
while i <= 100:
	i+=1
	print(i) 


#EJERCICIO13
n="si"
sum=0
pro=1
while n!="no":
	num=int(input("ingrese un numero: "))
	sum+=num
	pro=pro*num
	n=input("desea continuar si/no: ")
	n=n.lower()
print("La suma es:{} y el producto es:{}".format(sum,pro))

#EJERCICIO14
suma = 0
producto = 1
numero = 0
        
numero = int(input("Ingrese un número: "))
while (numero != -1):
    suma = suma + numero
    producto = producto * numero
    numero = int(input("Ingresa un número: "))
print("Total de la suma es:", suma)
print("Total del producto:", producto)

#EJERCICIO15
primo, divisor, numero, res = bool, 0, 0, 0
primo = "T"
divisor = 2
numero = int(input("Ingresar un número: "))
while ((divisor < numero) and (primo == "T")):
        res = numero % divisor
        if (res == 0):
             primo = "F"
        divisor = divisor + 1
if primo == "T":
            print("Número", num, "es primo")
else:
            print("Número", num, "no es primo")

#EJERCICIO16
i, numero, serie = 1, 0, 0
bandera = "T"
numero = int(input("Ingrese un número: "))
while (i < numero):
    if bandera == "T":
        serie = serie + (1/i)
        bandera = "F"
    else:
        serie = serie - (1/i)
        bandera = "T"
        i = i + 1
print('Serie:', serie)

#EJERCICIO17
numero = int(input("Ingrese las repeticiones: "))
for i in range(1, numero+1):
    numero = int(input("Ingrese un número: "))
    fac = 1
for j in range(1, numero+1):
    fac = fac * j
print("El factorial del número", numero, "es", fac)

#EJERCICIO18
calificaciones = []
for i in range(10):
    datonuevo = int( input( "Escribe el dato numero {}: ".format(i)))
    calificaciones.append(datonuevo)
print("Las calificaciones son: {}".format(calificaciones))


#EJERCICIO19
nummero, a, b = [], [], []
for i in range(1, 21):
    numero.append(int(input("Ingrese el número {}: ".format(i))))
    if (numero[i-1] > 0):
        a.append(numero[i-1])
    else:
        b.append(numero[i-1])
print("A")
for i in a:
    print(i)
print("B")
for i in b:
    print(i)

#EJERCICIO20
notas_lista = []
estudiantes_lista = []
estudiantes = 30
Casilleros_notas = 6
promedio_examenes = []       
for estudiante in range(1, 31):
    """Grupo de los 30 alumnos"""
    estudiante_temporal = input("Nombre del estudiante {}: ".format(estudiante))
    estudiantes_lista.append(estudiante_temporal)
for nota in range(1, 7):
        print('Escriba la calificación del alumno "{}" en el exámen "{}"'.format(estudiante_temporal, nota))
        """Lectura de las 6 calificaciones de los 30 alumnos"""
        notas_temporal = round(float(input('Nota #{}: '.format(nota))), 2)
        if nota == 1:
                notas_lista.append([notas_temporal])
        else:
                notas_lista[estudiante-1].append(notas_temporal)
        print("")
        
        """Calculo promedio de calificaciones de cada uno de los exámenes"""
        for numero_examen in range(6):
            sumas_notas = 0
            for nota in notas_lista:
                sumas_notas += nota[numero_examen]
            prom = round((sumas_notas/estudiante), 2)
            print('Promedio de exámen {}: {}'.format(numero_examen+1, prom))
        
        """Cálculo del promedio de cada alumno."""
        print("")
        for numero, alumno in enumerate(estudiantes_lista):
            sumas_notas = sum(notas_lista[numero])
            prom = round((sumas_notas/Casilleros_notas), 2)
            print("{} su promedio es: {}".format(alumno, prom))
            
        """Cálculo del tipo de exámen que tuvo mayor promedio de calificación."""
        prom_mayor = 0
        for numero_examen in range(6):
            sumas_notas = 0
            for nota in notas_lista:
                sumas_notas += nota[numero_examen]
            prom = round((sumas_notas/estudiante), 2)
            if prom_mayor < prom:
                prom_mayor = prom
            promedio_examenes.append(prom)
        print("")
        print("El exámen", promedio_examenes.index(prom_mayor)+1,"obtuvo el promedio mayor :", prom_mayor)