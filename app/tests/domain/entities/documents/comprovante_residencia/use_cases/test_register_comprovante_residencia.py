"""
Module containing the RegisterComprovanteResidenciaUseCaseTestCase Test Class.
"""

from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.domain.documents.comprovante_residencia import (
    RegisterComprovanteResidenciaUseCase,
    RegisterComprovanteResidenciaRequestModel,
    RegisterComprovanteResidenciaResponseModel,
    ComprovanteResidenciaType
)


@patch(
    "src.domain.documents.comprovante_residencia.use_cases.register_comprovante_residencia."
    "register_comprovante_residencia.ComprovanteResidencia"
)
class RegisterComprovanteResidenciaUseCaseTestCase(TestCase):
    """
    Class to test the RegisterComprovanteResidencia class.
    """

    def test_should_register_new_comprovante_residencia(self, mock_comprovante_residencia: MagicMock):
        """
        Method to assert the RegisterComprovanteResidenciaUseCase class is correctly created
        since it has valid parameters.
        """
        use_case = RegisterComprovanteResidenciaUseCase()

        test_value = "test_value"
        test_date = datetime.now()
        test_comprovante_type = ComprovanteResidenciaType.AGUA

        request_model = RegisterComprovanteResidenciaRequestModel(
            value=test_value,
            date=test_date,
            comprovante_type=test_comprovante_type
        )

        actual = use_case.execute(request_model)
        expected = RegisterComprovanteResidenciaResponseModel("test_response")

        mock_comprovante_residencia.assert_called_once_with(
            value=test_value,
            date=test_date,
            comprovante_type=test_comprovante_type
        )
        self.assertEqual(actual, expected)
