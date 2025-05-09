from src.validators.fisic_person_creator_validator import fisic_person_creator_validator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from ..controllers.fisic_person_creator_controller import FisicPersonCreatorController
from .interfaces.view_interface import ViewInterface

class FisicPersonCreatorView(ViewInterface):
    def __init__(self, controller: FisicPersonCreatorController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        fisic_person_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(body=body_response, status_code=201)
