"""
Module containing all "InvalidComprovanteResidenciaException" Exceptions.
"""


class InvalidComprovanteResidenciaException(Exception):
    """
    Class to represent a "ComprovanteResidenciaException" exception.
    This exceptions should be raised when a "ComprovanteResidencia" is invalid.
    """

    def __init__(self, message: str) -> None:
        """
        Constructor of the class.

        Parameters
        ----------
        message : str
            The message of the exception.
        """
        self._message = message

        super().__init__(self._message)
