from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from animal import cruds, schemas
from authentication import security
from core.database import get_db

router = APIRouter()

router_especie = APIRouter(prefix="/especie", tags=["especie"],
                           dependencies=[Depends(security.get_current_active_user)])


@router_especie.get("/", response_model=List[schemas.Especie],
                    dependencies=[Depends(security.has_permission("animal.view_especie"))])
def read_especies(db: Session = Depends(get_db), skip: int = 0, limit: int = 25) -> Any:
    """
    Retrieve especies.
    """
    especies = cruds.especie.get_multi(db, skip=skip, limit=limit)
    return especies


@router_especie.post("/", response_model=schemas.Especie,
                     dependencies=[Depends(security.has_permission("animal.add_especie"))])
def create_especie(*, db: Session = Depends(get_db), especie_in: schemas.EspecieCreate) -> Any:
    """
    Create new especie.
    """
    especie = cruds.especie.create(db, obj_in=especie_in)
    return especie


@router_especie.get("/{especie_id}", response_model=schemas.Especie,
                    dependencies=[Depends(security.has_permission("animal.view_especie"))])
def read_especie_by_id(especie_id: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a specific especie by id.
    """
    especie = cruds.especie.get(db, id=especie_id)
    if not especie:
        raise HTTPException(status_code=404, detail="Esse especie não existe no sistema")
    return especie


@router_especie.put("/{especie_id}", response_model=schemas.Especie,
                    dependencies=[Depends(security.has_permission("animal.change_especie"))])
def update_especie(*, db: Session = Depends(get_db), especie_id: str, especie_in: schemas.EspecieUpdate) -> Any:
    """
    Update a especie.
    """
    especie = cruds.especie.get(db, id=especie_id)
    if not especie:
        raise HTTPException(status_code=404,detail="Esse especie não existe no sistema")
    especie = cruds.especie.update(db, db_obj=especie, obj_in=especie_in)
    return especie


@router_especie.delete("/{id}", response_model=schemas.Especie,
                       dependencies=[Depends(security.has_permission("animal.delete_especie"))])
def delete_especie(*, db: Session = Depends(get_db), id: str) -> Any:
    """
    Delete an note.
    """
    especie = cruds.especie.get(db=db, id=id)
    if not especie:
        raise HTTPException(status_code=404, detail="Esse especie não existe no sistema")
    especie = cruds.especie.remove(db=db, id=id)
    return especie


router.include_router(router_especie)

router_animal = APIRouter(prefix="/animal", tags=["animal"], dependencies=[Depends(security.get_current_active_user)])


@router_animal.get("/", response_model=List[schemas.Animal],
                   dependencies=[Depends(security.has_permission("animal.view_animal"))])
def read_animals(db: Session = Depends(get_db), skip: int = 0, limit: int = 25) -> Any:
    """
    Retrieve animals.
    """
    animals = cruds.animal.get_multi(db, skip=skip, limit=limit)
    return animals


@router_animal.post("/", response_model=schemas.Animal,
                    dependencies=[Depends(security.has_permission("animal.add_animal"))])
def create_animal(*, db: Session = Depends(get_db), animal_in: schemas.AnimalCreate) -> Any:
    """
    Create new animal.
    """
    animal = cruds.animal.create(db, obj_in=animal_in)
    return animal


@router_animal.get("/{animal_id}", response_model=schemas.Animal,
                   dependencies=[Depends(security.has_permission("animal.view_animal"))])
def read_animal_by_id(animal_id: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a specific animal by id.
    """
    animal = cruds.animal.get(db, id=animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Esse animal não existe no sistema")
    return animal


@router_animal.put("/{animal_id}", response_model=schemas.Animal,
                   dependencies=[Depends(security.has_permission("animal.change_animal"))])
def update_animal(*, db: Session = Depends(get_db), animal_id: str, animal_in: schemas.AnimalUpdate) -> Any:
    """
    Update a animal.
    """
    animal = cruds.animal.get(db, id=animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Esse animal não existe no sistema")
    animal = cruds.animal.update(db, db_obj=animal, obj_in=animal_in)
    return animal


@router_animal.delete("/{id}", response_model=schemas.Animal,
                      dependencies=[Depends(security.has_permission("animal.delete_animal"))])
def delete_animal(*, db: Session = Depends(get_db), id: str) -> Any:
    """
    Delete an note.
    """
    animal = cruds.animal.get(db=db, id=id)
    if not animal:
        raise HTTPException(status_code=404, detail="Esse animal não existe no sistema")
    animal = cruds.animal.remove(db=db, id=id)
    return animal


router.include_router(router_animal)
