import csv
import random
import matplotlib.pyplot as plt

def cargar_datos(archivo, delimiter=';'):
    with open(archivo, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        next(reader)  
        return [row for row in reader]


def parsear_rangos_km(rangos):
    min_km, max_km = rangos.replace(' a ', '-').split('-')
    return int(min_km.strip()), int(max_km.strip())


aviones = cargar_datos('Aeronaves.csv')
pilotos = cargar_datos('Pilotos.csv')
desastres = cargar_datos('Desastres.csv')
rutas = {row[0]: parsear_rangos_km(row[1]) for row in cargar_datos('Rutas.csv')}


def generar_id_vuelo(nombre_avion):
    return nombre_avion[:2] + str(random.randint(100, 999))


def seleccionar_avion_y_piloto(duracion_km):

    tipos_posibles = [tipo for tipo, (min_km, max_km) in rutas.items() if min_km <= duracion_km <= max_km]
    if not tipos_posibles:
        return None, None

    tipo_avion = random.choice(tipos_posibles)
    aviones_posibles = [avion for avion in aviones if avion[1].strip() == tipo_avion]
    avion_elegido = random.choice(aviones_posibles) if aviones_posibles else None


    pilotos_posibles = [piloto for piloto in pilotos if piloto[2].strip() == tipo_avion and piloto[1].strip() == 'si']
    piloto_elegido = random.choice(pilotos_posibles) if pilotos_posibles else None

    return avion_elegido, piloto_elegido


def generar_vuelo():
    duracion_km = random.randint(100, 25000)
    avion, piloto = seleccionar_avion_y_piloto(duracion_km)
    if not avion or not piloto:
        return None

    id_vuelo = generar_id_vuelo(avion[0])
    desastre = random.choice(desastres)  
    km_desastre = random.randint(0, duracion_km)
    decision = "Curso normal"
    if(desastre[0] == "Terrorismo"):
      decision = "Aterrizar lo antes posible"
    if(desastre[0] == "Politico"):
      decision = "Buscar otro aeropuerto"
    if(desastre[0] == "Fallas en la Aeronave"):
      decision = "Aterrizar en el mar"
    if(desastre[0] == "Climatico"):
      decision = "Cambiar ruta"

    return [id_vuelo, duracion_km, avion[0], piloto[0], desastre[1], km_desastre, decision]

vuelos = [generar_vuelo() for _ in range(100)]
vuelos = [vuelo for vuelo in vuelos if vuelo is not None]


with open('vuelos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["ID_vuelo", "duracion[km]", "avion elegido", "piloto", "descripcion desastre", "km del desastre", "decision del piloto"])
    for vuelo in vuelos:
        writer.writerow(vuelo)
nDesastres =[0,0,0,0,0]
nVTA=[0,0,0]
for i in vuelos:
  if (i[6] == "Curso normal"):
    nDesastres[0]+=1
  elif(i[6] == "Aterrizar lo antes posible"):
    nDesastres[1]+=1
  elif(i[6] =="Buscar otro aeropuerto"):
    nDesastres[2]+=1
  elif(i[6] =="Aterrizar en el mar"):
    nDesastres[3]+=1
  elif(i[6]=="Cambiar ruta"):
    nDesastres[4]+=1
  if int(i[1])>=100 and (int(i[1]))<10000:
    nVTA[0]+=1
  if int(i[1])>=1000 and (int(i[1]))<10000:
    nVTA[1]+=1
  if int(i[1])>=10000 and (int(i[1]))<25000:
    nVTA[2]+=1
av =[]
nVAv =[0,0,0,0,0,0,0,0,0]

for i in aviones:
  av.append(i[0])
for i in vuelos:
  for j in range(9):
    if (i[2] == av[j]):
      nVAv[j]+=1

aMax= 0
aMin =0
for i in range(8):
  if (nVAv[i]<= nVAv[i+1]):
    aMax=i+1

for i in range(8):
  if(nVAv[i]>=nVAv[i+1]):
    aMin=i+1



pilotos = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in vuelos:
  if (i[3] == "Gonzalo Grau"):
    pilotos[0]+=1
  elif(i[3] == "Franco Iotti"):
    pilotos[1]+=1
  elif(i[3] =="Alejandra Buquete"):
    pilotos[2]+=1
  elif(i[3] =="Ninfa Delgado"):
    pilotos[3]+=1
  elif(i[3]=="Francisco Testa"):
    pilotos[4]+=1
  elif(i[3]=="Paola Barri"):
    pilotos[5]+=1
  elif(i[3]=="Marcelo Iripino"):
    pilotos[6]+=1
  elif(i[3]=="Lucas Rodriguez"):
    pilotos[7]+=1
  elif(i[3]=="Alfredo Montes"):
    pilotos[8]+=1
  elif(i[3]=="Mario Santos"):
    pilotos[9]+=1
  elif(i[3]=="Pablo Medina"):
    pilotos[10]+=1
  elif(i[3]=="Emilio Lamponne"):
    pilotos[11]+=1

pilotomaxvuelos = 0
for j in range (11):
    if(pilotos[j] < pilotos[j+1]):
      pilotomaxvuelos = j+1
pilotomax= ""
if (pilotomaxvuelos == 0):
    pilotomax = "Gonzalo Grau"
elif(pilotomaxvuelos == 1):
    pilotomax = "Franco Iotti"
elif(pilotomaxvuelos == 2):
    pilotomax = "Alejandra Buquete"
elif(pilotomaxvuelos == 3):
    pilotomax = "Ninfa Delgado"
elif(pilotomaxvuelos == 4):
    pilotomax = "Francisco Testa"
elif(pilotomaxvuelos == 5):
    pilotomax = "Paola Barri"
elif(pilotomaxvuelos == 6):
    pilotomax = "Marcelo Iripino"
elif(pilotomaxvuelos == 7):
    pilotomax = "Lucas Rodriguez"
elif(pilotomaxvuelos == 8):
    pilotomax = "Alfredo Montes"
elif(pilotomaxvuelos == 9):
    pilotomax = "Mario Santos"
elif(pilotomaxvuelos == 10):
    pilotomax = "Pablo Medina"
elif(pilotomaxvuelos == 11):
    pilotomax = "Emilio Lamponne"



pilotominvuelos = 0
for j in range (11):
    if(pilotos[j]>pilotos[j+1]):
      pilotominvuelos = j+1
pilotomin= ""
if (pilotominvuelos == 0):
    pilotomin = "Gonzalo Grau"
elif(pilotominvuelos == 1):
    pilotomin = "Franco Iotti"
elif(pilotominvuelos == 2):
    pilotomin = "Alejandra Buquete"
elif(pilotominvuelos == 3):
    pilotomin = "Ninfa Delgado"
elif(pilotominvuelos == 4):
    pilotomin = "Francisco Testa"
elif(pilotominvuelos == 5):
    pilotomin = "Paola Barri"
elif(pilotominvuelos == 6):
    pilotomin = "Marcelo Iripino"
elif(pilotominvuelos == 7):
    pilotomin = "Lucas Rodriguez"
elif(pilotominvuelos == 8):
    pilotomin = "Alfredo Montes"
elif(pilotominvuelos == 9):
    pilotomin = "Mario Santos"
elif(pilotominvuelos == 10):
    pilotomin = "Pablo Medina"
elif(pilotominvuelos == 11):
    pilotomin = "Emilio Lamponne"





def menu():
    print("Menú:")
    print("1. Elegir el tipo de gráfico")
    print("2. Generar el archivo vuelos.csv")
    print("3. Visualizar datos estadísticos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Lógica para el primer ítem del menú
        print("Ha seleccionado la opción 1: Elegir el tipo de gráfico")
        porcentajes_recorridos = [vuelo[5] / vuelo[1] * 100 for vuelo in vuelos if vuelo[1] > 0]  # Asegurarse de que no dividimos por cero

        plt.figure(figsize=(10, 6))
        plt.bar(range(len(porcentajes_recorridos)), porcentajes_recorridos, color='blue')
        plt.title('Porcentaje de Ruta Recorrida Antes del Desastre')
        plt.xlabel('Vuelo')
        plt.ylabel('% de Ruta Recorrida')
        plt.show()

    elif opcion == "2":
   
        print("Ha seleccionado la opción 2: Generar el archivo vuelos.csv")
    elif opcion == "3":

        print("Ha seleccionado la opción 3: Visualizar datos estadísticos")
        print("Hubo ",nVTA[0], " vuelos de avionetas ",nVTA[1]," vuelos de aviones continentales y ",nVTA[2] ," vuelos de aviones transoceanicos","\n","El avion con mas vuelos es el ",av[aMax],"\n","Piloto con mas vuelos", pilotomax,"\n","Piloto con menos vuelos", pilotomin,"\n","Hubo ", nDesastres[0] ," vuelos sin desastres, ", nDesastres[1] ," vuelos con desastres de terrorismo, ", nDesastres[2] ," vuelos con desastres poiliticos, " ,nDesastres[3]," con fallas en la aeronave y  " ,nDesastres[4]," vuelos con problemas climaticos","\n","El avion menos usado es el ",av[aMin])

    elif opcion == "4":
        print("Saliendo del programa...")
        return
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

   
menu()

menu()