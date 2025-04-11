from sqlalchemy import Column, REAL, BIGINT, String, INTEGER
from src.models.sqlite.settings.base import Base


class JuridicPerson(Base):
    __tablename__ = "pessoa_juridica"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    faturamento = Column(REAL, nullable=False)
    idade = Column(INTEGER, nullable=False)
    nome_completo = Column(String, nullable=False)
    celular = Column(String, nullable=True)
    email = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return f"Fisic Person [name={self.nome_completo}, idade={self.idade}, email={self.email}]"
