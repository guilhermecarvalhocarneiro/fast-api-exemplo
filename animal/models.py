from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base


class Especie(Base):
    __tablename__ = "animal_especie"

    enabled = Column(Boolean, nullable=False, default=True)
    nome = Column(String(300), nullable=False)


class Animal(Base):
    __tablename__ = "animal_animal"

    enabled = Column(Boolean, nullable=False, default=True)
    fk_cliente_id = Column(ForeignKey("usuario_cliente.id"), nullable=True)
    fk_cliente = relationship("Cliente")
    fk_especie_id = Column(ForeignKey("animal_especie.id"), nullable=True)
    fk_especie = relationship("Especie")
    nome = Column(String(300), nullable=False)
    raca = Column(String(300), nullable=False)
    idade = Column(Integer, nullable=False)
    sexo = Column(String(50), nullable=False)
    observacao = Column(String, nullable=True)
