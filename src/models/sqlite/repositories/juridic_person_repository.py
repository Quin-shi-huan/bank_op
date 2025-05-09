from sqlalchemy.exc import NoResultFound
from src.models.sqlite.entities.juridic_person import JuridicPersonTable
from src.models.sqlite.interfaces.juridic_person_repository import JuridicPersonRepositoryInterface

class JuridicPersonRepository(JuridicPersonRepositoryInterface):
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def insert_person(
            self, faturamento: float, idade: int, nome_fantasia: str,
            celular: str, email_corporativo: str, categoria: str, saldo: float
        ) -> None:

        with self.__db_connection as database:
            try:
                person_data = JuridicPersonTable(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo
                )

                database.session.add(person_data)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_person(self, person_id : int) -> JuridicPersonTable:
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                    .query(JuridicPersonTable)
                    .filter(JuridicPersonTable.id == person_id)
                    .one()
                )

                return person
            except NoResultFound:
                return None
