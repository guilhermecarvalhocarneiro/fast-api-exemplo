from sqlalchemy import Boolean, Column, String

from core.database import Base


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
