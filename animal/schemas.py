import datetime
from typing import Optional, Set
from uuid import UUID

from pydantic import BaseModel, EmailStr

# Especie


class EspecieBase(BaseModel):
    enabled: bool = True
    nome: str


class EspecieCreate(EspecieBase):
    pass


class EspecieUpdate(EspecieBase):
    pass


class EspecieInDBBase(EspecieBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Especie(EspecieInDBBase):
    pass


# Additional properties stored in DB
class EspecieInDB(EspecieInDBBase):
    pass


# Animal

class AnimalBase(BaseModel):
    enabled: bool = True
    fk_cliente_id: Optional[int]
    fk_especie_id: Optional[int]
    nome: str
    raca: str
    idade: int
    sexo: str
    observacao: Optional[str]


class AnimalCreate(AnimalBase):
    pass


class AnimalUpdate(AnimalBase):
    pass


class AnimalInDBBase(AnimalBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Animal(AnimalInDBBase):
    pass


# Additional properties stored in DB
class AnimalInDB(AnimalInDBBase):
    pass
