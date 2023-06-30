"""
Module containing the RegisterComprovanteResidenciaTestCase Test Class.
"""

from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.domain.documents.comprovante_residencia import (
    # ComprovanteResidencia,
    ComprovanteResidenciaType,
    RegisterComprovanteResidencia,
    RegisterComprovanteResidenciaRequest,
    RegisterComprovanteResidenciaResponse,
)


class RegisterComprovanteResidenciaTestCase(TestCase):
    """
    Class to test the RegisterComprovanteResidencia class.
    """

    def setUp(self) -> None:
        """
        Method to set the test up.
        """
        self._mock_repository()

        self._use_case = RegisterComprovanteResidencia()
        self._test_value = "test_value"
        self._test_date = datetime.now()
        self._test_comprovante_type = ComprovanteResidenciaType.AGUA

    def tearDown(self) -> None:
        """
        Method to tear the test down.
        """
        self._patcher.stop()

    def _mock_repository(self) -> None:
        """TODO"""
        patcher_path = (
            "src.domain.documents.comprovante_residencia.use_cases."
            "register_comprovante_residencia.register_comprovante_residencia.get_repository"
        )
        self._patcher = patch(patcher_path)
        mock_repository_factory = self._patcher.start()
        mock_repository = mock_repository_factory.return_value = MagicMock()
        self._mock_create: MagicMock = mock_repository.create

    def test_should_register_new_comprovante_residencia_in_repository(self):
        """TODO"""
        request_model = RegisterComprovanteResidenciaRequest(
            value=self._test_value,
            date=self._test_date,
            comprovante_type=self._test_comprovante_type
        )

        actual = self._use_case.execute(request_model)
        expected = RegisterComprovanteResidenciaResponse(
            True,
            "ComprovanteResidencia was successfully created and registered."
        )

        self.assertEqual(actual, expected)
        # self._mock_create.assert_called_once()

    def test_should_not_register_comprovante_residencia_because_it_is_invalid(self):
        """TODO"""
        date_in_future = datetime.now() + timedelta(days=1)

        request_model = RegisterComprovanteResidenciaRequest(
            value=self._test_value,
            date=date_in_future,
            comprovante_type=self._test_comprovante_type
        )

        actual = self._use_case.execute(request_model)

        expected_message = (
            "Comprovante de Residência is invalid. "
            f"Date can't be newer than current date (date={date_in_future})."
        )
        expected = RegisterComprovanteResidenciaResponse(False, expected_message)

        self.assertEqual(actual, expected)
        # self._mock_create.assert_not_called()
