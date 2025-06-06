import base64
import hashlib

def toBase64(texto: str):
    """ Função codifca o texto em base64 """

    buffer = texto.encode("utf-8")
    
    return str(
        base64.b64encode(buffer),
        "utf-8"
    )

def fromBase64(texto: str):
    """ Função decodifca o texto de base64 """

    return str(base64.b64decode(texto),
        "utf-8"
    )

def hash(texto: str):
    """ Função para encriptar senhas """

    # Embaça o texto com outros caracteres antes de criptografar
    texto = f"xoQxfTJ210I{texto}_b2xhMT"
    buffer = texto.encode("utf-8")
    _hash = hashlib.md5(buffer)
    
    return _hash.hexdigest()