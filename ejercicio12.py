class Estudiante:
    def __init__(self , nombre , edad , curso , materias_pendiente):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.materias_pendiente = materias_pendiente
    
    
    def agregar_estudiante():
        nombre = input('Agregar el nombre del nuevo estudiante : ')
        edad = input('Agregue la edad: ')
        while not edad.isdigit():
            print('Ponga la edad en valor numerico ')
            edad = input('Agregue la edad: ')
        curso = input('Curso: ')
        pendientes = input('Tiene materias pendientes ? si o no? ').lower()
        if pendientes =='si':
            materias_pendiente = input('Cuales tiene pendiente ? ')
        
        else:
            materias_pendiente = 0
            
        print('Liso , ya se registro')
        estudiantes = Estudiante (nombre , edad , curso , materias_pendiente)
        
        
agregar = input('Desea agregar un nuevo estudiante? si o no? ').lower()

while agregar == 'si':
    print(Estudiante.agregar_estudiante())
    agregar = input('Desea agregar un nuevo estudiante? si o no? ').lower()

    
