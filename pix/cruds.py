from core.cruds import CRUDBase
from pix.models import ConfiguracaoPix, PagamentoPix
from pix.schemas import (ConfiguracaoPixCreate, ConfiguracaoPixUpdate,
                         PagamentoPixCreate, PagamentoPixUpdate)


class CRUDConfiguracaoPix(
        CRUDBase[ConfiguracaoPix, ConfiguracaoPixCreate, ConfiguracaoPixUpdate]):
    pass


configuracaopix = CRUDConfiguracaoPix(ConfiguracaoPix)


class CRUDPagamentoPix(
        CRUDBase[PagamentoPix, PagamentoPixCreate, PagamentoPixUpdate]):
    pass


pagamentopix = CRUDPagamentoPix(PagamentoPix)
