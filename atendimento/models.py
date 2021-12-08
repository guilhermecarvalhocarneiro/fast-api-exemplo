from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from core.database import Base

atendimento_agendamento_servico = Table(
    "atendimento_agendamento_servico",
    Base.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("agendamento_id", ForeignKey("atendimento_agendamento.id")),
    Column("servico_id", ForeignKey("servico_servico.id")),
)


class Agendamento(Base):
    __tablename__ = "atendimento_agendamento"

    enabled = Column(Boolean, nullable=False, default=True)
    fk_cliente_id = Column(ForeignKey("usuario_cliente.id"), nullable=False)
    fk_cliente = relationship("Cliente")
    fk_profissional_id = Column(ForeignKey("usuario_profissional.id"), nullable=True)
    fk_profissional = relationship("Profissional")
    fk_animal_id = Column(ForeignKey("animal_animal.id"), nullable=True)
    fk_animal = relationship("Animal")
    data_solicitacao = Column(DateTime, nullable=True)
    data_agendamento = Column(DateTime, nullable=False)
    data_confirmacao = Column(DateTime, nullable=True)
    observacao = Column(String, nullable=True)
    endereco_atendimento = Column(String, nullable=True)
    etapa = Column(String(30), nullable=False, default="Agendado")
    fk_servico = relationship("Servico", secondary=atendimento_agendamento_servico)


class Atendimento(Base):
    __tablename__ = "atendimento_atendimento"

    enabled = Column(Boolean, nullable=False, default=True)
    fk_agendamento_id = Column(ForeignKey("atendimento_agendamento.id"), nullable=False)
    fk_agendamento = relationship("Agendamento")
    fk_atendente_id = Column(ForeignKey("usuario_profissional.id"), nullable=True)
    fk_atendente = relationship("Profissional")
    inicio = Column(DateTime, nullable=False)
    fim = Column(Date, nullable=False)
    ocorrencia = Column(String, nullable=True)
    valor_cobrado = Column(Float, nullable=False)
    valor_pago = Column(Float, nullable=False)


class Avaliacao(Base):
    __tablename__ = "atendimento_avaliacao"

    enabled = Column(Boolean, nullable=False, default=True)
    fk_atendimento_id = Column(ForeignKey("atendimento_atendimento.id"), nullable=False)
    fk_atendimento = relationship("Atendimento")
    nota = Column(Integer, nullable=False)
    critica = Column(String, nullable=True)
    sugestao = Column(String, nullable=True)
    observacao = Column(String, nullable=True)
    satisfatorio = Column(Boolean, nullable=False, default=True)
