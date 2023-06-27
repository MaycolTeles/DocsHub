"""
Module containing the RegisterComprovanteResidenciaResponseModel class.
"""

from dataclasses import dataclass

from src.domain.interfaces import ResponseModel


@dataclass
class RegisterComprovanteResidenciaResponseModel(ResponseModel):
    """
    Class containing the request model for the RegisterComprovanteResidenciaUseCase class.
    """
    response: str
