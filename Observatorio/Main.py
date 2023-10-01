import pandas as pd
from cuerposCelestes import *

planetas_data = pd.DataFrame(columns=["Nombre", "Masa", "Densidad", "Satelites", "Período Orbital"])
estrellas_data = pd.DataFrame(columns=["Nombre", "Masa", "Densidad", "Luminosidad", "TemperaturaSuperficial"])
satelites_data = pd.DataFrame(columns=["Nombre", "Masa", "Densidad", "Planeta Anfitrión"])

#  agrega un planeta
def add_planeta():
    nombre = input("Ingrese el nombre del planeta: ")
    masa = float(input("Ingrese la masa del planeta: "))
    densidad = float(input("Ingrese la densidad del planeta: "))
    satelites = int(input("Ingrese el número de satélites del planeta: "))
    perorbital = float(input("Ingrese el período orbital del planeta: "))

    planeta = Planeta(nombre, masa, densidad, satelites, perorbital)
    planetas_data.loc[len(planetas_data)] = [planeta.nombre, planeta.masa, planeta.densidad, planeta.satelites,
                                             planeta.perOrbital]

#  agrega una estrella
def add_estrella():
    nombre = input("Ingrese el nombre de la estrella: ")
    masa = float(input("Ingrese la masa de la estrella: "))
    densidad = float(input("Ingrese la densidad de la estrella: "))
    luminosidad = float(input("Ingrese la luminosidad de la estrella: "))
    tempsuperficie = int(input("Ingrese la temperatura superficial de la estrella: "))

    estrella = Estrella(nombre, masa, densidad, luminosidad, tempsuperficie)
    estrellas_data.loc[len(estrellas_data)] = [estrella.nombre, estrella.masa, estrella.densidad, estrella.luminosidad,
                                               estrella.tempSuperficie]

#  agrega un satelite
def add_satelite():
    nombre = input("Ingrese el nombre del satélite: ")
    masa = float(input("Ingrese la masa del satélite: "))
    densidad = float(input("Ingrese la densidad del satélite: "))
    planetahost = input("Ingrese el nombre del planeta anfitrión del satélite: ")

    satelite = Satelite(nombre, masa, densidad, planetahost)
    satelites_data.loc[len(satelites_data)] = [satelite.nombre, satelite.masa, satelite.densidad, satelite.planetaHost]

#  crea la tabla para visualizar datos
def view_data():
    print("Datos: \n")

    print("\nPlanetas: ")
    print("-" * 85)
    print(f"| {'Nombre':20} | {'Masa':10} | {'Densidad':10} | {'Satelites':10} | {'Período Orbital':20} |")
    print("-" * 85)
    for _, planeta in planetas_data.iterrows():
        print(
            f"| {planeta['Nombre']:20} | {planeta['Masa']:10.2f} | {planeta['Densidad']:10.2f} | {planeta['Satelites']:10} | {planeta['Período Orbital']:20.2f} |")

    print("\nEstrellas: ")
    print("-" * 90)
    print(f"| {'Nombre':20} | {'Masa':10} | {'Densidad':10} | {'Luminosidad':10} | {'Temperatura Superficial':20} |")
    print("-" * 90)
    for _, estrella in estrellas_data.iterrows():
        print(
            f"| {estrella['Nombre']:20} | {estrella['Masa']:10.2f} | {estrella['Densidad']:10.2f} | {estrella['Luminosidad']:10.2f} | {estrella['TemperaturaSuperficial']:20.2f} |")

    print("\nSatelites: ")
    print("-" * 73)
    print(f"| {'Nombre':20} | {'Masa':10} | {'Densidad':10} | {'Planeta Anfitrión':20} |")
    print("-" * 73)
    for _, satelite in satelites_data.iterrows():
        print(
            f"| {satelite['Nombre']:20} | {satelite['Masa']:10.2f} | {satelite['Densidad']:10.2f} | {satelite['Planeta Anfitrión']:20} |")


# crea el menu
while True:
    print("1. Agregar Planeta")
    print("2. Agregar Estrella")
    print("3. Agregar Satélite")
    print("4. Ver Datos")
    print("5. Salir")
    choice = input("Seleccione una opción: ")

    if choice == "1":
        add_planeta()
    elif choice == "2":
        add_estrella()
    elif choice == "3":
        add_satelite()
    elif choice == "4":
        view_data()
    elif choice == "5":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
