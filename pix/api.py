from typing import Any, List

from authentication import security
from core.database import get_db
from fastapi import APIRouter, Body, Depends, HTTPException
from pix import cruds, schemas
from sqlalchemy.orm import Session

router = APIRouter()

router_configuracaopix = APIRouter(
    prefix="/configuracaopix",
    tags=['configuracaopix'],
    dependencies=[Depends(security.get_current_active_user)]
)


@router_configuracaopix.get(
    "/",
    response_model=List[schemas.ConfiguracaoPix],
    dependencies=[Depends(security.has_permission("pix.view_configuracaopix"))]
)
def read_configuracaopixs(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 25
) -> Any:
    """
    Retrieve configuracaopixs.
    """
    configuracaopixs = cruds.configuracaopix.get_multi(
        db, skip=skip, limit=limit)
    return configuracaopixs


@router_configuracaopix.post(
    "/",
    response_model=schemas.ConfiguracaoPix,
    dependencies=[
        Depends(
            security.has_permission("pix.add_configuracaopix"))])
def create_configuracaopix(
    *,
    db: Session = Depends(get_db),
    configuracaopix_in: schemas.ConfiguracaoPixCreate,
) -> Any:
    """
    Create new configuracaopix.
    """
    configuracaopix = cruds.configuracaopix.create(
        db, obj_in=configuracaopix_in)
    return configuracaopix


@router_configuracaopix.get(
    "/{configuracaopix_id}",
    response_model=schemas.ConfiguracaoPix,
    dependencies=[
        Depends(
            security.has_permission("pix.view_configuracaopix"))])
def read_configuracaopix_by_id(
    configuracaopix_id: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Get a specific configuracaopix by id.
    """
    configuracaopix = cruds.configuracaopix.get(db, id=configuracaopix_id)
    if not configuracaopix:
        raise HTTPException(
            status_code=404,
            detail="Esse configuracaopix não existe no sistema",
        )
    return configuracaopix


@router_configuracaopix.put(
    "/{configuracaopix_id}",
    response_model=schemas.ConfiguracaoPix,
    dependencies=[
        Depends(
            security.has_permission("pix.change_configuracaopix"))])
def update_configuracaopix(
    *,
    db: Session = Depends(get_db),
    configuracaopix_id: str,
    configuracaopix_in: schemas.ConfiguracaoPixUpdate
) -> Any:
    """
    Update a configuracaopix.
    """
    configuracaopix = cruds.configuracaopix.get(db, id=configuracaopix_id)
    if not configuracaopix:
        raise HTTPException(
            status_code=404,
            detail="Esse configuracaopix não existe no sistema",
        )
    configuracaopix = cruds.configuracaopix.update(
        db, db_obj=configuracaopix, obj_in=configuracaopix_in)
    return configuracaopix


@router_configuracaopix.delete(
    "/{id}",
    response_model=schemas.ConfiguracaoPix,
    dependencies=[
        Depends(
            security.has_permission("pix.delete_configuracaopix"))])
def delete_configuracaopix(
    *,
    db: Session = Depends(get_db),
    id: str
) -> Any:
    """
    Delete an note.
    """
    configuracaopix = cruds.configuracaopix.get(db=db, id=id)
    if not configuracaopix:
        raise HTTPException(
            status_code=404,
            detail="Esse configuracaopix não existe no sistema",
        )
    configuracaopix = cruds.configuracaopix.remove(db=db, id=id)
    return configuracaopix


router.include_router(router_configuracaopix)


router_pagamentopix = APIRouter(
    prefix="/pagamentopix",
    tags=['pagamentopix'],
    dependencies=[Depends(security.get_current_active_user)]
)


@router_pagamentopix.get(
    "/",
    response_model=List[schemas.PagamentoPix],
    dependencies=[Depends(security.has_permission("pix.view_pagamentopix"))]
)
def read_pagamentopixs(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 25
) -> Any:
    """
    Retrieve pagamentopixs.
    """
    pagamentopixs = cruds.pagamentopix.get_multi(db, skip=skip, limit=limit)
    return pagamentopixs


@router_pagamentopix.post("/", response_model=schemas.PagamentoPix,
                          dependencies=[Depends(security.has_permission("pix.add_pagamentopix"))])
def create_pagamentopix(
    *,
    db: Session = Depends(get_db),
    pagamentopix_in: schemas.PagamentoPixCreate,
) -> Any:
    """
    Create new pagamentopix.
    """
    pagamentopix = cruds.pagamentopix.create(db, obj_in=pagamentopix_in)
    return pagamentopix


@router_pagamentopix.get(
    "/{pagamentopix_id}",
    response_model=schemas.PagamentoPix,
    dependencies=[
        Depends(
            security.has_permission("pix.view_pagamentopix"))])
def read_pagamentopix_by_id(
    pagamentopix_id: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Get a specific pagamentopix by id.
    """
    pagamentopix = cruds.pagamentopix.get(db, id=pagamentopix_id)
    if not pagamentopix:
        raise HTTPException(
            status_code=404,
            detail="Esse pagamentopix não existe no sistema",
        )
    return pagamentopix


@router_pagamentopix.put(
    "/{pagamentopix_id}",
    response_model=schemas.PagamentoPix,
    dependencies=[
        Depends(
            security.has_permission("pix.change_pagamentopix"))])
def update_pagamentopix(
    *,
    db: Session = Depends(get_db),
    pagamentopix_id: str,
    pagamentopix_in: schemas.PagamentoPixUpdate
) -> Any:
    """
    Update a pagamentopix.
    """
    pagamentopix = cruds.pagamentopix.get(db, id=pagamentopix_id)
    if not pagamentopix:
        raise HTTPException(
            status_code=404,
            detail="Esse pagamentopix não existe no sistema",
        )
    pagamentopix = cruds.pagamentopix.update(
        db, db_obj=pagamentopix, obj_in=pagamentopix_in)
    return pagamentopix


@router_pagamentopix.delete(
    "/{id}",
    response_model=schemas.PagamentoPix,
    dependencies=[
        Depends(
            security.has_permission("pix.delete_pagamentopix"))])
def delete_pagamentopix(
    *,
    db: Session = Depends(get_db),
    id: str
) -> Any:
    """
    Delete an note.
    """
    pagamentopix = cruds.pagamentopix.get(db=db, id=id)
    if not pagamentopix:
        raise HTTPException(
            status_code=404,
            detail="Esse pagamentopix não existe no sistema",
        )
    pagamentopix = cruds.pagamentopix.remove(db=db, id=id)
    return pagamentopix


router.include_router(router_pagamentopix)
