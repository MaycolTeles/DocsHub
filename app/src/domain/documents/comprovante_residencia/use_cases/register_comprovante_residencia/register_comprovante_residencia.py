"""
Module containing the RegisterComprovanteResidencia Use Case.
"""

from .register_comprovante_residencia_request import RegisterComprovanteResidenciaRequest
from .register_comprovante_residencia_response import RegisterComprovanteResidenciaResponse
from ...comprovante_residencia import ComprovanteResidencia
# from ...comprovante_residencia_repository import ComprovanteResidenciaRepository
from ...exceptions import InvalidComprovanteResidenciaException
from src.dependencies.repositories import get_repository
from src.domain.interfaces import UseCase


class RegisterComprovanteResidencia(UseCase):
    """
    Use Case class to register a new ComprovanteResidencia.
    """
    # _repository: ComprovanteResidenciaRepository

    def __init__(self):
        """TODO"""
        self._repository = get_repository()

    def execute(
        self,
        request: RegisterComprovanteResidenciaRequest
    ) -> RegisterComprovanteResidenciaResponse:
        """
        Method to execute the use case.
        """
        success = True
        try:
            comprovante_residencia = self._create_comprovante_residencia(request)

        except InvalidComprovanteResidenciaException as error:
            # TODO> Log error
            print(error)
            success = False
            response = str(error)

            response_model = RegisterComprovanteResidenciaResponse(
                success=success,
                response=response
            )
            return response_model

        self._save_comprovante_residencia_in_repository(comprovante_residencia)

        response = "ComprovanteResidencia was successfully created and registered."
        response_model = RegisterComprovanteResidenciaResponse(
            success=success,
            response=response
        )

        return response_model

    def _create_comprovante_residencia(
        self,
        request: RegisterComprovanteResidenciaRequest
    ) -> ComprovanteResidencia:
        """
        TODO
        """
        value = request.value
        date = request.date
        comprovante_type = request.comprovante_type

        comprovante_residencia = ComprovanteResidencia(
            value=value,
            date=date,
            comprovante_type=comprovante_type
        )

        return comprovante_residencia

    def _save_comprovante_residencia_in_repository(self, comprovante_residencia: ComprovanteResidencia):
        """
        TODO: IMPLEMENT
        """
        # self._repository.create(comprovante_residencia)
