from unittest.mock import MagicMock
# import pytest
from src.controllers.fisic_person_creator_controller import FisicPersonCreatorController
from src.views.fisic_person_creator_view import FisicPersonCratorView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

def test_fisic_person_crator_view():
    fake_person_info = {"name": "João", "cpf": "123.456.789-00"}
    expected_response = {"id": 1, "name": "João", "cpf": "123.456.789-00"}

    controller_mock = MagicMock(spec=FisicPersonCreatorController)
    controller_mock.create.return_value = expected_response

    view = FisicPersonCratorView(controller=controller_mock)
    request = HttpRequest(body=fake_person_info)

    response = view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body == expected_response
    controller_mock.create.assert_called_once_with(fake_person_info)
