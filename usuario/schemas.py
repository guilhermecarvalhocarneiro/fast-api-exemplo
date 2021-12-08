import datetime
from typing import Optional, Set
from uuid import UUID

from pydantic import BaseModel, EmailStr

# Usuario


class UsuarioBase(BaseModel):
    enabled: bool = True
    django_user_id: Optional[int]
    cpf: Optional[str]
    nome: str
    email: EmailStr
    telefone: Optional[str]
    token: Optional[str]
    firebase: Optional[str]
    access_token: Optional[str]
    id_token: Optional[str]
    latitude: Optional[float] = 0.0
    longitude: Optional[float] = 0.0
    endereco: Optional[str]


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(UsuarioBase):
    pass


class UsuarioInDBBase(UsuarioBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Usuario(UsuarioInDBBase):
    pass


# Additional properties stored in DB
class UsuarioInDB(UsuarioInDBBase):
    pass


# Cliente

class ClienteBase(BaseModel):
    enabled: bool = True
    django_user_id: Optional[int]
    cpf: Optional[str]
    nome: str
    email: EmailStr
    telefone: Optional[str]
    token: Optional[str]
    firebase: Optional[str]
    access_token: Optional[str]
    id_token: Optional[str]
    latitude: Optional[float] = 0.0
    longitude: Optional[float] = 0.0
    endereco: Optional[str]
    usuario_ptr_id: int
    endereco_res: Optional[str]
    endereco_com: Optional[str]


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(ClienteBase):
    pass


class ClienteInDBBase(ClienteBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Cliente(ClienteInDBBase):
    pass


# Additional properties stored in DB
class ClienteInDB(ClienteInDBBase):
    pass


# Profissao

class ProfissaoBase(BaseModel):
    enabled: bool = True
    nome: str


class ProfissaoCreate(ProfissaoBase):
    pass


class ProfissaoUpdate(ProfissaoBase):
    pass


class ProfissaoInDBBase(ProfissaoBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Profissao(ProfissaoInDBBase):
    pass


# Additional properties stored in DB
class ProfissaoInDB(ProfissaoInDBBase):
    pass


# Profissional

class ProfissionalBase(BaseModel):
    enabled: bool = True
    django_user_id: Optional[int]
    cpf: Optional[str]
    nome: str
    email: EmailStr
    telefone: Optional[str]
    token: Optional[str]
    firebase: Optional[str]
    access_token: Optional[str]
    id_token: Optional[str]
    latitude: Optional[float] = 0.0
    longitude: Optional[float] = 0.0
    endereco: Optional[str]
    usuario_ptr_id: int
    foto: Optional[str]
    valor_hora: Optional[float] = 0.0
    profissao_id: int
    especializacao: Optional[str]
    bio: Optional[str]
    aprovado: bool = False
    cnpj: Optional[str]
    banco_codigo: Optional[int]
    banco_nome: Optional[str]
    banco_tipo_conta: Optional[str]
    banco_numero_conta: Optional[str]
    banco_pix: Optional[str]


class ProfissionalCreate(ProfissionalBase):
    pass


class ProfissionalUpdate(ProfissionalBase):
    pass


class ProfissionalInDBBase(ProfissionalBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Profissional(ProfissionalInDBBase):
    pass


# Additional properties stored in DB
class ProfissionalInDB(ProfissionalInDBBase):
    pass


# ProfissionalServico

class ProfissionalServicoBase(BaseModel):
    enabled: bool = True
    profissional_id: int
    servico_id: int
    tempo: Optional[int]
    valor: Optional[float]


class ProfissionalServicoCreate(ProfissionalServicoBase):
    pass


class ProfissionalServicoUpdate(ProfissionalServicoBase):
    pass


class ProfissionalServicoInDBBase(ProfissionalServicoBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class ProfissionalServico(ProfissionalServicoInDBBase):
    pass


# Additional properties stored in DB
class ProfissionalServicoInDB(ProfissionalServicoInDBBase):
    pass
