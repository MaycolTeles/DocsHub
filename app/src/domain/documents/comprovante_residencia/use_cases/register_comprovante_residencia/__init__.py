"""
__init__ file to export the classes below.
"""

from .register_comprovante_residencia import RegisterComprovanteResidenciaUseCase
from .models import RegisterComprovanteResidenciaRequestModel, RegisterComprovanteResidenciaResponseModel


__all__ = [
    "RegisterComprovanteResidenciaUseCase",
    "RegisterComprovanteResidenciaRequestModel",
    "RegisterComprovanteResidenciaResponseModel"
]
