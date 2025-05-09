from typing import Dict
import re
from src.models.sqlite.interfaces.fisic_person_repository import FisicPersonRepositoryInterface
from .interfaces.person_creator_controller import PersonCreatorControllerInterface

class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, fisic_person_repository: FisicPersonRepositoryInterface):
        self.__fisic_person_repository = fisic_person_repository

    def create(self, person_info: Dict) -> Dict:
        renda_mensal = person_info["renda_mensal"]
        idade = person_info["idade"]
        nome_completo = person_info["nome_completo"]
        celular = person_info["celular"]
        email = person_info["email"]
        categoria = person_info["categoria"]
        saldo = person_info["saldo"]


        self.__validate_nome_completo(nome_completo)
        self.__insert_person_in_db(
            renda_mensal, idade, nome_completo, celular, email, categoria, saldo
        )
        formated_response = self.__format_response(person_info)

        return formated_response

    def __validate_nome_completo(self, nome_completo: str) -> None:
        non_valid_characters = re.compile(r'[^a-zA-Z-\s]')

        if non_valid_characters.search(nome_completo):
            raise ValueError("Invalid Character!")

    def __insert_person_in_db(
        self, renda_mensal: float, idade: int, nome_completo: str,
        celular: str, email: str, categoria: str, saldo: float
        ) -> None:
        self.__fisic_person_repository.insert_person(
            renda_mensal, idade, nome_completo, celular, email, categoria, saldo
            )

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
