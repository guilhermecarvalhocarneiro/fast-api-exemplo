from typing import Any, List

from atendimento import cruds, schemas
from authentication import security
from core.database import get_db
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

router_agendamento = APIRouter(
    prefix="/agendamento",
    tags=['agendamento'],
    dependencies=[Depends(security.get_current_active_user)]
)


@router_agendamento.get(
    "/",
    response_model=List[schemas.Agendamento],
    dependencies=[Depends(security.has_permission("atendimento.view_agendamento"))]
)
def read_agendamentos(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 25
) -> Any:
    """
    Retrieve agendamentos.
    """
    agendamentos = cruds.agendamento.get_multi(db, skip=skip, limit=limit)
    return agendamentos


@router_agendamento.post("/", response_model=schemas.Agendamento, dependencies=[
                         Depends(security.has_permission("atendimento.add_agendamento"))])
def create_agendamento(
    *,
    db: Session = Depends(get_db),
    agendamento_in: schemas.AgendamentoCreate,
) -> Any:
    """
    Create new agendamento.
    """
    agendamento = cruds.agendamento.create(db, obj_in=agendamento_in)
    return agendamento


@router_agendamento.get(
    "/{agendamento_id}",
    response_model=schemas.Agendamento,
    dependencies=[
        Depends(
            security.has_permission("atendimento.view_agendamento"))])
