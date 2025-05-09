from unittest.mock import MagicMock
# import pytest
from src.controllers.fisic_person_creator_controller import FisicPersonCreatorController
from src.views.fisic_person_creator_view import FisicPersonCreatorView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

def test_fisic_person_creator_view():
    fake_person_info = {
        "renda_mensal": 5000.0,
        "idade": 30,
        "nome_completo": "João",
        "celular": "11999999999",
        "email": "joao@email.com",
        "categoria": "Premium",
        "saldo": 2000.0
    }

    expected_response = {
        "id": 1, 
        "renda_mensal": 5000.0,
        "idade": 30,
        "nome_completo": "João",
        "celular": "11999999999",
        "email": "joao@email.com",
        "categoria": "Premium",
        "saldo": 2000.0
        }

    controller_mock = MagicMock(spec=FisicPersonCreatorController)
    controller_mock.create.return_value = expected_response

    view = FisicPersonCreatorView(controller=controller_mock)
    request = HttpRequest(body=fake_person_info)

    response = view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body == expected_response
    controller_mock.create.assert_called_once_with(fake_person_info)
