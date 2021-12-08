import datetime
from typing import Optional, Set
from uuid import UUID

from pydantic import BaseModel, EmailStr

# Categoria


class CategoriaBase(BaseModel):
    enabled: bool = True
    nome: str
    icone: Optional[str]


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(CategoriaBase):
    pass


class CategoriaInDBBase(CategoriaBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Categoria(CategoriaInDBBase):
    pass


# Additional properties stored in DB
class CategoriaInDB(CategoriaInDBBase):
    pass


# TipoServico

class TipoServicoBase(BaseModel):
    enabled: bool = True
    nome: str
    categoria_id: Optional[int]


class TipoServicoCreate(TipoServicoBase):
    pass


class TipoServicoUpdate(TipoServicoBase):
    pass


class TipoServicoInDBBase(TipoServicoBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class TipoServico(TipoServicoInDBBase):
    pass


# Additional properties stored in DB
class TipoServicoInDB(TipoServicoInDBBase):
    pass


# Servico

class ServicoBase(BaseModel):
    enabled: bool = True
    nome: str
    tempo: int
    valor: float
    descricao: Optional[str]
    tipo_servico_id: Optional[int]


class ServicoCreate(ServicoBase):
    pass


class ServicoUpdate(ServicoBase):
    pass


class ServicoInDBBase(ServicoBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Servico(ServicoInDBBase):
    pass


# Additional properties stored in DB
class ServicoInDB(ServicoInDBBase):
    pass
