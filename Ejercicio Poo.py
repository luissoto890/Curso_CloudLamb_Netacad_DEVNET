"""Ejercicio: Crear una clase llamada Empleado que tenga variables de instancia para el nombre, 
la edad y el salario, y una variable de clase para llevar un registro del número total de 
empleados creados. Agregar dos métodos a la clase: uno para aumentar el salario y otro para 
mostrar la información del empleado."""

#creando clase Empleado:
class Empleado:
    #creando variable contador para la cantidad de empleados:
    total_empleados = 0
    #creando la clase constructor con las variables de instancia:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        Empleado.total_empleados +=1 #creando el contador de empleados
    
    #creando método para aumentar salario:
    def aumentar_salario(self, aumento):
        self.salario += aumento

#creando método para mostrar información:
    def mostrar_informacion (self):
        return f"El empleado {self.nombre}, tiene {self.edad} años de edad y gana {self.salario}$"
    

#creando objetos y sus instancias:
empleado1 = Empleado("Carlos", 22, 3000)
print (empleado1.mostrar_informacion())

#aplicando el método de aumento de salario y luego mostrando la información actualizada:
empleado1.aumentar_salario(2000)
print (empleado1.mostrar_informacion())

#ahora estoy realizando un breve cambio en este código para ver cómo funciona git y github
print ("Esto es algo nuevo")