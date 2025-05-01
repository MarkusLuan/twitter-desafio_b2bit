import datetime
import re

from werkzeug.exceptions import BadRequest

def validar_formato_data(j: dict, campo: str):
    "Função para validar se o campo de data está em um formato aceito"

    data = None
    formatos_data = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]
    
    formatos_data_str = ' ou '.join(formatos_data)\
        .replace("%Y", "ANO")\
        .replace("%m", "MÊS")\
        .replace("%d", "DIA")\
        .replace("%H", "HORA")\
        .replace("%M", "MINUTO")\
        .replace("%S", "SEGUNDO")
    
    for formato in formatos_data:
        try:
            data = datetime.datetime.strptime(j[campo], formato)
        except:
            ...
    
    if data:
        j[campo] = data
    else:
        raise BadRequest(f"O campo '{campo}' não foi preenchido corretamente!\nData deverá ser informada nos seguintes formatos {formatos_data_str}")

def validar_campos_obrigatorios(j: dict, campos_obrigatorios: list):
    "Função para validar se faltou passar algum parametro no JSON"

    pattern_email = re.compile(r"(\w+)\@(\w{3,}[\w\.]{0,})")

    for campo in campos_obrigatorios:
        # Valida se o campo foi informado
        if campo not in j:
            raise BadRequest(f"O campo '{campo}' não foi informado!")

        # Valida campo de e-mail
        if campo == "email" and not pattern_email.match(j[campo]):
            raise BadRequest("O endereço de e-mail é invalido!")
        
        # Validar campo de data
        if campo.startswith("dt_"):
            validar_formato_data(j, campo)

def remover_campos(j: dict, campos: list):
    "Função para remover campos de um json"

    for campo in campos:
        if campo in j:
            del j[campo]