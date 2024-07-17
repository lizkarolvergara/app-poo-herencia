from model.Deportivo import Deportivo
from model.Furgoneta import Furgoneta

objDeportivo = Deportivo("Ferrari", "488", 2021, 330)
print(objDeportivo.descripcion())
print(objDeportivo.tipo())

objFurgoneta = Furgoneta("Volvo", "212", 2022, 300)
print(objFurgoneta.descripcion())
