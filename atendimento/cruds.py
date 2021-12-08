from atendimento.models import Agendamento, Atendimento, Avaliacao
from atendimento.schemas import (AgendamentoCreate, AgendamentoUpdate, AtendimentoCreate, AtendimentoUpdate,
                                 AvaliacaoCreate, AvaliacaoUpdate)
from core.cruds import CRUDBase


class CRUDAgendamento(CRUDBase[Agendamento, AgendamentoCreate, AgendamentoUpdate]):
    pass


agendamento = CRUDAgendamento(Agendamento)


class CRUDAtendimento(CRUDBase[Atendimento, AtendimentoCreate, AtendimentoUpdate]):
    pass


atendimento = CRUDAtendimento(Atendimento)


class CRUDAvaliacao(CRUDBase[Avaliacao, AvaliacaoCreate, AvaliacaoUpdate]):
    pass


avaliacao = CRUDAvaliacao(Avaliacao)
