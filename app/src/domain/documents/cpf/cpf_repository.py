"""
TODO
"""

from abc import ABC, abstractmethod

from src.domain.documents.cpf import CPF


class CPFRepository(ABC):

    @abstractmethod
    def create(self, cpf: CPF):
        """
        TODO
        """
