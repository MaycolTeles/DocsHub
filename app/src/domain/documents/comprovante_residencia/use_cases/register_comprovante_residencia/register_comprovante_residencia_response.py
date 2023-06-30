"""
Module containing the RegisterComprovanteResidenciaResponse class.
"""

from dataclasses import dataclass

from src.domain.interfaces import ResponseModel


@dataclass
class RegisterComprovanteResidenciaResponse(ResponseModel):
    """
    Class containing the request model for the RegisterComprovanteResidenciaUseCase class.
    """
    success: bool
    response: str
