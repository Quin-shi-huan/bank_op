from src.models.sqlite.repositories.juridic_person_repository import JuridicPersonRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.controllers.juridic_person_creator_controller import JuridicPersonCreatorController
from src.views.juridic_person_creator_view import JuridicPersonCreatorView

def juridic_person_creator_composer():
    model = JuridicPersonRepository(db_connection_handler)
    controller = JuridicPersonCreatorController(model)
    view = JuridicPersonCreatorView(controller)

    return view
