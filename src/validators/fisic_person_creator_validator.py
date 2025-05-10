from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_type.http_unprocessable_entity_error import HttpUnprocessableEntityError

def fisic_person_creator_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        renda_mensal: float
        idade: int
        nome_completo: constr(min_length=1)
        celular: constr(min_length=1)
        email: constr(min_length=1)
        categoria: constr(min_length=1)
        saldo: float

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
