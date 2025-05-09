from typing import Dict
from src.models.sqlite.entities.juridic_person import JuridicPersonTable
from src.models.sqlite.interfaces.juridic_person_repository import JuridicPersonRepositoryInterface
from src.errors.error_type.http_not_found import HttpNotFoundError
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class JuridicPersonFinderController(PersonFinderControllerInterface):
    def __init__(self, juridic_person_repository: JuridicPersonRepositoryInterface):
        self.__juridic_person_repository = juridic_person_repository

    def find(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_in_db(self, person_id: int) -> JuridicPersonTable:
        person = self.__juridic_person_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("Juridic person not found!")

        return person

    def __format_response(self, juridic_person: JuridicPersonTable) -> Dict:
        return {
            "data": {
                "type": "Juridic Person",
                "count": 1,
                "attributes": {
                    "faturamento": juridic_person.faturamento,
                    "idade": juridic_person.idade,
                    "nome_fantasia": juridic_person.nome_fantasia,
                    "celular": juridic_person.celular,
                    "email_corporativo": juridic_person.email_corporativo,
                    "categoria": juridic_person.categoria,
                    "saldo": juridic_person.saldo
                }
            }
        }
