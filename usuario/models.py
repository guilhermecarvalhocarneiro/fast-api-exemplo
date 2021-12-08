from authentication.models import User
from core.database import Base
from servico.models import Servico
from sqlalchemy import (Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String, Table)
from sqlalchemy.orm import relationship


class Usuario(Base):
    __tablename__ = "usuario_usuario"

    enabled = Column(Boolean, nullable=False, default=True)
    cpf = Column(String(11), nullable=True)
    nome = Column(String(300), nullable=False)
    email = Column(String(254), nullable=False)
    telefone = Column(String(100), nullable=True)
    token = Column(String, nullable=True)
    firebase = Column(String, nullable=True)
    access_token = Column(String, nullable=True)
    id_token = Column(String, nullable=True)
    latitude = Column(Float, nullable=True, default=0.0)
    longitude = Column(Float, nullable=True, default=0.0)
    endereco = Column(String, nullable=True)


class Cliente(Base):
    __tablename__ = "usuario_cliente"

    enabled = Column(Boolean, nullable=False, default=True)
    cpf = Column(String(11), nullable=True)
    nome = Column(String(300), nullable=False)
    email = Column(String(254), nullable=False)
    telefone = Column(String(100), nullable=True)
    token = Column(String, nullable=True)
    firebase = Column(String, nullable=True)
    access_token = Column(String, nullable=True)
    id_token = Column(String, nullable=True)
    latitude = Column(Float, nullable=True, default=0.0)
    longitude = Column(Float, nullable=True, default=0.0)
    endereco = Column(String, nullable=True)
    usuario_ptr_id = Column(ForeignKey('usuario_usuario.id'), nullable=False, unique=True)
    usuario_ptr = relationship('Usuario')
    endereco_res = Column(String, nullable=True)
    endereco_com = Column(String, nullable=True)


class Profissao(Base):
    __tablename__ = "usuario_profissao"

    enabled = Column(Boolean, nullable=False, default=True)
    nome = Column(String(300), nullable=False)


usuario_profissional_servico = Table(
    'usuario_profissional_servico', Base.metadata, Column(
        'id', Integer, primary_key=True, index=True), Column(
            'profissional_id', ForeignKey('usuario_profissional.id')), Column(
                'servico_id', ForeignKey('servico_servico.id')))

usuario_profissional_cliente = Table(
    'usuario_profissional_cliente', Base.metadata, Column(
        'id', Integer, primary_key=True, index=True), Column(
            'profissional_id', ForeignKey('usuario_profissional.id')), Column(
                'cliente_id', ForeignKey('usuario_cliente.id')))


class Profissional(Base):
    __tablename__ = "usuario_profissional"

    enabled = Column(Boolean, nullable=False, default=True)
    cpf = Column(String(11), nullable=True)
    nome = Column(String(300), nullable=False)
    email = Column(String(254), nullable=False)
    telefone = Column(String(100), nullable=True)
    token = Column(String, nullable=True)
    firebase = Column(String, nullable=True)
    access_token = Column(String, nullable=True)
    id_token = Column(String, nullable=True)
    latitude = Column(Float, nullable=True, default=0.0)
    longitude = Column(Float, nullable=True, default=0.0)
    endereco = Column(String, nullable=True)
    usuario_ptr_id = Column(ForeignKey('usuario_usuario.id'), nullable=False, unique=True)
    usuario_ptr = relationship('Usuario')
    foto = Column(String(300), nullable=True)
    valor_hora = Column(Float, nullable=True, default=0.0)
    profissao_id = Column(ForeignKey('usuario_profissao.id'), nullable=False)
    profissao = relationship('Profissao')
    especializacao = Column(String(300), nullable=True)
    bio = Column(String, nullable=True)
    aprovado = Column(Boolean, nullable=False, default=False)
    cnpj = Column(String(50), nullable=True)
    banco_codigo = Column(Integer, nullable=True)
    banco_nome = Column(String(250), nullable=True)
    banco_tipo_conta = Column(String(50), nullable=True)
    banco_numero_conta = Column(String(50), nullable=True)
    banco_pix = Column(String, nullable=True)
    servicos = relationship('Servico', secondary=usuario_profissional_servico)
    favorito_clientes = relationship('Cliente', secondary=usuario_profissional_cliente)


class ProfissionalServico(Base):
    __tablename__ = "usuario_profissionalservico"

    enabled = Column(Boolean, nullable=False, default=True)
    profissional_id = Column(ForeignKey('usuario_profissional.id'), nullable=False)
    profissional = relationship('Profissional')
    servico_id = Column(ForeignKey('servico_servico.id'), nullable=False)
    servico = relationship('Servico')
    tempo = Column(Integer, nullable=True)
    valor = Column(Float, nullable=True)
