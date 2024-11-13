class Vehiculo:
   def __init__(self, marca, modelo, año):
       self.marca = marca
       self.modelo = modelo
       self.año = año


   def mostrar_informacion(self):
       print(f"Marca: {self.marca}")
       print(f"Modelo: {self.modelo}")
       print(f"Año: {self.año}")


class Auto(Vehiculo):
   def __init__(self, marca, modelo, año, tipo_combustible):
       super().__init__(marca, modelo, año)
       self.tipo_combustible=tipo_combustible


   def mostrar_informacion(self):
       super().mostrar_informacion()
       print(f"tipo_combustible: {self.tipo_combustible}")


class Motocicleta(Vehiculo):
   def __init__(self, marca, modelo, año,velocidad_maxima):
       super().__init__(marca, modelo, año)
       self.velocidad_maxima = velocidad_maxima


   def mostrar_informacion(self):
       super().mostrar_informacion()
       print(f"velocidad_maxima: {self.velocidad_maxima}")


class Camion(Vehiculo):
   def __init__(self, marca, modelo, año, capacidad_carga):
       super().__init__(marca, modelo, año)
       self.capacidad_carga = capacidad_carga


   def mostrar_informacion(self):
       super().mostrar_informacion()
       print(f"Capacidad de carga: {self.capacidad_carga}")


auto1 = Auto("Toyota", "Hilux", 2022,"Diesel")




moto2 = Motocicleta("Honda", "Wave 110", 1995, "87 km")




camion3 = Camion("Renault","Kerax" ,"2010", "10 kg")




print("Información del Auto:")
auto1.mostrar_informacion()
print("------------------")
print("Información de la Motocicleta:")
moto2.mostrar_informacion()
print("-----------------------")
print("Información del Camión:")
camion3.mostrar_informacion()
print("------------------------")


