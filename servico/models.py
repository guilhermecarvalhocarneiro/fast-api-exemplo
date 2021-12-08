from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base


class Categoria(Base):
    __tablename__ = "servico_categoria"

    enabled = Column(Boolean, nullable=False, default=True)
    nome = Column(String(250), nullable=False, unique=True)
    icone = Column(String(100), nullable=True)


class TipoServico(Base):
    __tablename__ = "servico_tiposervico"

    enabled = Column(Boolean, nullable=False, default=True)
    nome = Column(String(250), nullable=False)
    categoria_id = Column(ForeignKey("servico_categoria.id"), nullable=True)
    categoria = relationship("Categoria")


class Servico(Base):
    __tablename__ = "servico_servico"

    enabled = Column(Boolean, nullable=False, default=True)
    nome = Column(String(300), nullable=False)
    tempo = Column(Integer, nullable=False)
    valor = Column(Float, nullable=False)
    descricao = Column(String, nullable=True)
    tipo_servico_id = Column(ForeignKey("servico_tiposervico.id"), nullable=True)
    tipo_servico = relationship("TipoServico")
