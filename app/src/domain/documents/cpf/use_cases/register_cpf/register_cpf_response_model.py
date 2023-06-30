"""
Module containing the RegisterCPFResponse class.
"""

from dataclasses import dataclass

from src.domain.interfaces import ResponseModel


@dataclass
class RegisterCPFResponse(ResponseModel):
    """
    Class containing the request model for the RegisterCPFResponse class.
    """
    success: bool
    response: str
