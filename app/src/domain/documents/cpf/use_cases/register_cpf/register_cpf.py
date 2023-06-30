"""
Module containing the RegisterCPF Use Case.
"""

from .register_cpf_request_model import RegisterCPFRequest
from .register_cpf_response_model import RegisterCPFResponse
from ...cpf import CPF
# from ...cpf_repository import CPFRepository
from ...exceptions import InvalidCPFException
from src.dependencies.repositories import get_repository
from src.domain.interfaces import UseCase


class RegisterCPF(UseCase):
    """
    Use Case class to register a new CPF.
    """
    # _repository: CPFRepository

    def __init__(self) -> None:
        self._repository = get_repository()

    def execute(self, request: RegisterCPFRequest) -> RegisterCPFResponse:
        """
        Method to execute the use case.
        """
        success = True
        try:
            cpf = self._create_cpf(request)

        except InvalidCPFException as error:
            # TODO> Log error
            print(error)
            success = False
            response = str(error)

            response_model = RegisterCPFResponse(
                success=success,
                response=response
            )
            return response_model

        self._save_cpf(cpf)

        response = "CPF was successfully created and registered."
        response_model = RegisterCPFResponse(
            success=success,
            response=response
        )

        return response_model

    def _create_cpf(self, request: RegisterCPFRequest) -> CPF:
        """
        TODO
        """
        value = request.value
        date = request.date

        cpf = CPF(value=value, date=date)

        return cpf

    def _save_cpf(self, cpf: CPF):
        """
        TODO: IMPLEMENT
        """
        # self._repository.create(cpf)
