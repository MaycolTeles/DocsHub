"""
Module containing the RegisterRG Use Case.
"""

from .register_rg_request import RegisterRGRequest
from .register_rg_response import RegisterRGResponse
from ...rg import RG
# from ...rg_repository import RGRepository
from ...exceptions import InvalidRGException
from src.dependencies.repositories import get_repository
from src.domain.interfaces import UseCase


class RegisterRG(UseCase):
    """
    Use Case class to register a new RG.
    """
    # _repository: RGRepository

    def __init__(self) -> None:
        self._repository = get_repository()

    def execute(self, request: RegisterRGRequest) -> RegisterRGResponse:
        """
        Method to execute the use case.
        """
        success = True
        try:
            rg = self._create_rg(request)

        except InvalidRGException as error:
            # TODO> Log error
            print(error)
            success = False
            response = str(error)

            response_model = RegisterRGResponse(
                success=success,
                response=response
            )
            return response_model

        self._save_rg(rg)

        response = "RG was successfully created and registered."
        response_model = RegisterRGResponse(
            success=success,
            response=response
        )

        return response_model

    def _create_rg(self, request: RegisterRGRequest) -> RG:
        """
        TODO
        """
        value = request.value
        date = request.date

        rg = RG(value=value, date=date)

        return rg

    def _save_rg(self, rg: RG):
        """
        TODO: IMPLEMENT
        """
        # self._repository.create(rg)
