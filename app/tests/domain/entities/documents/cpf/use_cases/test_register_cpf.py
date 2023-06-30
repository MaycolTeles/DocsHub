"""
Module containing the RegisterCPFTestCase Test Class.
"""

from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.domain.documents.cpf import (
    # CPF,
    RegisterCPF,
    RegisterCPFRequest,
    RegisterCPFResponse
)


class RegisterCPFTestCase(TestCase):
    """
    Class to test the RegisterCPF class.
    """

    def setUp(self) -> None:
        """
        Method to set the test up.
        """
        self._mock_repository()

        self._use_case = RegisterCPF()
        self._test_value = "11144477735"
        self._test_date = datetime.now()

    def tearDown(self) -> None:
        """
        Method to tear the test down.
        """
        self._patcher.stop()

    def _mock_repository(self) -> None:
        """TODO"""
        patcher_path = (
            "src.domain.documents.cpf.use_cases."
            "register_cpf.register_cpf.get_repository"
        )
        self._patcher = patch(patcher_path)
        mock_repository_factory = self._patcher.start()
        mock_repository = mock_repository_factory.return_value = MagicMock()
        self._mock_create: MagicMock = mock_repository.create

    def test_should_register_new_cpf_in_repository(self):
        """TODO"""
        request = RegisterCPFRequest(
            value=self._test_value,
            date=self._test_date,
        )

        actual = self._use_case.execute(request)
        expected = RegisterCPFResponse(True, "CPF was successfully created and registered.")

        self.assertEqual(actual, expected)
        # self._mock_create.assert_called_once()

    def test_should_not_register_cpf_because_it_is_invalid(self):
        """TODO"""
        date_in_future = datetime.now() + timedelta(days=1)

        request = RegisterCPFRequest(
            value=self._test_value,
            date=date_in_future,
        )

        actual = self._use_case.execute(request)

        expected_message = f"CPF is invalid. Date can't be newer than current date (date={date_in_future})."
        expected = RegisterCPFResponse(False, expected_message)

        self.assertEqual(actual, expected)
        # self._mock_create.assert_not_called()
