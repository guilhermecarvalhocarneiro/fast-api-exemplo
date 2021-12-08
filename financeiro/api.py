from typing import Any, List

from authentication import security
from core.database import get_db
from fastapi import APIRouter, Body, Depends, HTTPException
from financeiro import cruds, schemas
from sqlalchemy.orm import Session

router = APIRouter()

router_contasreceber = APIRouter(
    prefix="/contasreceber",
    tags=['contasreceber'],
    dependencies=[Depends(security.get_current_active_user)]
)


@router_contasreceber.get(
    "/",
    response_model=List[schemas.ContasReceber],
    dependencies=[Depends(security.has_permission("financeiro.view_contasreceber"))]
)
def read_contasrecebers(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 25
) -> Any:
    """
    Retrieve contasrecebers.
    """
    contasrecebers = cruds.contasreceber.get_multi(db, skip=skip, limit=limit)
    return contasrecebers


@router_contasreceber.post(
    "/",
    response_model=schemas.ContasReceber,
    dependencies=[
        Depends(
            security.has_permission("financeiro.add_contasreceber"))])
def create_contasreceber(
    *,
    db: Session = Depends(get_db),
    contasreceber_in: schemas.ContasReceberCreate,
) -> Any:
    """
    Create new contasreceber.
    """
    contasreceber = cruds.contasreceber.create(db, obj_in=contasreceber_in)
    return contasreceber


@router_contasreceber.get(
    "/{contasreceber_id}",
    response_model=schemas.ContasReceber,
    dependencies=[
        Depends(
            security.has_permission("financeiro.view_contasreceber"))])
def read_contasreceber_by_id(
    contasreceber_id: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Get a specific contasreceber by id.
    """
    contasreceber = cruds.contasreceber.get(db, id=contasreceber_id)
    if not contasreceber:
        raise HTTPException(
            status_code=404,
            detail="Esse contasreceber não existe no sistema",
        )
    return contasreceber


@router_contasreceber.put(
    "/{contasreceber_id}",
    response_model=schemas.ContasReceber,
    dependencies=[
        Depends(
            security.has_permission("financeiro.change_contasreceber"))])
def update_contasreceber(
    *,
    db: Session = Depends(get_db),
    contasreceber_id: str,
    contasreceber_in: schemas.ContasReceberUpdate
) -> Any:
    """
    Update a contasreceber.
    """
    contasreceber = cruds.contasreceber.get(db, id=contasreceber_id)
    if not contasreceber:
        raise HTTPException(
            status_code=404,
            detail="Esse contasreceber não existe no sistema",
        )
    contasreceber = cruds.contasreceber.update(
        db, db_obj=contasreceber, obj_in=contasreceber_in)
    return contasreceber


@router_contasreceber.delete(
    "/{id}",
    response_model=schemas.ContasReceber,
    dependencies=[
        Depends(
            security.has_permission("financeiro.delete_contasreceber"))])
def delete_contasreceber(
    *,
    db: Session = Depends(get_db),
    id: str
) -> Any:
    """
    Delete an note.
    """
    contasreceber = cruds.contasreceber.get(db=db, id=id)
    if not contasreceber:
        raise HTTPException(
            status_code=404,
            detail="Esse contasreceber não existe no sistema",
        )
    contasreceber = cruds.contasreceber.remove(db=db, id=id)
    return contasreceber


router.include_router(router_contasreceber)
