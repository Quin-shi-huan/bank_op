from abc import ABC, abstractmethod
from src.models.sqlite.entities.juridic_person import JuridicPersonTable

class JuridicPersonRepositoryInterface(ABC):
    @abstractmethod
    def insert_person(
            self, faturamento: float, idade: int, nome_fantasia: str,
            celular: str, email_corporativo: str, categoria: str, saldo: float
        ) -> None: pass

    @abstractmethod
    def get_person(self, person_id: int) -> JuridicPersonTable:
        pass
