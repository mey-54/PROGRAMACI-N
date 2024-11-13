class Student:
   def __init__(self, fname, lname, dni, direccion, codigo_postal, fechaNacimiento, matricula, curso, estado, añoIngreso):
       super().__init__(fname, lname, dni, direccion, codigo_postal, fechaNacimiento)
       self.matricula = matricula
       self.curso = curso
       self.estado = estado
       self.añoIngreso = añoIngreso




   def printname(self):
       super().printname()




   def print_student_details(self):
       self.print_details()
       print(f"Matrícula: {self.matricula}")
       print(f"Curso: {self.curso}")
       print(f"Estado: {self.estado}")
       print(f"Año de Ingreso: {self.añoIngreso}")



x1 = Student("Malena", "Perez", "41234728", "jonh kennedy 345", "5280", "09/10/2007", "MET235", "4to", "Activo", 2015)
x2 = Student("Pedro", "Lopez", "6885943", "yrigoyen", "5280", "01/02/2003", "TIA908", "5to", "Inactivo", 2017)
x3 = Student("Ana", "Martinez", "1109584", "ataliva herrera", "5280", "03/04/2001", "CER394", "2do", "Activo", 2019)



x1.print_student_details()
print()
x2.print_student_details()
print()
x3.print_student_details()
print()