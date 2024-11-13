class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota




    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")




    def resultado(self):
        if self.nota >= 7:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"{self.nombre} ha suspendido con una nota de {self.nota}.")




# Ejemplo de uso
alumno1 = Alumno("María", 7)
alumno2 = Alumno("Juan", 4)




alumno1.imprimir_datos()
alumno1.resultado()




alumno2.imprimir_datos()
alumno2.resultado()
