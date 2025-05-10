from src.models.sqlite.settings.connection import db_connection_handler
from src.controllers.juridic_person_finder_controller import JuridicPersonFinderController
from src.models.sqlite.repositories.juridic_person_repository import JuridicPersonRepository
from src.views.juridic_person_finder_view import JuridicPersonFinderView

def juridic_person_finder_composer():
    model = JuridicPersonRepository(db_connection_handler)
    controller = JuridicPersonFinderController(model)
    view = JuridicPersonFinderView(controller)

    return view
