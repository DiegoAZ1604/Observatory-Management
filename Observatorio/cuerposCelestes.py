class CuerpoCeleste:
    def __init__(self, nombre, masa, densidad):  # constructor
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")
        self.masa = masa
        self.densidad = densidad

    def validar(self):
        if self.masa > 0 and self.densidad > 0:
            return True
        else:
            return False


class Planeta(CuerpoCeleste):
    def __init__(self, nombre, masa, densidad, satelites, perorbital):
        super().__init__(nombre, masa, densidad)
        self.satelites = satelites
        self.perOrbital = perorbital

    def validar(self):
        if super().validar():
            if self.satelites > 0 and self.perOrbital > 0:
                return True
            else:
                return False
        else:
            return False


class Estrella(CuerpoCeleste):
    def __init__(self, nombre, masa, densidad, luminosidad, tempsuperficie):
        super().__init__(nombre, masa, densidad)
        self.luminosidad = luminosidad
        self.tempSuperficie = tempsuperficie

    def validar(self):
        if super().validar():
            if self.luminosidad > 0 and self.tempSuperficie > 0:
                return True
            else:
                return False
        else:
            return False


class Satelite(CuerpoCeleste):
    def __init__(self, nombre, masa, densidad, planetahost):
        super().__init__(nombre, masa, densidad)
        self.planetaHost = planetahost

    def validar(self):
        if super().validar() and isinstance(self.planetaHost, str):
            return True
        else:
            return False
