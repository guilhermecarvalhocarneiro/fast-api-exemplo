import datetime
from typing import Optional, Set
from uuid import UUID

from pydantic import BaseModel, EmailStr

# ContasReceber


class ContasReceberBase(BaseModel):
    enabled: bool = True
    fk_atendimento_id: int
    status: str
    valor_pago: float
    codigo: Optional[str]
    conteudo: Optional[str]


class ContasReceberCreate(ContasReceberBase):
    pass


class ContasReceberUpdate(ContasReceberBase):
    pass


class ContasReceberInDBBase(ContasReceberBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class ContasReceber(ContasReceberInDBBase):
    pass


# Additional properties stored in DB
class ContasReceberInDB(ContasReceberInDBBase):
    pass
