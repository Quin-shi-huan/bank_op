from .juridic_person_creator_validator import juridic_person_creator_validator

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body

def test_person_creator_validator():
    request = MockRequest({
        "faturamento": 5000.0,
        "idade": 30,
        "nome_fantasia": "Julius",
        "celular": "119966004400",
        "email_corporativo": "juliusCeasar@mail.com",
        "categoria": "C",
        "saldo": 1200.0
    })

    juridic_person_creator_validator(request)
