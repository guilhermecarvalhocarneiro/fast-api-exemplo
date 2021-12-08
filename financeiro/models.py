from atendimento.models import Atendimento
from core.database import Base
from sqlalchemy import (Boolean, Column, Date, DateTime, Float, ForeignKey,
                        Integer, String, Table)
from sqlalchemy.orm import relationship


class ContasReceber(Base):
    __tablename__ = "financeiro_contasreceber"

    enabled = Column(Boolean, nullable=False, default=True)
    fk_atendimento_id = Column(ForeignKey('atendimento_atendimento.id'), nullable=False)
    fk_atendimento = relationship('Atendimento')
    status = Column(String(200), nullable=False)
    valor_pago = Column(Float, nullable=False)
    codigo = Column(String(100), nullable=True, unique=True)
    conteudo = Column(String, nullable=True)
