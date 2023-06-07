"""
Module containing the "RG" class.
"""

from typing import Optional
from datetime import datetime

from .exceptions import InvalidRGException
from ..cpf import CPF
from ..document import Document


class RG(Document):
    """
    Class to represent a RG.
    """
    _rg_value: str
    _cpf: Optional[CPF]

    def __init__(self, value: str, date: datetime, cpf: Optional[CPF] = None) -> None:
        """
        Constructor of the class.

        Parameters
        ----------
        value : str
            The value of the RG.

        date : datetime
            The date of the RG.

        cpf : Optional[CPF]
            The CPF of the RG, by default None
        """
        self._rg_value = value
        self._cpf = cpf

        super().__init__(date)

    def get_cpf(self) -> Optional[CPF]:
        """
        Public Method to get the CPF.
        """
        return self._cpf

    def _validate_document(self) -> None:
        """
        Protected method to validate the document by raising an exception if it's not valid.
        """
        self._validate_rg()

    def _validate_rg(self) -> None:
        """
        Private method to validate the RG.
        """
        self._validate_date()

    def _validate_date(self) -> None:
        """
        Private Method to validate the RG date by raising an InvalidRGException exception
        if its date is not valid.
        """
        current_date = datetime.now()

        if self._date <= current_date:
            return

        invalid_date_message = f"RG is invalid. The date {self._date} must be in the past."
        raise InvalidRGException(invalid_date_message)