def read_agendamento_by_id(
    agendamento_id: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Get a specific agendamento by id.
    """
    agendamento = cruds.agendamento.get(db, id=agendamento_id)
    if not agendamento:
        raise HTTPException(
            status_code=404,
            detail="Esse agendamento não existe no sistema",
        )
    return agendamento


@router_agendamento.put(
    "/{agendamento_id}",
    response_model=schemas.Agendamento,
    dependencies=[
        Depends(
            security.has_permission("atendimento.change_agendamento"))])
def update_agendamento(
    *,
    db: Session = Depends(get_db),
    agendamento_id: str,
    agendamento_in: schemas.AgendamentoUpdate
) -> Any:
    """
    Update a agendamento.
    """
    agendamento = cruds.agendamento.get(db, id=agendamento_id)
    if not agendamento:
        raise HTTPException(
            status_code=404,
            detail="Esse agendamento não existe no sistema",
        )
    agendamento = cruds.agendamento.update(
        db, db_obj=agendamento, obj_in=agendamento_in)
    return agendamento


@router_agendamento.delete(
    "/{id}",
    response_model=schemas.Agendamento,
    dependencies=[
        Depends(
            security.has_permission("atendimento.delete_agendamento"))])
def delete_agendamento(
    *,
    db: Session = Depends(get_db),
    id: str
) -> Any:
    """
    Delete an note.
    """
    agendamento = cruds.agendamento.get(db=db, id=id)
    if not agendamento:
        raise HTTPException(
            status_code=404,
            detail="Esse agendamento não existe no sistema",
        )
    agendamento = cruds.agendamento.remove(db=db, id=id)
    return agendamento


router.include_router(router_agendamento)


router_atendimento = APIRouter(
    prefix="/atendimento",
    tags=['atendimento'],
    dependencies=[Depends(security.get_current_active_user)]
)


@router_atendimento.get(
    "/",
    response_model=List[schemas.Atendimento],
    dependencies=[Depends(security.has_permission("atendimento.view_atendimento"))]
)
def read_atendimentos(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 25
) -> Any:
    """
    Retrieve atendimentos.
    """
    atendimentos = cruds.atendimento.get_multi(db, skip=skip, limit=limit)
    return atendimentos


@router_atendimento.post("/", response_model=schemas.Atendimento, dependencies=[
                         Depends(security.has_permission("atendimento.add_atendimento"))])
def create_atendimento(
    *,
    db: Session = Depends(get_db),
    atendimento_in: schemas.AtendimentoCreate,
) -> Any:
    """
    Create new atendimento.
    """
    atendimento = cruds.atendimento.create(db, obj_in=atendimento_in)
    return atendimento


@router_atendimento.get(
    "/{atendimento_id}",
    response_model=schemas.Atendimento,
    dependencies=[
        Depends(
            security.has_permission("atendimento.view_atendimento"))])
def read_atendimento_by_id(
    atendimento_id: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Get a specific atendimento by id.
    """
    atendimento = cruds.atendimento.get(db, id=atendimento_id)
    if not atendimento:
        raise HTTPException(
            status_code=404,
            detail="Esse atendimento não existe no sistema",
        )
    return atendimento


@router_atendimento.put(
    "/{atendimento_id}",
    response_model=schemas.Atendimento,
    dependencies=[
        Depends(
            security.has_permission("atendimento.change_atendimento"))])
def update_atendimento(
    *,
    db: Session = Depends(get_db),
    atendimento_id: str,
    atendimento_in: schemas.AtendimentoUpdate
) -> Any:
    """
    Update a atendimento.
    """
    atendimento = cruds.atendimento.get(db, id=atendimento_id)
    if not atendimento:
        raise HTTPException(
            status_code=404,
            detail="Esse atendimento não existe no sistema",
        )
    atendimento = cruds.atendimento.update(
        db, db_obj=atendimento, obj_in=atendimento_in)
    return atendimento


@router_atendimento.delete(
    "/{id}",
    response_model=schemas.Atendimento,
    dependencies=[
        Depends(
            security.has_permission("atendimento.delete_atendimento"))])
def delete_atendimento(
    *,
    db: Session = Depends(get_db),
    id: str
) -> Any:
    """
    Delete an note.
    """
    atendimento = cruds.atendimento.get(db=db, id=id)
    if not atendimento:
        raise HTTPException(
            status_code=404,
            detail="Esse atendimento não existe no sistema",
        )
    atendimento = cruds.atendimento.remove(db=db, id=id)
    return atendimento


router.include_router(router_atendimento)


router_avaliacao = APIRouter(
    prefix="/avaliacao",
    tags=['avaliacao'],
    dependencies=[Depends(security.get_current_active_user)]
)


@router_avaliacao.get(
    "/",
    response_model=List[schemas.Avaliacao],
    dependencies=[Depends(security.has_permission("atendimento.view_avaliacao"))]
)
def read_avaliacaos(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 25
) -> Any:
    """
    Retrieve avaliacaos.
    """
    avaliacaos = cruds.avaliacao.get_multi(db, skip=skip, limit=limit)
    return avaliacaos


@router_avaliacao.post("/", response_model=schemas.Avaliacao, dependencies=[
                       Depends(security.has_permission("atendimento.add_avaliacao"))])
def create_avaliacao(
    *,
    db: Session = Depends(get_db),
    avaliacao_in: schemas.AvaliacaoCreate,
) -> Any:
    """
    Create new avaliacao.
    """
    avaliacao = cruds.avaliacao.create(db, obj_in=avaliacao_in)
    return avaliacao


@router_avaliacao.get(
    "/{avaliacao_id}",
    response_model=schemas.Avaliacao,
    dependencies=[
        Depends(
            security.has_permission("atendimento.view_avaliacao"))])
def read_avaliacao_by_id(
    avaliacao_id: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Get a specific avaliacao by id.
    """
    avaliacao = cruds.avaliacao.get(db, id=avaliacao_id)
    if not avaliacao:
        raise HTTPException(
            status_code=404,
            detail="Esse avaliacao não existe no sistema",
        )
    return avaliacao


@router_avaliacao.put(
    "/{avaliacao_id}",
    response_model=schemas.Avaliacao,
    dependencies=[
        Depends(
            security.has_permission("atendimento.change_avaliacao"))])
def update_avaliacao(
    *,
    db: Session = Depends(get_db),
    avaliacao_id: str,
    avaliacao_in: schemas.AvaliacaoUpdate
) -> Any:
    """
    Update a avaliacao.
    """
    avaliacao = cruds.avaliacao.get(db, id=avaliacao_id)
    if not avaliacao:
        raise HTTPException(
            status_code=404,
            detail="Esse avaliacao não existe no sistema",
        )
    avaliacao = cruds.avaliacao.update(
        db, db_obj=avaliacao, obj_in=avaliacao_in)
    return avaliacao


@router_avaliacao.delete("/{id}", response_model=schemas.Avaliacao, dependencies=[
                         Depends(security.has_permission("atendimento.delete_avaliacao"))])
def delete_avaliacao(
    *,
    db: Session = Depends(get_db),
    id: str
) -> Any:
    """
    Delete an note.
    """
    avaliacao = cruds.avaliacao.get(db=db, id=id)
    if not avaliacao:
        raise HTTPException(
            status_code=404,
            detail="Esse avaliacao não existe no sistema",
        )
    avaliacao = cruds.avaliacao.remove(db=db, id=id)
    return avaliacao


router.include_router(router_avaliacao)
