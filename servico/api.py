from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from authentication import security
from core.database import get_db
from servico import cruds, schemas

router = APIRouter()

router_categoria = APIRouter(
    prefix="/categoria", tags=["categoria"], dependencies=[Depends(security.get_current_active_user)]
)


@router_categoria.get("/", response_model=List[schemas.Categoria],
                      dependencies=[Depends(security.has_permission("servico.view_categoria"))], )
def read_categorias(db: Session = Depends(get_db), skip: int = 0, limit: int = 25) -> Any:
    """
    Retrieve categorias.
    """
    categorias = cruds.categoria.get_multi(db, skip=skip, limit=limit)
    return categorias


@router_categoria.post("/", response_model=schemas.Categoria,
                       dependencies=[Depends(security.has_permission("servico.add_categoria"))])
def create_categoria(*, db: Session = Depends(get_db), categoria_in: schemas.CategoriaCreate, ) -> Any:
    """
    Create new categoria.
    """
    categoria = cruds.categoria.create(db, obj_in=categoria_in)
    return categoria


@router_categoria.get("/{categoria_id}", response_model=schemas.Categoria,
                      dependencies=[Depends(security.has_permission("servico.view_categoria"))], )
def read_categoria_by_id(categoria_id: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a specific categoria by id.
    """
    categoria = cruds.categoria.get(db, id=categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Esse categoria não existe no sistema", )
    return categoria


@router_categoria.put("/{categoria_id}", response_model=schemas.Categoria,
                      dependencies=[Depends(security.has_permission("servico.change_categoria"))])
def update_categoria(*, db: Session = Depends(get_db), categoria_id: str, categoria_in: schemas.CategoriaUpdate) -> Any:
    """
    Update a categoria.
    """
    categoria = cruds.categoria.get(db, id=categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Esse categoria não existe no sistema")
    categoria = cruds.categoria.update(db, db_obj=categoria, obj_in=categoria_in)
    return categoria


@router_categoria.delete("/{id}", response_model=schemas.Categoria,
                         dependencies=[Depends(security.has_permission("servico.delete_categoria"))])
def delete_categoria(*, db: Session = Depends(get_db), id: str) -> Any:
    """
    Delete an note.
    """
    categoria = cruds.categoria.get(db=db, id=id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Esse categoria não existe no sistema")
    categoria = cruds.categoria.remove(db=db, id=id)
    return categoria


router.include_router(router_categoria)

router_tiposervico = APIRouter(prefix="/tiposervico", tags=["tiposervico"],
                               dependencies=[Depends(security.get_current_active_user)])


@router_tiposervico.get("/", response_model=List[schemas.TipoServico],
                        dependencies=[Depends(security.has_permission("servico.view_tiposervico"))])
def read_tiposervicos(db: Session = Depends(get_db), skip: int = 0, limit: int = 25) -> Any:
    """
    Retrieve tiposervicos.
    """
    tiposervicos = cruds.tiposervico.get_multi(db, skip=skip, limit=limit)
    return tiposervicos


@router_tiposervico.post("/", response_model=schemas.TipoServico,
                         dependencies=[Depends(security.has_permission("servico.add_tiposervico"))])
def create_tiposervico(*, db: Session = Depends(get_db), tiposervico_in: schemas.TipoServicoCreate) -> Any:
    """
    Create new tiposervico.
    """
    tiposervico = cruds.tiposervico.create(db, obj_in=tiposervico_in)
    return tiposervico


@router_tiposervico.get("/{tiposervico_id}", response_model=schemas.TipoServico,
                        dependencies=[Depends(security.has_permission("servico.view_tiposervico"))])
def read_tiposervico_by_id(tiposervico_id: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a specific tiposervico by id.
    """
    tiposervico = cruds.tiposervico.get(db, id=tiposervico_id)
    if not tiposervico:
        raise HTTPException(status_code=404, detail="Esse tiposervico não existe no sistema")
    return tiposervico


@router_tiposervico.put("/{tiposervico_id}", response_model=schemas.TipoServico,
                        dependencies=[Depends(security.has_permission("servico.change_tiposervico"))])
def update_tiposervico(*, db: Session = Depends(get_db), tiposervico_id: str,
                       tiposervico_in: schemas.TipoServicoUpdate) -> Any:
    """
    Update a tiposervico.
    """
    tiposervico = cruds.tiposervico.get(db, id=tiposervico_id)
    if not tiposervico:
        raise HTTPException(status_code=404, detail="Esse tiposervico não existe no sistema")
    tiposervico = cruds.tiposervico.update(db, db_obj=tiposervico, obj_in=tiposervico_in)
    return tiposervico


@router_tiposervico.delete("/{id}", response_model=schemas.TipoServico,
                           dependencies=[Depends(security.has_permission("servico.delete_tiposervico"))])
def delete_tiposervico(*, db: Session = Depends(get_db), id: str) -> Any:
    """
    Delete an note.
    """
    tiposervico = cruds.tiposervico.get(db=db, id=id)
    if not tiposervico:
        raise HTTPException(status_code=404, detail="Esse tiposervico não existe no sistema")
    tiposervico = cruds.tiposervico.remove(db=db, id=id)
    return tiposervico


router.include_router(router_tiposervico)

router_servico = APIRouter(prefix="/servico", tags=["servico"],
                           dependencies=[Depends(security.get_current_active_user)])


@router_servico.get("/", response_model=List[schemas.Servico],
                    dependencies=[Depends(security.has_permission("servico.view_servico"))])
def read_servicos(db: Session = Depends(get_db), skip: int = 0, limit: int = 25) -> Any:
    """
    Retrieve servicos.
    """
    servicos = cruds.servico.get_multi(db, skip=skip, limit=limit)
    return servicos


@router_servico.post("/", response_model=schemas.Servico,
                     dependencies=[Depends(security.has_permission("servico.add_servico"))])
def create_servico(*, db: Session = Depends(get_db), servico_in: schemas.ServicoCreate, ) -> Any:
    """
    Create new servico.
    """
    servico = cruds.servico.create(db, obj_in=servico_in)
    return servico


@router_servico.get("/{servico_id}", response_model=schemas.Servico,
                    dependencies=[Depends(security.has_permission("servico.view_servico"))])
def read_servico_by_id(servico_id: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a specific servico by id.
    """
    servico = cruds.servico.get(db, id=servico_id)
    if not servico:
        raise HTTPException(status_code=404, detail="Esse servico não existe no sistema")
    return servico


@router_servico.put("/{servico_id}", response_model=schemas.Servico,
                    dependencies=[Depends(security.has_permission("servico.change_servico"))])
def update_servico(*, db: Session = Depends(get_db), servico_id: str, servico_in: schemas.ServicoUpdate) -> Any:
    """
    Update a servico.
    """
    servico = cruds.servico.get(db, id=servico_id)
    if not servico:
        raise HTTPException(status_code=404, detail="Esse servico não existe no sistema")
    servico = cruds.servico.update(db, db_obj=servico, obj_in=servico_in)
    return servico


@router_servico.delete("/{id}", response_model=schemas.Servico,
                       dependencies=[Depends(security.has_permission("servico.delete_servico"))])
def delete_servico(*, db: Session = Depends(get_db), id: str) -> Any:
    """
    Delete an note.
    """
    servico = cruds.servico.get(db=db, id=id)
    if not servico:
        raise HTTPException(status_code=404, detail="Esse servico não existe no sistema")
    servico = cruds.servico.remove(db=db, id=id)
    return servico


router.include_router(router_servico)
