class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
      self.__lista_pacientes = []
    #   self.__lista_pacientes = {}
      self.__numero_pacientes = len(self.__lista_pacientes)
      
    def ingresarPaciente(self):
        # Actualización de la cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPaciente(self):
        cedula = int(input("Ingrese la cedula a buscar: "))
        
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cedula: " + str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())

    def verificar(self, c):
        for i in self.__lista_pacientes:
            if c == Paciente.verCedula():
                print("El paciente ya existe.")
                continue
            else:
                print("Continue")
                

    
def main():
    mi_sistema = Sistema()
    while True:
        opcion = int(input("1. Nuevo paciente\n - 2. Numero de paciente\n - 3. Datos paciente\n - 4. Salir:  \n"))
        if opcion == 1:
            # 1- solicito los datos por teclado
            cedula = int(input("Ingrese la cedula: "))   
            mi_sistema.verificar(cedula)
            nombre = input("Ingrese el nombre: ") 
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            # 2- creo el objeto Paciente y le asigno los datos
            p = Paciente()
            p.asignarNombre(nombre)
            p.asignarCedula(cedula)
            p.asignarGenero(genero)
            p.asignarServicio(servicio)
            mi_sistema.__lista_pacientes.append(p)       
            mi_sistema.ingresarPaciente()
        elif opcion == 2:
            print("Ahora hay: " + str(mi_sistema.verNumeroPacientes()))
        elif opcion == 3:
            mi_sistema.verDatosPaciente()
        elif opcion == 4:
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()
    
