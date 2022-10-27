class Alumno():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(nota):
        if nota > 5:
            print('Has aprobrado')
        else:
            print('Has suspendido')

    def __str__(self):
        return Alumno.__str__(self) + 'el nombre es {}'.format(self.nombre)

Alumno = [{'Mario', 10},{'Juan', 6},{'Alvaro', 10}]

