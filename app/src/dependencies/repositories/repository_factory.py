"""
TODO
"""

from src.application.infra.repositories import InMemoRepository


REPOSITORY = InMemoRepository()


def get_repository():
    """
    Function to get the repository.
    """
    return REPOSITORY
