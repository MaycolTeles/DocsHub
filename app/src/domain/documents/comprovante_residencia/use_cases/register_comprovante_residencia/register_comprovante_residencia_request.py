"""
Module containing the RegisterComprovanteResidenciaRequest class.
"""

from dataclasses import dataclass
from datetime import datetime

from src.domain.documents.comprovante_residencia import ComprovanteResidenciaType
from src.domain.interfaces import ResponseModel


@dataclass
class RegisterComprovanteResidenciaRequest(ResponseModel):
    """
    Class containing the request model for the RegisterComprovanteResidenciaUseCase class.
    """
    value: str
    date: datetime
    comprovante_type: ComprovanteResidenciaType
