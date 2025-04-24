from sqlalchemy import Column, REAL, BIGINT, String, INTEGER
from src.models.sqlite.settings.base import Base


class FisicPersonTable(Base): # pylint: disable=too-few-public-methods
    __tablename__ = "pessoa_fisica"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    renda_mensal = Column(REAL, nullable=False)
    idade = Column(INTEGER, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=True)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return f"Juridic Person [name={self.nome_completo}, idade={self.idade}, email={self.email}]"
