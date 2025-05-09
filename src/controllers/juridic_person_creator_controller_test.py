import pytest
from .juridic_person_creator_controller import JuridicPersonCreatorController

class MockJuridicPersonRepository:
    def insert_person(
        self, faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo
    ) -> None: pass

def test_create():
    person_info = {
        "faturamento": 5000.0,
        "idade": 30,
        "nome_fantasia": "Julius Ceasar",
        "celular": "119966004400",
        "email_corporativo": "juliusCeasar@mail.com",
        "categoria": "C",
        "saldo": 1200.0
    }
    controller = JuridicPersonCreatorController(MockJuridicPersonRepository())
    response = controller.create(person_info)

    assert response["data"]["type"] == "Juridic Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_error():
    person_info = {
        "faturamento": 5000.0,
        "idade": 30,
        "nome_fantasia": "Julius Ceasar123",
        "celular": "1122334455",
        "email_corporativo": "juliusCeasar@mail.com",
        "categoria": "C",
        "saldo": 1200.0
    }

    controller = JuridicPersonCreatorController(MockJuridicPersonRepository())

    with pytest.raises(Exception):
        controller.create(person_info)
