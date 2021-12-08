from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime


'''
Arquivo com os  models da app de autenticação

- É configurado o nome da tabela, colunas e relacionamentos
'''

Base = declarative_base()

class ContentType(Base):
    __tablename__ = "django_content_type"

    id = Column(Integer, primary_key=True, index=True)
    app_label = Column(String, nullable=False)
    model = Column(String, nullable=False)

class Permission(Base):
    __tablename__ = "auth_permission"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    content_type_id = Column(Integer, ForeignKey("django_content_type.id"), nullable=False)
    codename = Column(String, nullable=False)
    contentType = relationship("ContentType")


group_permission = Table('auth_group_permissions', Base.metadata,
    Column('group_id', ForeignKey('auth_group.id'), primary_key=True),
    Column('permission_id', ForeignKey('auth_permission.id'), primary_key=True)
)

class Group(Base):
    __tablename__ = "auth_group"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    permissions = relationship("Permission", secondary=group_permission)


user_group = Table('auth_user_groups', Base.metadata,
    Column('group_id', ForeignKey('auth_group.id'), primary_key=True),
    Column('user_id', ForeignKey('auth_user.id'), primary_key=True)
)

class User(Base):
    __tablename__ = "auth_user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    is_staff = Column(Boolean, default=False)
    date_joined  =Column(DateTime, default=datetime.now())
    groups = relationship("Group", secondary=user_group)
