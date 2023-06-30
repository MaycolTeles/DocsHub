"""
Module containing the RegisterRGRequest class.
"""

from dataclasses import dataclass
from datetime import datetime

from src.domain.interfaces import ResponseModel


@dataclass
class RegisterRGRequest(ResponseModel):
    """
    Class containing the request model for the RegisterRGRequest class.
    """
    value: str
    date: datetime
