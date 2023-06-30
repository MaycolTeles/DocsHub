"""
Module containing the RegisterCPFRequest class.
"""

from dataclasses import dataclass
from datetime import datetime

from src.domain.interfaces import ResponseModel


@dataclass
class RegisterCPFRequest(ResponseModel):
    """
    Class containing the request model for the RegisterCPFRequest class.
    """
    value: str
    date: datetime
