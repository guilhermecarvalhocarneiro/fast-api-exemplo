from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from authentication import security
from core.database import get_db
from usuario import cruds, schemas

router = APIRouter()

router_usuario = APIRouter(
    prefix="/usuario", tags=["usuario"], dependencies=[Depends(security.get_current_active_user)]
)


@router_usuario.get(
    "/", response_model=List[schemas.Usuario], dependencies=[Depends(security.has_permission("usuario.view_usuario"))]
)
def read_usuarios(db: Session = Depends(get_db), skip: int = 0, limit: int = 25) -> Any:
    """
    Retrieve usuarios.
    """
    usuarios = cruds.usuario.get_multi(db, skip=skip, limit=limit)
    return usuarios


@router_usuario.post(
    "/", response_model=schemas.Usuario, dependencies=[Depends(security.has_permission("usuario.add_usuario"))]
)
def create_usuario(*, db: Session = Depends(get_db), usuario_in: schemas.UsuarioCreate) -> Any:
    """
    Create new usuario.
    """
    usuario = cruds.usuario.create(db, obj_in=usuario_in)
    return usuario


@router_usuario.get("/{usuario_id}", response_model=schemas.Usuario,
                    dependencies=[Depends(security.has_permission("usuario.view_usuario"))])
def read_usuario_by_id(usuario_id: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a specific usuario by id.
    """
    usuario = cruds.usuario.get(db, id=usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Esse usuario não existe no sistema")
    return usuario


@router_usuario.put(
    "/{usuario_id}",
    response_model=schemas.Usuario,
    dependencies=[Depends(security.has_permission("usuario.change_usuario"))],
)
def update_usuario(*, db: Session = Depends(get_db), usuario_id: str, usuario_in: schemas.UsuarioUpdate) -> Any:
    """
    Update a usuario.
    """
    usuario = cruds.usuario.get(db, id=usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Esse usuario não existe no sistema")
    usuario = cruds.usuario.update(db, db_obj=usuario, obj_in=usuario_in)
    return usuario


@router_usuario.delete(
    "/{id}", response_model=schemas.Usuario, dependencies=[Depends(security.has_permission("usuario.delete_usuario"))]
)
def delete_usuario(*, db: Session = Depends(get_db), id: str) -> Any:
    """
    Delete an note.
    """
    usuario = cruds.usuario.get(db=db, id=id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Esse usuario não existe no sistema")
    usuario = cruds.usuario.remove(db=db, id=id)
    return usuario


router.include_router(router_usuario)

router_cliente = APIRouter(
    prefix="/cliente", tags=["cliente"], dependencies=[Depends(security.get_current_active_user)]
)


@router_cliente.get(
    "/", response_model=List[schemas.Cliente], dependencies=[Depends(security.has_permission("usuario.view_cliente"))]
)
def read_clientes(db: Session = Depends(get_db), skip: int = 0, limit: int = 25) -> Any:
    """
    Retrieve clientes.
    """
    clientes = cruds.cliente.get_multi(db, skip=skip, limit=limit)
    return clientes


@router_cliente.post(
    "/", response_model=schemas.Cliente, dependencies=[Depends(security.has_permission("usuario.add_cliente"))]
)
def create_cliente(*, db: Session = Depends(get_db), cliente_in: schemas.ClienteCreate) -> Any:
    """
    Create new cliente.
    """
    cliente = cruds.cliente.create(db, obj_in=cliente_in)
    return cliente


@router_cliente.get("/{cliente_id}", response_model=schemas.Cliente,
                    dependencies=[Depends(security.has_permission("usuario.view_cliente"))])
def read_cliente_by_id(cliente_id: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a specific cliente by id.
    """
    cliente = cruds.cliente.get(db, id=cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Esse cliente não existe no sistema")
    return cliente


@router_cliente.put(
    "/{cliente_id}",
    response_model=schemas.Cliente,
    dependencies=[Depends(security.has_permission("usuario.change_cliente"))],
)
def update_cliente(*, db: Session = Depends(get_db), cliente_id: str, cliente_in: schemas.ClienteUpdate) -> Any:
    """
    Update a cliente.
    """
    cliente = cruds.cliente.get(db, id=cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Esse cliente não existe no sistema")
    cliente = cruds.cliente.update(db, db_obj=cliente, obj_in=cliente_in)
    return cliente


@router_cliente.delete("/{id}", response_model=schemas.Cliente,
                       dependencies=[Depends(security.has_permission("usuario.delete_cliente"))])
def delete_cliente(*, db: Session = Depends(get_db), id: str) -> Any:
    """
    Delete an note.
    """
    cliente = cruds.cliente.get(db=db, id=id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Esse cliente não existe no sistema")
    cliente = cruds.cliente.remove(db=db, id=id)
    return cliente


router.include_router(router_cliente)

router_profissao = APIRouter(prefix="/profissao", tags=["profissao"],
                             dependencies=[Depends(security.get_current_active_user)])


@router_profissao.get("/", response_model=List[schemas.Profissao],
                      dependencies=[Depends(security.has_permission("usuario.view_profissao"))])
def read_profissaos(db: Session = Depends(get_db), skip: int = 0, limit: int = 25) -> Any:
    """
    Retrieve profissaos.
    """
    profissaos = cruds.profissao.get_multi(db, skip=skip, limit=limit)
    return profissaos


@router_profissao.post("/", response_model=schemas.Profissao,
                       dependencies=[Depends(security.has_permission("usuario.add_profissao"))])
def create_profissao(*, db: Session = Depends(get_db), profissao_in: schemas.ProfissaoCreate) -> Any:
    """
    Create new profissao.
    """
    profissao = cruds.profissao.create(db, obj_in=profissao_in)
    return profissao


@router_profissao.get("/{profissao_id}", response_model=schemas.Profissao,
                      dependencies=[Depends(security.has_permission("usuario.view_profissao"))])
def read_profissao_by_id(profissao_id: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a specific profissao by id.
    """
    profissao = cruds.profissao.get(db, id=profissao_id)
    if not profissao:
        raise HTTPException(status_code=404, detail="Esse profissao não existe no sistema")
    return profissao


@router_profissao.put("/{profissao_id}", response_model=schemas.Profissao,
                      dependencies=[Depends(security.has_permission("usuario.change_profissao"))])
def update_profissao(*, db: Session = Depends(get_db), profissao_id: str, profissao_in: schemas.ProfissaoUpdate) -> Any:
    """
    Update a profissao.
    """
    profissao = cruds.profissao.get(db, id=profissao_id)
    if not profissao:
        raise HTTPException(status_code=404, detail="Esse profissao não existe no sistema")
    profissao = cruds.profissao.update(db, db_obj=profissao, obj_in=profissao_in)
    return profissao


@router_profissao.delete("/{id}", response_model=schemas.Profissao,
                         dependencies=[Depends(security.has_permission("usuario.delete_profissao"))])
def delete_profissao(*, db: Session = Depends(get_db), id: str) -> Any:
    """
    Delete an note.
    """
    profissao = cruds.profissao.get(db=db, id=id)
    if not profissao:
        raise HTTPException(status_code=404, detail="Esse profissao não existe no sistema")
    profissao = cruds.profissao.remove(db=db, id=id)
    return profissao


router.include_router(router_profissao)

router_profissional = APIRouter(prefix="/profissional", tags=["profissional"],
                                dependencies=[Depends(security.get_current_active_user)])


@router_profissional.get("/", response_model=List[schemas.Profissional],
                         dependencies=[Depends(security.has_permission("usuario.view_profissional"))])
def read_profissionals(db: Session = Depends(get_db), skip: int = 0, limit: int = 25) -> Any:
    """
    Retrieve profissionals.
    """
    profissionals = cruds.profissional.get_multi(db, skip=skip, limit=limit)
    return profissionals


@router_profissional.post("/", response_model=schemas.Profissional,
                          dependencies=[Depends(security.has_permission("usuario.add_profissional"))])
def create_profissional(*, db: Session = Depends(get_db), profissional_in: schemas.ProfissionalCreate) -> Any:
    """
    Create new profissional.
    """
    profissional = cruds.profissional.create(db, obj_in=profissional_in)
    return profissional


@router_profissional.get("/{profissional_id}", response_model=schemas.Profissional,
                         dependencies=[Depends(security.has_permission("usuario.view_profissional"))])
def read_profissional_by_id(profissional_id: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a specific profissional by id.
    """
    profissional = cruds.profissional.get(db, id=profissional_id)
    if not profissional:
        raise HTTPException(status_code=404, detail="Esse profissional não existe no sistema")
    return profissional


@router_profissional.put("/{profissional_id}", response_model=schemas.Profissional,
                         dependencies=[Depends(security.has_permission("usuario.change_profissional"))])
def update_profissional(*, db: Session = Depends(get_db), profissional_id: str,
                        profissional_in: schemas.ProfissionalUpdate) -> Any:
    """
    Update a profissional.
    """
    profissional = cruds.profissional.get(db, id=profissional_id)
    if not profissional:
        raise HTTPException(status_code=404, detail="Esse profissional não existe no sistema")
    profissional = cruds.profissional.update(db, db_obj=profissional, obj_in=profissional_in)
    return profissional


@router_profissional.delete("/{id}", response_model=schemas.Profissional,
                            dependencies=[Depends(security.has_permission("usuario.delete_profissional"))])
def delete_profissional(*, db: Session = Depends(get_db), id: str) -> Any:
    """
    Delete an note.
    """
    profissional = cruds.profissional.get(db=db, id=id)
    if not profissional:
        raise HTTPException(status_code=404, detail="Esse profissional não existe no sistema")
    profissional = cruds.profissional.remove(db=db, id=id)
    return profissional


router.include_router(router_profissional)

router_profissionalservico = APIRouter(prefix="/profissionalservico", tags=["profissionalservico"],
                                       dependencies=[Depends(security.get_current_active_user)])


@router_profissionalservico.get("/", response_model=List[schemas.ProfissionalServico],
                                dependencies=[Depends(security.has_permission("usuario.view_profissionalservico"))])
def read_profissionalservicos(db: Session = Depends(get_db), skip: int = 0, limit: int = 25) -> Any:
    """
    Retrieve profissionalservicos.
    """
    profissionalservicos = cruds.profissionalservico.get_multi(db, skip=skip, limit=limit)
    return profissionalservicos


@router_profissionalservico.post("/", response_model=schemas.ProfissionalServico,
                                 dependencies=[Depends(security.has_permission("usuario.add_profissionalservico"))])
def create_profissionalservico(*, db: Session = Depends(get_db),
                               profissionalservico_in: schemas.ProfissionalServicoCreate) -> Any:
    """
    Create new profissionalservico.
    """
    profissionalservico = cruds.profissionalservico.create(db, obj_in=profissionalservico_in)
    return profissionalservico


@router_profissionalservico.get("/{profissionalservico_id}", response_model=schemas.ProfissionalServico,
                                dependencies=[Depends(security.has_permission("usuario.view_profissionalservico"))])
def read_profissionalservico_by_id(profissionalservico_id: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a specific profissionalservico by id.
    """
    profissionalservico = cruds.profissionalservico.get(db, id=profissionalservico_id)
    if not profissionalservico:
        raise HTTPException(status_code=404, detail="Esse profissionalservico não existe no sistema")
    return profissionalservico


@router_profissionalservico.put("/{profissionalservico_id}", response_model=schemas.ProfissionalServico,
                                dependencies=[Depends(security.has_permission("usuario.change_profissionalservico"))])
def update_profissionalservico(*, db: Session = Depends(get_db), profissionalservico_id: str,
                               profissionalservico_in: schemas.ProfissionalServicoUpdate) -> Any:
    """
    Update a profissionalservico.
    """
    profissionalservico = cruds.profissionalservico.get(db, id=profissionalservico_id)
    if not profissionalservico:
        raise HTTPException(status_code=404, detail="Esse profissionalservico não existe no sistema")
    profissionalservico = cruds.profissionalservico.update(db, db_obj=profissionalservico,
                                                           obj_in=profissionalservico_in)
    return profissionalservico


@router_profissionalservico.delete("/{id}", response_model=schemas.ProfissionalServico,
                                   dependencies=[
                                       Depends(security.has_permission("usuario.delete_profissionalservico"))])
def delete_profissionalservico(*, db: Session = Depends(get_db), id: str) -> Any:
    """
    Delete an note.
    """
    profissionalservico = cruds.profissionalservico.get(db=db, id=id)
    if not profissionalservico:
        raise HTTPException(status_code=404, detail="Esse profissionalservico não existe no sistema")
    profissionalservico = cruds.profissionalservico.remove(db=db, id=id)
    return profissionalservico


router.include_router(router_profissionalservico)
