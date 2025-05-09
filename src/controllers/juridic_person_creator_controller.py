from typing import Dict
import re
from src.models.sqlite.interfaces.juridic_person_repository import JuridicPersonRepositoryInterface
from .interfaces.person_creator_controller import PersonCreatorControllerInterface

class JuridicPersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, juridic_person_repository: JuridicPersonRepositoryInterface):
        self.__juridic_person_repository = juridic_person_repository

    def create(self, person_info: Dict) -> Dict:
        faturamento = person_info["faturamento"]
        idade = person_info["idade"]
        nome_fantasia = person_info["nome_fantasia"]
        celular = person_info["celular"]
        email_corporativo = person_info["email_corporativo"]
        categoria = person_info["categoria"]
        saldo = person_info["saldo"]


        self.__validate_nome_fantasia(nome_fantasia)
        self.__insert_person_in_db(
            faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo
        )
        formated_response = self.__format_response(person_info)

        return formated_response

    def __validate_nome_fantasia(self, nome_fantasia: str) -> None:
        non_valid_characters = re.compile(r'[^a-zA-Z-\s]')

        if non_valid_characters.search(nome_fantasia):
            raise ValueError("Invalid Character!")

    def __insert_person_in_db(
        self, faturamento: float, idade: int, nome_fantasia: str,
        celular: str, email_corporativo: str, categoria: str, saldo: float
        ) -> None:
        self.__juridic_person_repository.insert_person(
            faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo
            )

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Juridic Person",
                "count": 1,
                "attributes": person_info
            }
        }
