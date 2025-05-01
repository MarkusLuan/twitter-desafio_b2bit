class InvalidLoginException (Exception):
    def __init__(self):
        super().__init__("Usuário ou Senha Invalidos!")

class UserNotFoundException (Exception):
    def __init__(self):
        super().__init__("Usuário não encontrado!")