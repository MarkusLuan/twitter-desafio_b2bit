class FollowerInvalidException (Exception):
    def __init__(self):
        super().__init__("Não é possivel seguir você mesmo!")

class FollowerNotFoundException (Exception):
    def __init__(self):
        super().__init__("Você não segue este usuário!")