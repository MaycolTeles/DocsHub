"""
Module containing the RegisterComprovanteResidenciaUseCase Use Case.
"""

from ...comprovante_residencia import ComprovanteResidencia
from .models import (
    RegisterComprovanteResidenciaRequestModel,
    RegisterComprovanteResidenciaResponseModel
)
from src.domain.interfaces import UseCase


class RegisterComprovanteResidenciaUseCase(UseCase):
    """
    Use Case class to register a new ComprovanteResidencia.
    """

    def execute(
        self,
        request: RegisterComprovanteResidenciaRequestModel
    ) -> RegisterComprovanteResidenciaResponseModel:
        """
        Method to execute the use case.
        """
        value = request.value
        date = request.date
        comprovante_type = request.comprovante_type

        _ = ComprovanteResidencia(
            value=value,
            date=date,
            comprovante_type=comprovante_type
        )

        return RegisterComprovanteResidenciaResponseModel("test_response")
