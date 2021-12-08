from fastapi import APIRouter

from animal.api import router as router_animal
from atendimento.api import router as router_atendimento
from authentication.api import router as router_users
from financeiro.api import router as router_financeiro
from pix.api import router as router_pix
from servico.api import router as router_servico
from usuario.api import router as router_usuario
from .config import settings

"""
TODO Importar para esse arquivo os endpoints das apps do Projeto
Arquivos com os endpoints principais do projeto

- Deve ser importado nesse arquivo, os arquivo routers de todas as apps
"""

api_router = APIRouter(prefix=settings.api_str)
api_router.include_router(router_users, prefix="/authentication")
api_router.include_router(router_animal, prefix="/animal")
api_router.include_router(router_atendimento, prefix="/atendimento")
api_router.include_router(router_financeiro, prefix="/financeiro")
api_router.include_router(router_pix, prefix="/pix")
api_router.include_router(router_servico, prefix="/servico")
api_router.include_router(router_usuario, prefix="/usuario")
