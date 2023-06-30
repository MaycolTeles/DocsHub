"""
Module containing the RegisterRGResponse class.
"""

from dataclasses import dataclass

from src.domain.interfaces import ResponseModel


@dataclass
class RegisterRGResponse(ResponseModel):
    """
    Class containing the request model for the RegisterRGResponse class.
    """
    success: bool
    response: str
