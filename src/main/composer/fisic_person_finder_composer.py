from src.models.sqlite.settings.connection import db_connection_handler
from src.controllers.fisic_person_finder_controller import FisicPersonFinderController
from src.models.sqlite.repositories.fisic_person_repository import FisicPersonRepository
from src.views.fisic_person_finder_view import FisicPersonFinderView

def fisic_person_finder_composer():
    model = FisicPersonRepository(db_connection_handler)
    controller = FisicPersonFinderController(model)
    view = FisicPersonFinderView(controller)

    return view
