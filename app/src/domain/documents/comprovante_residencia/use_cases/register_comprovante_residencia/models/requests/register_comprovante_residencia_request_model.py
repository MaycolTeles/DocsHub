"""
Module containing the RegisterComprovanteResidenciaRequestModel class.
"""

from dataclasses import dataclass
from datetime import datetime

from src.domain.documents.comprovante_residencia import ComprovanteResidenciaType
from src.domain.interfaces import ResponseModel


@dataclass
class RegisterComprovanteResidenciaRequestModel(ResponseModel):
    """
    Class containing the request model for the RegisterComprovanteResidenciaUseCase class.
    """
    value: str
    date: datetime
    comprovante_type: ComprovanteResidenciaType
