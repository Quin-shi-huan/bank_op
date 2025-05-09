from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.fisic_person import FisicPersonTable
from .fisic_person_repository import FisicPersonRepository

class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(

            data=[
                (
                    [
                        mock.call.query(FisicPersonTable),
                        mock.call.filter(FisicPersonTable.id == 1),
                        mock.call.one()
                    ],
                    [
                    FisicPersonTable(
                        nome_completo="João da Silva",
                        idade=30,
                        email="joao@email.com",
                        celular="11999999999",
                        categoria="C",
                        renda_mensal=5000.0,
                        saldo=2000.0
                    )
                ]
            )
        ]
    )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class MockConnectionNoResult:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_insert_person():
    mock_connection = MockConnection()
    repo = FisicPersonRepository(mock_connection)

    repo.insert_person(
        renda_mensal=3000.0,
        idade=28,
        nome_completo="Maria Oliveira",
        celular="11988888888",
        email="maria@email.com",
        categoria="A",
        saldo=1500.0
    )

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_insert_person_exception():
    mock_connection = MockConnection()
    mock_connection.session.commit.side_effect = Exception("Commit failed")
    repo = FisicPersonRepository(mock_connection)

    with pytest.raises(Exception, match="Commit failed"):
        repo.insert_person(
            renda_mensal=4000.0,
            idade=35,
            nome_completo="Erro Exemplo",
            celular="0000000000",
            email="erro@email.com",
            categoria="erro",
            saldo=100.0
        )

        mock_connection.session.rollback.assert_called_once()

def test_get_person():
    mock_connection = MockConnection()
    repo = FisicPersonRepository(mock_connection)

    repo.get_person(1)

    mock_connection.session.query.assert_called_once_with(FisicPersonTable)
    mock_connection.session.filter.assert_called_once_with(FisicPersonTable.id == 1)
    mock_connection.session.one.assert_called_once()

def test_get_person_no_result():
    mock_connection = MockConnectionNoResult()
    repo = FisicPersonRepository(mock_connection)

    response = repo.get_person(999)

    assert response is None
