from src.views.http_types.http_response import HttpResponse
from .error_type.http_bad_request import HttpBadRequest
from .error_type.http_not_found import HttpNotFoundError
from .error_type.http_unprocessable_entity_error import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequest, HttpNotFoundError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body= {
                "errors" : [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body= {
            "errors" : [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
