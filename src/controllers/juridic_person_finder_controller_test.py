from unittest.mock import MagicMock
import pytest
from src.controllers.juridic_person_finder_controller import JuridicPersonFinderController
from src.models.sqlite.entities.juridic_person import JuridicPersonTable


def test_find_person_success():
    fake_person = JuridicPersonTable(
        faturamento=15000.0,
        idade=30,
        nome_fantasia="Adalberto",
        celular="11009900990",
        email_corporativo="Adalberto11@mail.com",
        categoria="Premium",
        saldo=22000.0
    )

    repository_mock = MagicMock()
    repository_mock.get_person.return_value = fake_person

    controller = JuridicPersonFinderController(repository_mock)

    result = controller.find(1)

    assert result["data"]["type"] == "Juridic Person"
    assert result["data"]["count"] == 1
    assert result["data"]["attributes"]["faturamento"] == 15000.0
    assert result["data"]["attributes"]["idade"] == 30
    assert result["data"]["attributes"]["nome_fantasia"] == "Adalberto"
    assert result["data"]["attributes"]["celular"] == "11009900990"
    assert result["data"]["attributes"]["email_corporativo"] == "Adalberto11@mail.com"
    assert result["data"]["attributes"]["categoria"] == "Premium"
    assert result["data"]["attributes"]["saldo"] == 22000.0

    repository_mock.get_person.assert_called_once_with(1)


def test_find_person_not_found():
    repository_mock = MagicMock()
    repository_mock.get_person.return_value = None

    controller = JuridicPersonFinderController(repository_mock)

    with pytest.raises(ValueError, match="Juridic person not found"):
        controller.find(999)
