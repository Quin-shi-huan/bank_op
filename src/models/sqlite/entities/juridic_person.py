from sqlalchemy import Column, REAL, BIGINT, String, INTEGER
from src.models.sqlite.settings.base import Base


class JuridicPersonTable(Base): # pylint: disable=too-few-public-methods
    __tablename__ = "pessoa_juridica"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    faturamento = Column(REAL, nullable=False)
    idade = Column(INTEGER, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=True)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return (
            f"Faturamento={self.faturamento},\n"
            f"Idade={self.idade},\n"
            f"Nome={self.nome_fantasia},\n"
            f"Tel={self.celular},\n"
            f"Email={self.email_corporativo},\n"
            f"Categoria={self.categoria},\n"
            f"Saldo={self.saldo}"
        )
