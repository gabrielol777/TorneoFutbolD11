class Equipo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.goles_favor = 0
        self.goles_contra = 0
        self.diferencia_goles = 0
        self.puntos = 0 

def buscar_equipo(equipos, nombre):
    for equipo in equipos:
        if equipo.nombre.lower() == nombre.lower():
            return equipo
    return None


def registrar_equipo(equipos):
    if len(equipos) < 12:
        nombre = input("Ingrese el nombre del equipo: ").strip()

        while nombre == "" or buscar_equipo(equipos, nombre) is not None:
            if nombre == "":
                print("El nombre no puede estar vacío.")
            else:
                print("Ese equipo ya fue registrado.")

            nombre = input("Ingrese otro nombre: ").strip()

        nuevo_equipo = Equipo(nombre)
        equipos.append(nuevo_equipo)

        print("Equipo registrado correctamente.")
    else:
        print("Ya se registraron los 12 equipos.")

def mostrar_equipos(equipos):
    if len(equipos) == 0:
        print("Todavía no hay equipos registrados.")
    else:
        print("\n--- EQUIPOS REGISTRADOS ---")
        for i in range(len(equipos)):
            print(f"{i + 1}. {equipos[i].nombre}")
        print("---------------------------")


def pedir_goles(mensaje):
    valido = False

    while not valido:
        try:
            goles = int(input(mensaje))

            if goles >= 0:
                valido = True
            else:
                print("Los goles no pueden ser negativos.")

        except ValueError:
            print("Debe ingresar un número entero.")

    return goles


def registrar_partido(equipos):
    if len(equipos) < 2:
        print("Debe haber al menos 2 equipos registrados.")
        return

    mostrar_equipos(equipos)

    nombre_local = input("Ingrese el nombre del equipo local: ").strip()
    equipo_local = buscar_equipo(equipos, nombre_local)

    while equipo_local is None:
        print("El equipo local no existe.")
        nombre_local = input("Ingrese nuevamente el equipo local: ").strip()
        equipo_local = buscar_equipo(equipos, nombre_local)

    nombre_visitante = input("Ingrese el nombre del equipo visitante: ").strip()
    equipo_visitante = buscar_equipo(equipos, nombre_visitante)

    while equipo_visitante is None or equipo_visitante == equipo_local:
        if equipo_visitante is None:
            print("El equipo visitante no existe.")
        else:
            print("Un equipo no puede jugar contra sí mismo.")

        nombre_visitante = input("Ingrese nuevamente el equipo visitante: ").strip()
        equipo_visitante = buscar_equipo(equipos, nombre_visitante)

    goles_local = pedir_goles("Goles del equipo local: ")
    goles_visitante = pedir_goles("Goles del equipo visitante: ")

    equipo_local.partidos_jugados += 1
    equipo_visitante.partidos_jugados += 1

    equipo_local.goles_favor += goles_local
    equipo_local.goles_contra += goles_visitante

    equipo_visitante.goles_favor += goles_visitante
    equipo_visitante.goles_contra += goles_local

    equipo_local.diferencia_goles = equipo_local.goles_favor - equipo_local.goles_contra
    equipo_visitante.diferencia_goles = equipo_visitante.goles_favor - equipo_visitante.goles_contra

    if goles_local > goles_visitante:
        equipo_local.partidos_ganados += 1
        equipo_visitante.partidos_perdidos += 1
        equipo_local.puntos += 3

    elif goles_local < goles_visitante:
        equipo_visitante.partidos_ganados += 1
        equipo_local.partidos_perdidos += 1
        equipo_visitante.puntos += 3

    else:
        equipo_local.partidos_empatados += 1
        equipo_visitante.partidos_empatados += 1
        equipo_local.puntos += 1
        equipo_visitante.puntos += 1

    print("Partido registrado correctamente.")


def mostrar_tabla(equipos):
    if len(equipos) == 0:
        print("No hay equipos registrados.")
        return

    tabla = sorted(
        equipos,
        key=lambda equipo: (
            equipo.puntos,
            equipo.diferencia_goles,
            equipo.goles_favor
        ),
        reverse=True
    )

    print("\n================ TABLA DE POSICIONES ================")
    print(f"{'Pos':<5}{'Equipo':<20}{'PJ':<5}{'PG':<5}{'PE':<5}{'PP':<5}{'GF':<5}{'GC':<5}{'DG':<5}{'PTS':<5}")
    print("-" * 70)

    posicion = 1

    for equipo in tabla:
        print(f"{posicion:<5}"
              f"{equipo.nombre:<20}"
              f"{equipo.partidos_jugados:<5}"
              f"{equipo.partidos_ganados:<5}"
              f"{equipo.partidos_empatados:<5}"
              f"{equipo.partidos_perdidos:<5}"
              f"{equipo.goles_favor:<5}"
              f"{equipo.goles_contra:<5}"
              f"{equipo.diferencia_goles:<5}"
              f"{equipo.puntos:<5}")

        posicion += 1


def mostrar_estadisticas(equipos):
    if len(equipos) == 0:
        print("No hay equipos registrados.")
        return

    total_partidos = 0
    total_goles = 0

    equipo_mas_puntos = equipos[0]
    equipo_mas_goles = equipos[0]
    equipo_mejor_dg = equipos[0]

    for equipo in equipos:
        total_partidos += equipo.partidos_jugados
        total_goles += equipo.goles_favor

        if equipo.puntos > equipo_mas_puntos.puntos:
            equipo_mas_puntos = equipo

        if equipo.goles_favor > equipo_mas_goles.goles_favor:
            equipo_mas_goles = equipo

        if equipo.diferencia_goles > equipo_mejor_dg.diferencia_goles:
            equipo_mejor_dg = equipo

    total_partidos = total_partidos // 2

    if total_partidos > 0:
        promedio_goles = total_goles / total_partidos
    else:
        promedio_goles = 0

    print("\n========== ESTADÍSTICAS DEL TORNEO ==========")
    print(f"Cantidad de equipos: {len(equipos)}")
    print(f"Partidos jugados: {total_partidos}")
    print(f"Total de goles: {total_goles}")
    print(f"Promedio de goles por partido: {promedio_goles:.2f}")
    print(f"Equipo con más puntos: {equipo_mas_puntos.nombre} ({equipo_mas_puntos.puntos} pts)")
    print(f"Equipo con más goles a favor: {equipo_mas_goles.nombre} ({equipo_mas_goles.goles_favor} goles)")
    print(f"Mejor diferencia de gol: {equipo_mejor_dg.nombre} ({equipo_mejor_dg.diferencia_goles})")


def menu():
    equipos = []
    opcion = ""

    while opcion != "6":
        print("\n========== GESTIÓN DE TORNEO AMATEUR ==========")
        print("1. Registrar equipo")
        print("2. Mostrar equipos")
        print("3. Registrar partido")
        print("4. Mostrar tabla de posiciones")
        print("5. Mostrar estadísticas del torneo")
        print("6. Salir")
        print("===============================================")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_equipo(equipos)

        elif opcion == "2":
            mostrar_equipos(equipos)

        elif opcion == "3":
            registrar_partido(equipos)

        elif opcion == "4":
            mostrar_tabla(equipos)

        elif opcion == "5":
            mostrar_estadisticas(equipos)

        elif opcion == "6":
            print("Saliendo del programa...")

        else:
            print("Opción inválida. Intente nuevamente.")


menu() 
