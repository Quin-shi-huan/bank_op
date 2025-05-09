import pytest
from .fisic_person_creator_controller import PersonCreatorController

class MockFisicPersonRepository:
    def insert_person(
        self, renda_mensal, idade, nome_completo, celular, email, categoria, saldo
    ) -> None: pass

def test_create():
    person_info = {
        "renda_mensal": 5000.0,
        "idade": 30,
        "nome_completo": "Julius Ceasar",
        "celular": "119966004400",
        "email": "juliusCeasar@mail.com",
        "categoria": "C",
        "saldo": 1200.0
    }
    controller = PersonCreatorController(MockFisicPersonRepository())
    response = controller.create(person_info)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_error():
    person_info = {
        "renda_mensal": 5000.0,
        "idade": 30,
        "nome_completo": "Julius Ceasar123",
        "celular": "1122334455",
        "email": "juliusCeasar@mail.com",
        "categoria": "C",
        "saldo": 1200.0
    }

    controller = PersonCreatorController(MockFisicPersonRepository())

    with pytest.raises(Exception):
        controller.create(person_info)
