from animal.models import Animal, Especie
from animal.schemas import AnimalCreate, AnimalUpdate, EspecieCreate, EspecieUpdate
from core.cruds import CRUDBase


class CRUDEspecie(CRUDBase[Especie, EspecieCreate, EspecieUpdate]):
    pass


especie = CRUDEspecie(Especie)


class CRUDAnimal(CRUDBase[Animal, AnimalCreate, AnimalUpdate]):
    pass


animal = CRUDAnimal(Animal)
