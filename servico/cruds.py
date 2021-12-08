from core.cruds import CRUDBase
from servico.models import Categoria, Servico, TipoServico
from servico.schemas import (CategoriaCreate, CategoriaUpdate, ServicoCreate, ServicoUpdate, TipoServicoCreate,
                             TipoServicoUpdate)


class CRUDCategoria(CRUDBase[Categoria, CategoriaCreate, CategoriaUpdate]):
    pass


categoria = CRUDCategoria(Categoria)


class CRUDTipoServico(CRUDBase[TipoServico, TipoServicoCreate, TipoServicoUpdate]):
    pass


tiposervico = CRUDTipoServico(TipoServico)


class CRUDServico(CRUDBase[Servico, ServicoCreate, ServicoUpdate]):
    pass


servico = CRUDServico(Servico)
