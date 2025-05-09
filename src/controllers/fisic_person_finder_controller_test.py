from unittest.mock import MagicMock
import pytest
from src.controllers.fisic_person_finder_controller import FisicPersonFinderController
from src.models.sqlite.entities.fisic_person import FisicPersonTable


def test_find_person_success():
    fake_person = FisicPersonTable(
        renda_mensal=5000.0,
        idade=30,
        nome_completo="João da Silva",
        celular="11999999999",
        email="joao@email.com",
        categoria="Premium",
        saldo=15000.0
    )

    repository_mock = MagicMock()
    repository_mock.get_person.return_value = fake_person

    controller = FisicPersonFinderController(repository_mock)

    result = controller.find(1)

    assert result["data"]["type"] == "Fisic Person"
    assert result["data"]["count"] == 1
    assert result["data"]["attributes"]["renda_mensal"] == 5000.0
    assert result["data"]["attributes"]["idade"] == 30
    assert result["data"]["attributes"]["nome_completo"] == "João da Silva"
    assert result["data"]["attributes"]["celular"] == "11999999999"
    assert result["data"]["attributes"]["email"] == "joao@email.com"
    assert result["data"]["attributes"]["categoria"] == "Premium"
    assert result["data"]["attributes"]["saldo"] == 15000.0

    repository_mock.get_person.assert_called_once_with(1)


def test_find_person_not_found():
    repository_mock = MagicMock()
    repository_mock.get_person.return_value = None

    controller = FisicPersonFinderController(repository_mock)

    with pytest.raises(ValueError, match="Fisic person not found!"):
        controller.find(999)
