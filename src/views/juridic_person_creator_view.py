from src.validators.juridic_person_creator_validator import juridic_person_creator_validator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from ..controllers.juridic_person_creator_controller import JuridicPersonCreatorController
from .interfaces.view_interface import ViewInterface

class JuridicPersonCreatorView(ViewInterface):
    def __init__(self, controller: JuridicPersonCreatorController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        juridic_person_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(body=body_response, status_code=201)
