"""
__init__ file to export the classes below.
"""

from .register_comprovante_residencia import RegisterComprovanteResidencia
from .register_comprovante_residencia_request import RegisterComprovanteResidenciaRequest
from .register_comprovante_residencia_response import RegisterComprovanteResidenciaResponse


__all__ = [
    "RegisterComprovanteResidencia",
    "RegisterComprovanteResidenciaRequest",
    "RegisterComprovanteResidenciaResponse"
]
