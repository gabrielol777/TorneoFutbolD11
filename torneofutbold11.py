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
