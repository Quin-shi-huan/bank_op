from abc import ABC, abstractmethod
from src.models.sqlite.entities.fisic_person import FisicPersonTable

class FisicPersonRepositoryInterface(ABC):
    @abstractmethod
    def insert_person(
            self, renda_mensal: float, idade: int, nome_completo: str,
            celular: str, email: str, categoria: str, saldo: float
        ) -> None: pass

    @abstractmethod
    def get_person(self, person_id: int) -> FisicPersonTable:
        pass
