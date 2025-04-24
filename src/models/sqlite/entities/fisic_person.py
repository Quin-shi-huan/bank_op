from sqlalchemy import Column, REAL, BIGINT, String, INTEGER
from src.models.sqlite.settings.base import Base


class FisicPersonTable(Base): # pylint: disable=too-few-public-methods
    __tablename__ = "pessoa_fisica"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    renda_mensal = Column(REAL, nullable=False)
    idade = Column(INTEGER, nullable=False)
    nome_completo = Column(String, nullable=False)
    celular = Column(String, nullable=True)
    email = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return (
            f"Renda_mensal={self.renda_mensal},\n"
            f"Idade={self.idade},\n"
            f"Nome={self.nome_completo},\n"
            f"Tel={self.celular},\n"
            f"Email={self.email},\n"
            f"Categoria={self.categoria},\n"
            f"Saldo={self.saldo}"
        )
