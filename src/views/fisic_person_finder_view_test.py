from unittest.mock import MagicMock
#import pytest
from src.views.fisic_person_finder_view import FisicPersonFinderView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


def test_fisic_person_finder_view():
    person_id = 1

    fake_response = {
        "data": {
            "type": "Fisic Person",
            "count": 1,
            "attributes": {
                "renda_mensal": 5000.0,
                "idade": 30,
                "nome_completo": "João",
                "celular": "11999999999",
                "email": "joao@email.com",
                "categoria": "Premium",
                "saldo": 2000.0
            }
        }
    }

    controller_mock = MagicMock()
    controller_mock.find.return_value = fake_response

    view = FisicPersonFinderView(controller=controller_mock)

    http_request = HttpRequest(param={"person_id": person_id})

    http_response = view.handle(http_request)

    assert isinstance(http_response, HttpResponse)
    assert http_response.status_code == 200
    assert http_response.body == fake_response
    controller_mock.find.assert_called_once_with(person_id)
