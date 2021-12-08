import datetime
from uuid import UUID

from pydantic import BaseModel


# ConfiguracaoPix
class ConfiguracaoPixBase(BaseModel):
    enabled: bool = True
    chave: str
    descricao: str
    nome: str
    cidade: str


class ConfiguracaoPixCreate(ConfiguracaoPixBase):
    pass


class ConfiguracaoPixUpdate(ConfiguracaoPixBase):
    pass


class ConfiguracaoPixInDBBase(ConfiguracaoPixBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class ConfiguracaoPix(ConfiguracaoPixInDBBase):
    pass


# Additional properties stored in DB
class ConfiguracaoPixInDB(ConfiguracaoPixInDBBase):
    pass


# PagamentoPix
class PagamentoPixBase(BaseModel):
    enabled: bool = True
    status: str
    atendimento_id: str


class PagamentoPixCreate(PagamentoPixBase):
    pass


class PagamentoPixUpdate(PagamentoPixBase):
    pass


class PagamentoPixInDBBase(PagamentoPixBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class PagamentoPix(PagamentoPixInDBBase):
    pass


# Additional properties stored in DB
class PagamentoPixInDB(PagamentoPixInDBBase):
    pass
