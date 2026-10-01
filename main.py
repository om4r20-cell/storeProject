from models.programa_academico import Programa_academico
from models.asignaturas import asignaturas

programa1 = Programa_academico("Ingenieria de Sistemas", "ISIS01", "Ciencias e Ingenierias", 10, "virtual")
print(programa1.ShowInformation())

Asignaturas1 = asignaturas("Programacion 1", "600189", "3", programa1)

print(Asignaturas1.ShowInformation())