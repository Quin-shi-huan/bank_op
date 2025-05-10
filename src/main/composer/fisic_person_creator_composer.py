from src.models.sqlite.repositories.fisic_person_repository import FisicPersonRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.controllers.fisic_person_creator_controller import FisicPersonCreatorController
from src.views.fisic_person_creator_view import FisicPersonCreatorView

def fisic_person_creator_composer():
    model = FisicPersonRepository(db_connection_handler)
    controller = FisicPersonCreatorController(model)
    view = FisicPersonCreatorView(controller)

    return view
