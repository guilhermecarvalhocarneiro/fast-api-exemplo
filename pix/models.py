from core.database import Base
from sqlalchemy import (Boolean, Column, Date, DateTime, Float, ForeignKey,
                        Integer, String, Table)
from sqlalchemy.orm import relationship


class ConfiguracaoPix(Base):
    __tablename__ = "pix_configuracaopix"

    enabled = Column(Boolean, nullable=False, default=True)
    chave = Column(String(200), nullable=False)
    descricao = Column(String(200), nullable=False)
    nome = Column(String(200), nullable=False)
    cidade = Column(String(200), nullable=False)


class PagamentoPix(Base):
    __tablename__ = "pix_pagamentopix"

    enabled = Column(Boolean, nullable=False, default=True)
    status = Column(String(200), nullable=False)
    atendimento_id = Column(String(200), nullable=False)
