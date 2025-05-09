from .fisic_person_creator_validator import fisic_person_creator_validator

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body

def test_person_creator_validator():
    request = MockRequest({
        "renda_mensal": 5000.0,
        "idade": 30,
        "nome_completo": "João",
        "celular": "11999999999",
        "email": "joao@email.com",
        "categoria": "Premium",
        "saldo": 15000.0
    })

    fisic_person_creator_validator(request)
