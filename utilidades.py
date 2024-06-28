import random
import math



nivel = {}
def registrar_alumno():

  try:

    notas = random.randint(1, 10)
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    edad= int(input("Ingrese la edad del alumno: "))
    nivel = int(input("Ingrese el nivel de alumno : "))

    curso[notas] = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'nivel': nivel
        }

    print(f"alumno agregado exitosamente {nombre}!")

  except ValueError:
    print("Error: Ingreso de datos inválidos. Asegúrese de ingresar los solicitado.")



def lista_alumnos():

  if nivel:
    for nivel, datos in nivel.items():
        print(f"notas: {notas}")
        print(f"nombre: {datos['nombre']}")
        print(f"apellido: {datos['apellido']}")
        print(f"edad: {datos['edad']}")
        print(f"nivel: {', '.join(datos['nivel'])}")
  else:
        print("el alumno no esta registrado.")



def buscar_alumno():
  try:
    codigo_buscar = int(input("Ingrese el nivel que desea buscar: "))
    if codigo_buscar in nivel:
        datos=nivel[codigo_buscar]
        print(f"Nombre: {datos['nombre']}")
        print(f"apellido: {datos['apellido']}")
        print(f"notas: {datos['notas']}")
        print(f"nivel: {', '.join(datos['nivel'])}")
    else:
        print("No se encontró ningun alumno en ese nivel registrado en nuestra base de datos.")
  except ValueError:
        print("Error: Ingrese lo solicitado.")



def guardar_alumno():
  try:
    with open("archivo.txt", "w") as archivo:
        for notas, datos in nivel.items():
            archivo.write(f"notas: {notas}\n")
            archivo.write(f"Nombre: {datos['nombre']}\n")
            archivo.write(f"apellido: {datos['apellido']}\n")
            archivo.write(f"edad: {datos['categoria']}\n")
            archivo.write(f"nivel: {', '.join(datos['nivel'])}\n")
           

    print("alumnos guardados en archivo.txt")

  except Exception as e:

    print(f"Error al guardar los alumnos: {e}")

    def promedio_notas():
        promedio=({sum.notas/totalnotas})
        print(f"el promedio del alumno es: {promedio}")


def menu():

    while True:
        print("Menú de Usuario")
        print("1. registrar alumno")
        print("2. lista alumnos")
        print("3. buscar alumno")
        print("4. cacular promedio de notas del alumno")
        print("5. Salir")

        try:

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_alumno()
            elif opcion == 2:
                lista_alumnos()
            elif opcion == 3:
                buscar_alumno()
            elif opcion == 4:
                promedio_notas()
            elif opcion == 5:
                guardar_alumno()
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número válido.")
