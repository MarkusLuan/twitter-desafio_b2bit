import base64

def toBase64(texto: str):
    buffer = texto.encode("utf-8")
    
    return str(
        base64.b64encode(buffer),
        "utf-8"
    )

def fromBase64(texto: str):
    return str(base64.b64decode(texto),
        "utf-8"
    )