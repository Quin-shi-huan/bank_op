from typing import Dict
from src.models.sqlite.entities.fisic_person import FisicPersonTable
from src.models.sqlite.interfaces.fisic_person_repository import FisicPersonRepositoryInterface
from src.errors.error_type.http_not_found import HttpNotFoundError
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class FisicPersonFinderController(PersonFinderControllerInterface):
    def __init__(self, fisic_person_repository: FisicPersonRepositoryInterface):
        self.__fisic_person_repository = fisic_person_repository

    def find(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_in_db(self, person_id: int) -> FisicPersonTable:
        person = self.__fisic_person_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("Fisic person not found!")

        return person

    def __format_response(self, fisic_person: FisicPersonTable) -> Dict:
        return {
            "data": {
                "type": "Fisic Person",
                "attributes": {
                    "renda_mensal": fisic_person.renda_mensal,
                    "idade": fisic_person.idade,
                    "nome_completo": fisic_person.nome_completo,
                    "celular": fisic_person.celular,
                    "email": fisic_person.email,
                    "categoria": fisic_person.categoria,
                    "saldo": fisic_person.saldo
                }
            }
        }
