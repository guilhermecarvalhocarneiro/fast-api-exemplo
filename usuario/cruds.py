from core.cruds import CRUDBase
from usuario.models import (Cliente, Profissao, Profissional, ProfissionalServico, Usuario)
from usuario.schemas import (ClienteCreate, ClienteUpdate, ProfissaoCreate, ProfissaoUpdate, ProfissionalCreate,
                             ProfissionalServicoCreate, ProfissionalServicoUpdate, ProfissionalUpdate, UsuarioCreate,
                             UsuarioUpdate)


class CRUDUsuario(CRUDBase[Usuario, UsuarioCreate, UsuarioUpdate]):
    pass


usuario = CRUDUsuario(Usuario)


class CRUDCliente(CRUDBase[Cliente, ClienteCreate, ClienteUpdate]):
    pass


cliente = CRUDCliente(Cliente)


class CRUDProfissao(CRUDBase[Profissao, ProfissaoCreate, ProfissaoUpdate]):
    pass


profissao = CRUDProfissao(Profissao)


class CRUDProfissional(CRUDBase[Profissional, ProfissionalCreate, ProfissionalUpdate]):
    pass


profissional = CRUDProfissional(Profissional)


class CRUDProfissionalServico(CRUDBase[ProfissionalServico, ProfissionalServicoCreate, ProfissionalServicoUpdate]):
    pass


profissionalservico = CRUDProfissionalServico(ProfissionalServico)
