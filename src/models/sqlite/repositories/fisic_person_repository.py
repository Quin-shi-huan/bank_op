from sqlalchemy.exc import NoResultFound
from src.models.sqlite.entities.fisic_person import FisicPersonTable

class FisicPersonRepository:
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def insert_person(
            self, renda_mensal: float, idade: int, nome_completo: str,
            celular: str, email: str, categoria: str, saldo: float
        ) -> None:

        with self.__db_connection as database:
            try:
                person_data = FisicPersonTable(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )

                database.session.add(person_data)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_person(self, person_id : int) -> FisicPersonTable:
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                    .query(FisicPersonTable)
                    .filter(FisicPersonTable.id == person_id)
                    .one()
                )

                return person
            except NoResultFound:
                return None
