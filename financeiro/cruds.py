from core.cruds import CRUDBase
from financeiro.models import ContasReceber
from financeiro.schemas import ContasReceberCreate, ContasReceberUpdate


class CRUDContasReceber(CRUDBase[ContasReceber, ContasReceberCreate, ContasReceberUpdate]):
    pass


contasreceber = CRUDContasReceber(ContasReceber)
