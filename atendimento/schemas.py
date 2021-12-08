import datetime
from typing import Optional, Set
from uuid import UUID

from pydantic import BaseModel, EmailStr

# Agendamento


class AgendamentoBase(BaseModel):
    enabled: bool = True
    fk_cliente_id: int
    fk_profissional_id: Optional[int]
    fk_animal_id: Optional[int]
    data_solicitacao: Optional[datetime.datetime]
    data_agendamento: datetime.datetime
    data_confirmacao: Optional[datetime.datetime]
    observacao: Optional[str]
    endereco_atendimento: Optional[str]
    etapa: str = 'Agendado'


class AgendamentoCreate(AgendamentoBase):
    pass


class AgendamentoUpdate(AgendamentoBase):
    pass


class AgendamentoInDBBase(AgendamentoBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Agendamento(AgendamentoInDBBase):
    pass


# Additional properties stored in DB
class AgendamentoInDB(AgendamentoInDBBase):
    pass


# Atendimento

class AtendimentoBase(BaseModel):
    enabled: bool = True
    fk_agendamento_id: int
    fk_atendente_id: Optional[int]
    fk_usuario_id: Optional[int]
    inicio: datetime.datetime
    fim: datetime.date
    ocorrencia: Optional[str]
    valor_cobrado: float
    valor_pago: float


class AtendimentoCreate(AtendimentoBase):
    pass


class AtendimentoUpdate(AtendimentoBase):
    pass


class AtendimentoInDBBase(AtendimentoBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Atendimento(AtendimentoInDBBase):
    pass


# Additional properties stored in DB
class AtendimentoInDB(AtendimentoInDBBase):
    pass


# Avaliacao

class AvaliacaoBase(BaseModel):
    enabled: bool = True
    fk_atendimento_id: int
    nota: int
    critica: Optional[str]
    sugestao: Optional[str]
    observacao: Optional[str]
    satisfatorio: bool = True


class AvaliacaoCreate(AvaliacaoBase):
    pass


class AvaliacaoUpdate(AvaliacaoBase):
    pass


class AvaliacaoInDBBase(AvaliacaoBase):
    id: UUID
    deleted: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Avaliacao(AvaliacaoInDBBase):
    pass


# Additional properties stored in DB
class AvaliacaoInDB(AvaliacaoInDBBase):
    pass
